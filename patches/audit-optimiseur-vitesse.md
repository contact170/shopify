# Audit : un « optimiseur de vitesse » actif dans le thème publié

Constaté le 05/09/2026 sur le thème **Version finale 04092026** (MAIN), lu via
l'API Admin en lecture seule.

## Chaîne de rendu

```
layout/theme.liquid
  └─ {% render "head_metas" %}          ← 1re ligne du <head>
       └─ {% render "vital" %}
  └─ {% render "social-meta-tags" %}
       └─ {% render "essential" %}
```

Les deux snippets `vital` et `essential` ne font pas partie du thème d'origine.
Ils s'exécutent sur **toutes les pages**, panier compris.

## 1. `snippets/vital.liquid` — fabrication d'un faux score LCP

Le fichier injecte cet élément en tout début de page :

```html
<div id="fv-loading-icon" data-optimizer="layout"
     data-google-vendor="loading-indicator" aria-hidden="true">Γ</div>
```

Son style est encodé en base64 dans un `@import url("data:text/css;base64,…")`.
Décodé :

```css
#fv-loading-icon {
  width: 99vw;  height: 99vh;
  font-size: 190vw;
  opacity: 0.0001;
  z-index: -99;
  pointer-events: none;
}
```

Un caractère grec `Γ` en corps 190vw, occupant tout l'écran, à une opacité de
0,0001 — invisible à l'œil, mais peint instantanément par le navigateur.

Vient ensuite un script obfusqué en triple encodage :

```html
<script>eval(decodeURIComponent(atob('KGZ1bmN0aW9uKCkl…')))</script>
```

Décodé, il tient en cinq lignes :

```js
(function() {
  setTimeout(function() {
    var element = document.getElementById('fv-loading-icon');
    if (element) { element.remove(); }
  }, 1500);
})();
```

**Lecture.** Le plus gros élément peint de la page devient ce glyphe, disponible
en quelques millisecondes. Les outils de mesure (PageSpeed Insights, Lighthouse)
enregistrent donc un excellent *Largest Contentful Paint*. L'élément est ensuite
supprimé au bout d'une seconde et demie. L'opacité de 0,0001 plutôt que 0 n'est
pas un hasard : un élément totalement transparent est ignoré par l'algorithme
LCP de Chrome.

L'attribut `data-google-vendor="loading-indicator"` n'a aucune fonction
technique. Il sert à ce que l'élément paraisse légitime à l'inspection.

Le score monte. La page ne va pas plus vite pour un client réel.

## 2. `snippets/vital.liquid` — script tiers bloquant

```html
<script src="//cdn.shopify.com/s/files/1/0998/9029/9168/files/loader.init.js"></script>
```

Sans `defer` ni `async`, dans le `<head>` : il **bloque le rendu** de chaque page.

L'identifiant de boutique `1/0998/9029/9168` n'est pas le vôtre — vos fichiers
sont sous `1/0326/3132/4811`. C'est donc du JavaScript exécutable, servi depuis
une boutique Shopify tierce, qui s'exécute sur toutes vos pages, panier inclus.
Qui administre cette boutique peut en modifier le contenu à tout moment.

Je n'ai pas pu lire ce fichier : le proxy réseau de mon environnement bloque
l'accès à ce domaine, par curl comme par récupération web.

## 3. `snippets/essential.liquid` — neutralisation de scripts

Un `MutationObserver` surveille toute la page et intercepte les `<script>`
injectés. Pour trois familles d'URL :

- `assets/storefront/features` (fonctions natives Shopify)
- `assets/shopify_pay` (bouton Shop Pay)
- `connect.facebook.net` (**pixel Meta**)

il exécute :

```js
e.setAttribute("data-src", e.src);
e.removeAttribute("src");
```

Le script est vidé de sa source : le navigateur ne le charge pas. Il réécrit
aussi le `asyncLoad` de Shopify pour que les scripts d'applications attendent un
évènement maison, `asyncLazyLoad`.

**Le point à vérifier.** Ce mécanisme suppose que quelque chose restaure les
`data-src` et déclenche `asyncLazyLoad`. Je n'ai trouvé ce code dans aucun
fichier du thème — ni `custom.liquid`, ni `vital.liquid`, ni `essential.liquid`,
ni les layouts. Il se trouve vraisemblablement dans `loader.init.js`, que je ne
peux pas lire.

Un élément inquiète : le changelog de `snippets/custom.liquid` indique

> 04/09/2026 — retrait du bloc « loadJSscripts » (résidu d'une ancienne app
> d'optimisation) : il appelait observer.disconnect() alors que `observer`
> n'était jamais défini → ReferenceError systématique.

Autrement dit, une partie de ce dispositif était déjà cassée et a été retirée.
Si la restauration en dépendait, **le pixel Meta ne se charge plus**.

## Vérification en 30 secondes

Sur votre site, `F12` → onglet **Console** :

```js
document.querySelectorAll('script[data-src]:not([src])')
```

- Liste vide → les scripts ont bien été restaurés, le dispositif fonctionne.
- Liste non vide → ces scripts ne se sont jamais chargés. Regardez si
  `connect.facebook.net` y figure.

Puis onglet **Réseau**, filtre `facebook`, rechargez : la requête vers
`connect.facebook.net` part-elle ?

Faites le test sur une page produit et sur le panier.

## Enjeux

**Mesure.** Vos scores PageSpeed ne décrivent pas ce que vivent vos clients.
Avec un mobile à 0,69 % de conversion contre 3,11 % en desktop, piloter la
performance sur un chiffre fabriqué est un handicap réel.

**Publicité.** Si le pixel Meta est neutralisé, vos campagnes remontent des
conversions incomplètes et l'optimisation de Meta travaille sur des données
tronquées.

**Sécurité.** Un `eval()` de code obfusqué et un script tiers non maîtrisé
s'exécutent sur vos pages de panier.

**Conformité.** Servir aux outils de mesure un contenu conçu pour eux et retiré
ensuite est le genre de pratique que Google et Shopify sanctionnent.

## Marche à suivre

1. **Identifier la provenance.** Cherchez dans vos applications installées un
   optimiseur de vitesse. Si c'est une prestation d'agence, demandez-leur ce que
   fait `loader.init.js`.
2. **Faire le test console ci-dessus** avant toute décision.
3. **Si rien de légitime n'en dépend** : sur un thème dupliqué, retirer
   `{% render "vital" %}` de `snippets/head_metas.liquid` et
   `{% render "essential" %}` de `snippets/social-meta-tags.liquid`, puis
   mesurer la vraie performance avec WebPageTest ou l'onglet Réseau.

Ne retirez rien sur le thème publié sans être passé par une copie : `loader.init.js`
fait peut-être aussi des choses utiles que je ne peux pas voir.

## Note : `snippets/scripts.liquid` n'est plus appelé

Le script `githubfix.myshopify.com/…/component-3.0.96.js` que j'avais signalé
provenait de l'export de mai. Dans le thème publié, `layout/theme.liquid` ne
contient plus `{% render "scripts" %}`, et `social-meta-tags.liquid` non plus.
Le fichier subsiste mais **n'est chargé sur aucune page**. L'alerte portait sur
le mauvais fichier ; le script réellement actif est `loader.init.js`.
