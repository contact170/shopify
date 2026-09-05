# Bulle Chatbase : la faire disparaître (ou la déplacer) sur mobile

Chatbase est une **intégration d'application**, pas du code de thème :

```
config/settings_data.json → current.blocks
  shopify://apps/chatbase/blocks/chatbase-widget/a5677ff3-9ceb-42be-8a77-c14565a88476
```

Son HTML est injecté par l'application dans la page. On ne peut pas le modifier,
mais il vit dans le même document que le thème : du CSS du thème l'atteint sans
problème.

## Avant tout : regarder dans l'éditeur de thème

**Boutique en ligne → Thèmes → Personnaliser → Paramètres du thème → Intégrations
d'applications → Chatbase.**

Si l'application expose un réglage de position ou d'affichage, utilisez-le : c'est
plus propre que du CSS, et ça survivra à ses mises à jour. Je ne peux pas
vérifier d'ici si ce réglage existe.

Le même écran permet de **désactiver complètement** l'intégration — mais elle
disparaît alors aussi du desktop, et c'est la seule option qui supprime vraiment
le chargement du script.

## Option A — La déplacer (recommandé)

Sur vos captures, la bulle ne gêne pas parce qu'elle est grosse : elle gêne
parce qu'elle est **au même endroit que le dock mobile**, en bas. Elle recouvre
le message de livraison, le champ d'instructions, la flèche du carrousel d'avis.

La remonter au-dessus du dock règle la gêne sans vous priver d'un canal de
support sur 79 % de votre trafic.

## Option B — La masquer sur mobile

Si vous préférez vraiment la supprimer.

Dans `layout/theme.liquid`, juste avant `</head>` :

```liquid
    <style>
      @media screen and (max-width: 767px) {
        /* Option A : remonter la bulle au-dessus du dock mobile */
        [id^="chatbase-bubble"] {
          bottom: calc(var(--mobile-dock-height, 64px) + 12px) !important;
        }

        /* Option B : la masquer complètement — décommenter pour l'activer,
           et supprimer la règle ci-dessus. */
        /*
        [id^="chatbase-bubble"] { display: none !important; }
        */
      }
    </style>
```

`--mobile-dock-height` est déjà calculée et posée sur `<html>` par
`assets/mobile-dock.js`, la bulle se cale donc automatiquement au-dessus du dock.

## Vérifier le sélecteur en 30 secondes

`[id^="chatbase-bubble"]` correspond aux identifiants utilisés par le widget
Chatbase. **Je n'ai pas pu le confirmer sur votre site** : le widget n'existe pas
dans les fichiers du thème, il n'apparaît qu'une fois la page chargée.

Pour vérifier : sur ordinateur, ouvrez votre site, clic droit sur la bulle →
**Inspecter**. Dans le panneau, remontez jusqu'au conteneur de la bulle et lisez
son `id`. S'il ne commence pas par `chatbase-bubble`, remplacez le sélecteur par
celui que vous voyez.

Si le sélecteur ne correspond pas, la règle est simplement sans effet — rien ne
casse.

## Ce que le CSS ne fait pas

Masquer la bulle **ne l'empêche pas de se charger**. Le script Chatbase est
toujours téléchargé et exécuté sur mobile, avec son coût sur la vitesse de la
page. Si le but est aussi la performance, seule la désactivation de
l'intégration dans l'éditeur de thème y répond — au prix du desktop.

## Attention à ne pas casser la page Assistance

N'utilisez **pas** un sélecteur du type `iframe[src*="chatbase.co"]` : il
masquerait aussi le Franck intégré dans vos pages `/pages/assistance` et
`/pages/page`, qui est un iframe Chatbase affiché dans le contenu. Le sélecteur
par `id` ci-dessus ne touche que la bulle flottante.
