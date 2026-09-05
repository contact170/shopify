# Bulle Chatbase sur mobile

> **Corrigé le 05/09/2026.** La version précédente de ce document proposait de
> repositionner la bulle au-dessus du dock mobile. C'était déjà fait : la règle
> existe dans `snippets/custom.liquid` depuis le 04/09/2026. Le document est
> réécrit en conséquence.

## Ce qui est déjà en place

`snippets/custom.liquid`, rendu en fin de `<body>` sur toutes les pages :

```css
@media screen and (max-width: 767px) {
  #chatbase-bubble-button {
    bottom: calc(16px + var(--mobile-dock-height, 64px)) !important;
  }
  #chatbase-message-bubbles {
    bottom: calc(85px + var(--mobile-dock-height, 64px)) !important;
  }
}
```

La bulle est donc déjà remontée au-dessus du dock. Les sélecteurs exacts sont
`#chatbase-bubble-button` et `#chatbase-message-bubbles`.

## Le vrai problème : la taille, pas la position

Le commentaire du fichier documente la mesure :

> Depuis l'activation du libellé « Une question ? », le bouton Chatbase mesure
> **192 × 55 px** (contre **55 × 55** avant), soit ~208 px de large avec son
> offset.

C'est le **libellé** qui prend la place, pas la bulle. Sans lui, le bouton
redevient une pastille ronde de 55 px.

## Option 1 — Retirer le libellé (recommandé)

Dans le tableau de bord **Chatbase → votre agent → Connect / Embed → Chat
interface**, videz le champ du libellé du bouton (« Une question ? »).

Le bouton repasse à 55 × 55 px, la gêne disparaît, et vous gardez le support
sur mobile. Aucune modification de code.

Effet de bord à corriger ensuite : les deux règles de dégagement du
`.footer-copyright` dans `custom.liquid` (220 px à droite en desktop, 72 px en
bas sous 1024 px) ont été calculées pour un bouton de 208 px de large. Une fois
le libellé retiré, elles réservent trop d'espace — ramenez 220 px à ~80 px.

## Option 2 — Masquer la bulle sur mobile

Si vous voulez vraiment la supprimer, dans `snippets/custom.liquid`, à
l'intérieur du bloc `@media screen and (max-width: 767px)` existant :

```css
    #chatbase-bubble-button,
    #chatbase-message-bubbles {
      display: none !important;
    }
```

Deux limites :

- Le script Chatbase **continue de se charger** sur mobile, avec son coût. Seule
  la désactivation de l'intégration (Personnaliser → Paramètres du thème →
  Intégrations d'applications → Chatbase) supprime ce coût — mais elle vaut
  aussi pour le desktop.
- Vous perdez un canal de support sur 79 % de votre trafic. Sur des systèmes à
  200–1000 €, une question sans réponse est souvent une vente perdue.

## À ne pas faire

N'utilisez pas un sélecteur du type `iframe[src*="chatbase.co"]` : il masquerait
aussi le Franck intégré dans le contenu des pages `/pages/assistance`.
