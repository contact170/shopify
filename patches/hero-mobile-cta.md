# Hero d'accueil — CTA mobile

Fichier concerné : `snippets/dw-hero.liquid` (appelé par la 1re section de
`templates/index.json`, `custom_liquid_UpnCfz` → `{% render 'dw-hero' %}`).

**Mobile uniquement.** Tout le CSS ajouté vit dans le bloc
`@media (max-width: 768px)` déjà présent dans le fichier ; le seul changement
hors media query est l'ajout d'un libellé court masqué par défaut.

## Ce qui ne va pas, mesuré dans le code

**1. Le CTA du configurateur n'est pas un bouton.** C'est un lien souligné :

```css
.daewoo-banner__link { font-size: 13.5px !important; }
```

13,5 px, sans bordure ni fond, hauteur de frappe ~20 px. En dessous du seuil
de 44 px recommandé pour une cible tactile, et visuellement invisible à côté
d'un bouton bleu plein.

**2. Les CTA tombent sous la ligne de flottaison.** Empilement mobile actuel,
depuis le haut du hero :

| Élément | Hauteur approx. |
|---|---|
| Image | 210 px |
| Padding haut | 20 px |
| Badge + gap | 42 px |
| Titre (2 lignes à 27 px) + gap | 72 px |
| Preuve sociale + gap | 50 px |
| Prix + gap | 62 px |
| Description + gap | 56 px |
| **→ début des CTA** | **≈ 512 px** |

En ajoutant le bandeau d'annonce et l'en-tête (~115 px), le premier bouton
commence vers 627 px. Sur un écran de 390 × 844, la zone visible fait environ
650 px : le bouton est à la limite, le second en dessous.

## Les modifications

### 1 — Markup : libellé court pour mobile

Remplacer :

```liquid
          <a href="{{ dw_url_confi }}" class="daewoo-banner__link">
            Je ne sais pas lequel choisir&nbsp;: guidez-moi en 2&nbsp;min <span class="daewoo-banner__arrow">→</span>
          </a>
```

par :

```liquid
          <a href="{{ dw_url_confi }}" class="daewoo-banner__link">
            <span class="daewoo-banner__link-long">Je ne sais pas lequel choisir&nbsp;: guidez-moi en 2&nbsp;min</span>
            <span class="daewoo-banner__link-short">Guidez-moi en 2&nbsp;min</span>
            <span class="daewoo-banner__arrow">→</span>
          </a>
```

### 2 — CSS de base : masquer le libellé court

Juste après la ligne `.daewoo-banner__link:hover { color: #0f43b8 !important; }`,
ajouter :

```css
  .daewoo-banner__link-short { display: none; }
```

### 3 — Mobile : image resserrée

Dans le bloc `@media (max-width: 768px)`, remplacer :

```css
      max-height: 210px;
```

par :

```css
      max-height: 168px;
```

### 4 — Mobile : les CTA deviennent deux vrais boutons, remontés

Toujours dans `@media (max-width: 768px)`, remplacer ces trois lignes :

```css
    .daewoo-banner__ctas { max-width: 100%; width: 100%; }
    .daewoo-banner__btn { width: 100%; padding: 15px 18px; font-size: 15px; }
    .daewoo-banner__link { font-size: 13.5px !important; }
```

par :

```css
    /* Les boutons remontent au-dessus de la description : sur mobile, la
       phrase générique ne mérite pas de repousser l'action sous la ligne
       de flottaison. */
    .daewoo-banner__badge       { order: 1; }
    .daewoo-banner__title       { order: 2; }
    .daewoo-banner__proof       { order: 3; }
    .daewoo-banner__price       { order: 4; }
    .daewoo-banner__ctas        { order: 5; }
    .daewoo-banner__description { order: 6; }
    .daewoo-banner__trust       { order: 7; }

    .daewoo-banner__ctas { max-width: 100%; width: 100%; gap: 10px; margin-top: 6px; }

    /* Bouton principal : plus grand que sur desktop, pas plus petit. */
    .daewoo-banner__btn {
      width: 100%;
      min-height: 56px;
      padding: 17px 20px;
      font-size: 16.5px;
      border-radius: 8px;
    }
    .daewoo-banner__btn--primary { box-shadow: 0 10px 28px rgba(21,82,214,0.32); }

    /* Le configurateur devient un vrai bouton secondaire : même largeur,
       même hauteur de frappe, hiérarchie donnée par le contour plutôt que
       par la taille. */
    .daewoo-banner__link {
      display: flex;
      width: 100%;
      min-height: 54px;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 14px 18px;
      border: 2px solid var(--blue);
      border-radius: 8px;
      background: #fff;
      font-size: 15px !important;
      font-weight: 700 !important;
      text-decoration: none;
      text-align: center;
    }
    .daewoo-banner__link-long  { display: none; }
    .daewoo-banner__link-short { display: inline; }
```

## Résultat attendu

- Le configurateur passe de 13,5 px souligné à un bouton contourné de 54 px de
  haut, pleine largeur — même poids tactile que le bouton principal.
- Le bouton principal passe de 15 px / ~50 px de haut à 16,5 px / 56 px.
- Les deux CTA remontent d'environ **100 px** (42 px d'image + 56 px de
  description déplacée) et repassent au-dessus de la ligne de flottaison sur
  un écran de 390 × 844.
- Le libellé du configurateur passe de 49 à 21 caractères sur mobile, et tient
  sur une ligne.

Desktop inchangé : le libellé long reste affiché, le lien reste un lien.

## À vérifier

1. Sur un téléphone, la page d'accueil : les deux boutons sont visibles sans
   faire défiler.
2. Le bouton contourné affiche « Guidez-moi en 2 min » sur une seule ligne.
3. Sur ordinateur : le hero est strictement identique à avant.
