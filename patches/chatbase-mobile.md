# Bulle Chatbase sur mobile — CSS à ajouter dans `snippets/custom.liquid`

> Réécrit le 05/09/2026. Le repositionnement au-dessus du dock existe déjà dans
> `custom.liquid` ; ce document ne traite que ce qui reste à faire.

## Où coller

Dans `snippets/custom.liquid`, **remplacer** le bloc existant :

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

par le bloc ci-dessous.

## Le CSS

```css
  @media screen and (max-width: 767px) {
    /* ─── 1. Libellé « Une question ? » retiré sur mobile ───
       Le bouton mesure 192 × 55 px avec le libellé, 55 × 55 sans.
       font-size: 0 neutralise le texte quelle que soit sa balise — y compris
       un nœud texte nu — puis on rétablit la taille sur l'icône seule. */
    #chatbase-bubble-button {
      width: 56px !important;
      min-width: 0 !important;
      padding: 0 !important;
      gap: 0 !important;
      font-size: 0 !important;
      overflow: hidden !important;
      justify-content: center !important;

      /* ─── 2. Bouton collé à la barre du bas, sans espace ─── */
      bottom: var(--mobile-dock-height, 64px) !important;
      transition: opacity .2s ease !important;
    }

    #chatbase-bubble-button svg,
    #chatbase-bubble-button img {
      font-size: 1rem !important;
      width: 24px !important;
      height: 24px !important;
      flex: 0 0 auto !important;
    }

    #chatbase-message-bubbles {
      bottom: calc(69px + var(--mobile-dock-height, 64px)) !important;
    }

    /* ─── 3. Fiches produit : effacer la bulle quand la barre d'achat est là ───
       La barre d'achat et la bulle occupent la même bande, juste au-dessus du
       dock. Les décaler l'une par rapport à l'autre ne suffit pas : on masque
       la bulle tant que la barre est affichée, et elle revient ensuite. */
    body:has(.product-sticky-form__card:not(.invisible)) #chatbase-bubble-button {
      opacity: 0 !important;
      pointer-events: none !important;
    }
  }
```

## Pourquoi l'alignement seul ne règle pas le chevauchement

Mesuré dans le thème :

- `sections/main-product.liquid:908` — la barre d'achat est
  `product-sticky-form w-full fixed z-20 bottom-0`.
- `assets/mobile-dock.css:118` — quand le dock est actif, elle reçoit
  `transform: translateY(calc(var(--mobile-dock-height) * -1))`, donc elle se
  pose **exactement sur le dock**.
- Sa carte contient un bouton de `--sp-11` de haut plus deux paddings de
  `--sp-4` : environ **75 à 80 px**.

La bulle fait 55 px de haut. Aujourd'hui elle occupe la bande allant de
`dock + 16` à `dock + 71`. Collée à la barre, elle irait de `dock` à
`dock + 55`. **Dans les deux cas elle est entièrement à l'intérieur de la barre
d'achat**, qui monte jusqu'à `dock + 80`. Un décalage de 16 px ne peut pas en
sortir.

C'est pour ça que la règle 3 masque la bulle au lieu de la déplacer.

Le retrait du libellé (règle 1) aide aussi de son côté : la bulle passe de
208 px à 56 px de large, et ne peut plus atteindre le bouton d'achat, qui est
aligné à droite de la barre.

## Effet de bord à corriger

Les deux règles de dégagement du `.footer-copyright` dans `custom.liquid` ont
été calculées pour un bouton de 208 px de large :

```css
  @media screen and (min-width: 1024px) {
    .footer-copyright { padding-inline-end: 220px !important; }
  }
```

Le libellé n'étant retiré **que sur mobile**, cette règle desktop reste juste :
n'y touchez pas. En revanche celle sous 1024 px réserve 72 px en bas pour un
bouton qui n'en fait plus que 56 : vous pouvez ramener `+ 72px` à `+ 56px`.

## À vérifier

1. Fiche produit, faire défiler jusqu'à l'apparition de la barre d'achat : la
   bulle doit disparaître en fondu, puis revenir en remontant.
2. Page d'accueil et panier : la bulle est une pastille ronde, collée au dock,
   icône bien centrée.
3. Desktop : rien ne doit changer — le libellé reste, la position aussi.

**Non testé de mon côté** : je n'ai pas accès au DOM de Chatbase depuis cet
environnement. Si l'icône disparaît avec le texte, c'est qu'elle n'est ni un
`svg` ni un `img` : inspectez le bouton et ajoutez sa balise à la règle qui
rétablit `font-size`.
