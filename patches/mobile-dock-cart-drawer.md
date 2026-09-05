# Dock mobile : ouvrir le tiroir au lieu de partir sur /cart

## Le problème

Dans `sections/mobile-dock.liquid`, le bloc `cart` est le **seul** élément du dock
construit sur un `<a href>` :

| Bloc | Élément | Si l'écouteur du tiroir manque |
|---|---|---|
| Menu | `<button aria-controls="MenuDrawer">` | rien ne se passe |
| Recherche | `<a href="/search" aria-controls="SearchDrawer">` | va sur `/search` |
| **Panier** | `<a href="/cart" aria-controls="CartDrawer">` | **va sur `/cart`** |

Le tiroir attache ses écouteurs en balayant le DOM à la connexion
(`document.querySelectorAll('[aria-controls="CartDrawer"]')`), et son
gestionnaire appelle `event.preventDefault()`. L'icône panier du header ouvre
bien le tiroir sur mobile — donc le tiroir fonctionne, et c'est ce lien précis
que le balayage ne couvre pas.

`assets/mobile-dock.js` ne contient aucun code de clic : il ne gère que la
visibilité et la hauteur du dock.

## Le correctif

Il n'essaie pas de deviner pourquoi le balayage rate le lien : il ouvre le
tiroir explicitement, avec deux garde-fous qui le rendent inoffensif dans tous
les cas de figure.

**1.** Dans `sections/mobile-dock.liquid`, bloc `{%- when 'cart' -%}`, remplacer :

```liquid
          <a class="dock__item flex flex-col items-center justify-center gap-1d5 grow shrink-0 cursor-pointer" href="{{ routes.cart_url }}" aria-controls="CartDrawer" aria-expanded="false">
```

par :

```liquid
          <a id="DockCartLink" class="dock__item flex flex-col items-center justify-center gap-1d5 grow shrink-0 cursor-pointer" href="{{ routes.cart_url }}" aria-controls="CartDrawer" aria-expanded="false" data-no-instant>
```

Deux ajouts : un `id` pour cibler le lien, et `data-no-instant` pour cesser de
précharger `/cart` inutilement — c'est ce que fait déjà le lien du header.

**2.** Dans le même fichier, juste après `</nav>` et avant le `{%- endif -%}`
qui ferme la section, ajouter :

```liquid
  <script>
    /* Le panier du dock est le seul bloc bâti sur un <a href> : quand le tiroir
       n'attrape pas ce lien, le navigateur suit le href et le client atterrit
       sur /cart au lieu du tiroir. On ouvre le tiroir explicitement.

       Deux garde-fous :
       - si le gestionnaire du thème a déjà pris la main, il a appelé
         preventDefault() et on ne fait rien ;
       - si le tiroir n'existe pas ou n'est pas encore initialisé, on ne touche
         à rien et le lien vers /cart continue de fonctionner. */
    (function () {
      var link = document.getElementById('DockCartLink');
      if (!link) return;

      link.addEventListener('click', function (event) {
        if (event.defaultPrevented) return;

        var drawer = document.getElementById('CartDrawer');
        if (!drawer || typeof drawer.show !== 'function') return;

        event.preventDefault();
        if (!drawer.hasAttribute('open')) drawer.show(link);
      });
    })();
  </script>
```

## Pourquoi c'est sans risque

- **Le desktop n'est pas concerné** : le dock est une section mobile
  (`enabled_on: custom.overlay`, masquée au-dessus de 768 px).
- **Pas de double ouverture** : `event.defaultPrevented` détecte que le
  gestionnaire du thème s'est déjà exécuté, et `hasAttribute('open')` évite de
  rappeler `show()` sur un tiroir déjà ouvert.
- **Dégradation propre** : si le JS échoue ou si le tiroir est absent, le lien
  se comporte exactement comme aujourd'hui et mène à `/cart`.

## À vérifier après installation

1. Toucher « Panier » dans le dock : le tiroir s'ouvre, l'URL ne change pas.
2. Le toucher une seconde fois pendant que le tiroir est ouvert : rien ne doit
   clignoter ni se rouvrir.
3. Ajouter un produit depuis une fiche : le tiroir doit s'ouvrir normalement.
4. Aller sur `/cart` directement : la page doit toujours s'afficher.
