# Correctif galeries — pages caméras W512MW / W503 / W503SP

Date : 31/08/2026
Thème de travail : « Correctif galeries cameras 31082026 » (duplication du thème en ligne
« Site version finale 31082026 »).

## Constat

Les trois fiches caméras n'utilisent pas la galerie produit standard du thème.
Dans `templates/product.w512mw.json`, `product.w503.json` et `product.w503-solaire.json`,
la section `main-product` porte `"disabled": true` : la galerie du thème (et donc ses
vignettes) n'est jamais rendue. Toute la page est une section sur mesure :

| Fiche  | Suffixe de template | Section |
|--------|---------------------|---------|
| W512MW | `w512mw`            | `product-w512mw-landing.liquid` |
| W503   | `w503`              | `product-w503-landing.liquid` (`includes_solar_panel: false`) |
| W503SP | `w503-solaire`      | `product-w503-landing.liquid` (`includes_solar_panel: true`) |

Ces sections sélectionnent les images **par position** :

```liquid
assign gallery = product.images
assign hero_image  = gallery[0]   <- W503 : correct
assign hero_image  = gallery[1]   <- W512MW : DÉCALÉ d'un cran
```

Conséquences avant correctif :

1. **W512MW** : l'image principale affichée était `gallery[1]`, c'est-à-dire
   « vision panoramique 360° », et non la photo produit (qui est bien l'image
   mise en avant du produit). Les 4 visuels de rubriques étaient eux aussi
   décalés (`gallery[2]` à `gallery[5]`).
2. **Les trois fiches** : aucune vignette, la section sur mesure n'en a jamais
   comporté et la galerie du thème est désactivée.
3. Des images optimisées n'étaient affichées nulle part : 2 sur 7 pour la W512MW,
   3 sur 8 pour la W503SP.

## Correctif appliqué

1. `product-w512mw-landing.liquid` : `hero_image = gallery[0]`,
   `feat_image_1..4 = gallery[1..4]` — même convention que la section W503.
2. Ajout d'une bande de vignettes sous l'image principale dans les deux sections
   (`.w512-thumbs` / `.w503-thumbs`) : toutes les images du produit, cliquables,
   qui remplacent l'image principale sans rechargement.
   - vignettes servies en 160 px, `loading="lazy"` : quelques Ko chacune ;
   - l'image principale reste servie en 1200 px avec `srcset`.
3. Aucun changement sur les données produit : l'ordre des médias et l'image mise
   en avant restent inchangés.

## Détail technique du correctif

Bloc ajouté sous l'image principale (identique dans les deux sections, préfixe `w512`/`w503`) :

```liquid
{%- if gallery.size > 1 -%}
  <div class="w512-thumbs w512-reveal">
    {%- for img in gallery -%}
      {%- assign thumb_alt = img.alt | default: product.title | strip_newlines | strip -%}
      <button type="button" class="w512-thumb{% if forloop.first %} is-active{% endif %}"
        data-hero-src="{{ img | image_url: width: 1200 }}"
        data-hero-srcset="{{ img | image_url: width: 600 }} 600w, {{ img | image_url: width: 900 }} 900w, {{ img | image_url: width: 1200 }} 1200w"
        aria-label="{{ thumb_alt | escape }}">
        <img src="{{ img | image_url: width: 176 }}" width="88" height="88" loading="lazy" alt="{{ thumb_alt | escape }}">
      </button>
    {%- endfor -%}
  </div>
{%- endif -%}
```

L'image principale reçoit un identifiant (`W512HeroMedia-{{ section.id }}` /
`W503HeroMedia-{{ section.id }}`) et l'attribut `fetchpriority="high"`
(recommandation Shopify pour l'image LCP, gain direct sur la vitesse d'affichage).

Le script de la section fait le remplacement au clic :

```js
var heroMedia = root.querySelector('#W512HeroMedia-{{ section.id }}');
var heroImg = heroMedia ? heroMedia.querySelector('img') : null;
var thumbs = root.querySelectorAll('.w512-thumb');
if (heroImg && thumbs.length) {
  thumbs.forEach(function (thumb) {
    thumb.addEventListener('click', function () {
      heroImg.setAttribute('srcset', thumb.getAttribute('data-hero-srcset'));
      heroImg.setAttribute('src', thumb.getAttribute('data-hero-src'));
      heroImg.setAttribute('alt', thumb.getAttribute('aria-label'));
      thumbs.forEach(function (other) { other.classList.remove('is-active'); });
      thumb.classList.add('is-active');
    });
  });
}
```

Tailles des fichiers après correctif :

| Fichier | Avant | Après |
|---|---|---|
| `sections/product-w512mw-landing.liquid` | 37 839 o | 40 198 o |
| `sections/product-w503-landing.liquid`   | 42 577 o | 44 936 o |

## Poids des images (vérifié le 31/08/2026)

Toutes les images des trois fiches sont en **WebP 2048 × 2048, statut READY**.

| Fiche  | Images | Poids stocké total | Image la plus lourde |
|--------|--------|--------------------|----------------------|
| W512MW | 7      | 979 ko             | 204 ko (installation murale) |
| W503   | 5      | 787 ko             | 248 ko (détection forme humaine) |
| W503SP | 8      | 1,04 Mo            | 248 ko (détection forme humaine) |

Le poids réellement téléchargé par le visiteur est bien inférieur : Shopify sert
des dérivées redimensionnées (`image_url: width:`) — 1200 px pour l'image
principale, 1000 px pour les visuels de rubriques, 176 px pour les vignettes.

Doublon à traiter : sur la W503SP, `camera-autonome-daewoo-w503-panneau-solaire.webp`
et `camera-w503-daewoo-panneau-solaire-fixation-murale.webp` font exactement
77 716 octets — très probablement le même fichier importé deux fois.

## Mise en ligne

Thème à publier : **« Correctif galeries cameras 31082026 »**
(duplication du thème en ligne, correctif appliqué dessus, rien d'autre modifié).
Aperçu : `https://daewoo-security.fr/?preview_theme_id=202618962260`
