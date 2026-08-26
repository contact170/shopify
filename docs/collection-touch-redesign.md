# Page collection « Systèmes d'alarme TOUCH / TOUCH XL » (AM301 / AM302)

URL : https://daewoo-security.fr/collections/systeme-dalarme-am301-am302
Template Shopify : `templates/collection.collection-touch.json`

## Objectif

Compléter et « premiumiser » la page, en mettant l'accent sur **la différence entre les
deux centrales** (Touch AM301 4,3'' / Touch XL AM302 7''), refaire la FAQ, et reprendre les
informations utiles de la page Vigilia **avec un design différent**, pour éviter tout effet
de copier-coller entre les deux gammes.

## Parti pris visuel

La page Vigilia utilise un système clair de type Apple (fond `#f5f5f7`, pastilles bleues,
cartes blanches arrondies, grilles régulières). La page Touch adopte un système distinct :

| | Vigilia | Touch (cette page) |
|---|---|---|
| Base | clair, `#f5f5f7` | sombre « backlit », `#05080f` / `#0b1220`, alterné avec du clair `#eef1f7` |
| Accent | bleu unique `#0071e3` | **une couleur par modèle** : bleu `#4da3ff` = Touch, ambre `#f5b544` = Touch XL |
| Libellés | pastilles arrondies en casse normale | eyebrows en capitales espacées, filets fins |
| Structures | grilles régulières 3 colonnes | duel côte à côte, tableau, rail numéroté, frise horaire, bento asymétrique, rail horizontal |
| Typo | pile système | Poppins (déjà utilisée sur la page) |

Le code couleur par modèle est repris partout (duel, tableau, verdict, packs, fiches
techniques) : c'est le fil conducteur qui rend la différence Touch / Touch XL lisible.

## Structure de la page

1. **Hero** — accroche, deux pastilles modèle avec prix, CTA vers le comparatif + configurateur.
2. **Bandeau de confiance** — ligne fine à 4 cellules (installation, sans abonnement, SAV France, garantie).
3. **Duel Touch vs Touch XL** — deux panneaux côte à côte séparés par un « VS », chacun avec sa couleur, sa taille d'écran en grand, ses 4 points clés, son prix et son lien vers la bonne variante produit.
4. **Comparatif détaillé** — tableau de 13 lignes : ce qui diffère (écran, sirène, batterie) et tout ce qui est identique.
5. **Laquelle choisir ?** — deux colonnes « Choisissez la Touch si… » / « Choisissez la Touch XL si… » + rappel que les accessoires sont communs aux deux centrales.
6. **Packs** — Starter, AM340 (mis en avant), AM351, avec badge du modèle de centrale et jauge de couverture.
7. **Carrousel UGC Moast** *(section existante conservée)*.
8. **Anatomie de la centrale** — rail numéroté 01→06 + bande de 4 chiffres clés.
9. **Double pilotage** — écran de la centrale vs application Daewoo Home Connect, en écran partagé clair / sombre.
10. **Une journée avec la Touch** — frise horaire 07:45 → 23:10.
11. **Pourquoi la gamme Touch** — grille bento asymétrique (remplace les cartes à emoji).
12. **Installation** — 3 étapes horizontales + rappels pratiques et lien vers le manuel AM301.
13. **Évolutivité** — rail horizontal de 8 accessoires compatibles avec prix, vers la collection « Compatible gamme Vigilia / Touch ».
14. **Bandeau configurateur** *(contenu d'origine, converti en section `tc-configurateur`)*.
15. **Ils ont choisi Daewoo Security** *(section existante conservée)*.
16. **Avis Judge.me** *(section existante conservée)*.
17. **Détails produit** — accordéon deux colonnes ; chaque ligne indique la valeur Touch, la valeur Touch XL, ou « sur les deux ».
18. **FAQ** — 12 questions réécrites, accordéon sombre, la première portant sur la différence entre les deux centrales. Balisage `FAQPage` (JSON-LD) associé.
19. **CTA final**.

Les sections d'origine remplacées par la refonte, ainsi que les sections héritées déjà
désactivées (portfolio, collage, multicolumn, scrolling banner…), ont été retirées du
template. Leur contenu reste consultable dans `theme-src/collection-touch.base.json`
et dans le thème publié, qui n'est pas modifié. Les sections standard
`main-collection-banner` et `main-collection` sont conservées, désactivées.

## Données utilisées

Toutes les caractéristiques proviennent du contenu déjà publié sur la boutique
(fiche produit AM301/AM302, ancienne FAQ « Détails produit », catalogue accessoires) :

- Écran : 4,3'' (Touch) / 7'' (Touch XL)
- Sirène intégrée : 95 dB / 100 dB
- Batterie de secours : ≈ 4 h / ≈ 20 h
- Wi-Fi 2,4 GHz, GSM 4G avec carte SIM en option, Alexa & Google Home
- Jusqu'à 90 accessoires par centrale, caméras et objets connectés illimités
- Prix packs de départ : 199,90 € / 299,90 €

## Modifier la page

Les sections sont écrites en HTML/CSS autonome dans `theme-src/collection-touch/`,
un fichier par section. Après modification :

```bash
python3 theme-src/build-collection-touch.py
```

Le script produit deux choses :

1. `sections/tc-*.liquid` — les fichiers de section du thème (le HTML/CSS de la source,
   suivi d'un bloc `{% schema %}` généré) ;
2. `templates/collection.collection-touch.json` — le template, assemblé à partir de
   `theme-src/collection-touch.base.json` (l'état du template en ligne avant refonte,
   qui porte les sections conservées telles quelles) et de l'ordre défini dans le script.

Le template ne contient plus de HTML : tout le code vit dans `sections/`, ce qui le rend
lisible et évite de dupliquer du CSS dans le JSON.

## Aperçu

Déployé sur le thème non publié **« Page Touch AM301/AM302 - refonte (Claude) »**
(id `202175971668`) :

<https://daewoo-security.fr/collections/systeme-dalarme-am301-am302?preview_theme_id=202175971668>

Le thème publié n'est pas modifié.
