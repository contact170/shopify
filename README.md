# Thème Daewoo Security — fichiers de travail

Ce dépôt contient l'export du thème Shopify (`theme_export__…zip`) ainsi que les
fichiers modifiés, extraits à la racine dans l'arborescence du thème, pour que les
modifications restent lisibles dans les diffs Git.

## Fichiers suivis

| Fichier | Rôle |
| --- | --- |
| `theme_export__daewoo-security-fr-concept__18MAY2026-1100am.zip` | Export du thème daté du 18/05/2026 (mis à jour avec les modifications ci-dessous) |
| `templates/page.cloud.json` | Gabarit de la page `/pages/cloud` |
| `templates/page.avis-clients.json` | Gabarit de la page `/pages/avis-clients-2` |
| `sections/reviews-summary.liquid` | Bandeau de synthèse des avis (temps réel) |
| `sections/judgeme-appearance.liquid` | Harmonisation du widget d'avis Judge.me |

## Refonte de la page Cloud (`templates/page.cloud.json`)

Objectifs :

1. **Lever la contradiction avec le positionnement « Sans abonnement »** : la page
   annonce dès le titre et le chapô que le Cloud est une **option facultative**, et
   une section entière rappelle ce qui fonctionne sans le moindre abonnement.
2. **Expliquer clairement l'apport du Cloud** : une section « À quoi sert le Cloud ? »
   (carte SD locale vs copie en ligne) et quatre bénéfices concrets remplacent le
   paragraphe unique, non ponctué, de l'ancienne version.
3. **Éclaircir la page** : suppression de la bannière photo sombre en pleine largeur ;
   fonds blanc (`#ffffff`) et bleu très clair (`#f2f3ff`) en alternance, texte marine
   (`#0c1e4a`), accents bleus (`#0b61cd`).

Structure de la page :

1. Introduction (`rich-text`) — H1 + chapô + boutons
2. « Ce qui reste 100 % sans abonnement » (`multicolumn-with-icons`, 3 colonnes)
3. « Alors, à quoi sert le Cloud ? » (`image-with-text`, capture de l'application
   en visionnage : `Application_Photo_Jardin.jpg`)
4. « Ce que le Cloud change concrètement » (`multicolumn-with-icons`, 4 colonnes)
5. « Si vous choisissez le Cloud » — les 4 formules et leurs tarifs (`multicolumn-with-icons`)
6. FAQ (`faq`) — 6 questions, dont l'avertissement multi-caméras (auparavant répété
   dans chacune des 4 offres)
7. Conclusion (`rich-text`) — rappel « sans abonnement » + boutons

Les tarifs, les durées de conservation (14 jours) et l'avertissement multi-caméras
sont repris à l'identique de l'ancienne page.

À noter : la page ne mentionne pas la saturation de la carte SD comme un risque de
perte, le système écrasant automatiquement les vidéos les plus anciennes lorsque la
carte est pleine. L'argument stockage oppose donc l'écrasement progressif sur carte SD
aux 14 jours complets conservés en ligne.

## Attention : le zip n'est pas le thème en ligne

Vérification du 24/08/2026 : l'export zip date du 18/05/2026 et ne correspond plus au
thème publié (« Theme final 24/08/2026 Pages Accessoires »). Le thème live compte
718 fichiers contre 663 dans le zip, et plusieurs sections ont évolué depuis
(`rich-text`, `image-with-text`, `faq`, `multicolumn-with-icons`, `settings_data.json`).

Le gabarit `templates/page.cloud.json` de ce dépôt a été validé contre les versions
**live** de ces sections : tous les réglages et blocs utilisés existent bien, et la
palette employée (`#0c1e4a`, `#f2f3ff`, `#0b61cd`) est celle du thème en ligne.

Pour les prochaines modifications, mieux vaut repartir d'un export frais du thème publié.

## Page Avis clients (`templates/page.avis-clients.json`)

La page n'affichait que le widget Judge.me, sans titre ni synthèse. Elle comporte
désormais :

1. **Bandeau de synthèse** (`sections/reviews-summary.liquid`) — note moyenne, nombre
   total d'avis et nombre d'avis positifs (4 et 5 étoiles), avec le pourcentage.
2. Le **widget Judge.me** inchangé pour la liste des avis.
3. Une **harmonisation visuelle** (`sections/judgeme-appearance.liquid`).
4. Une conclusion avec liens vers les alarmes et les caméras.

### D'où viennent les chiffres

Judge.me alimente des métachamps de boutique lus à chaque affichage de la page :

| Métachamp | Usage |
| --- | --- |
| `shop.metafields.judgeme.all_reviews_count` | Nombre total d'avis publiés |
| `shop.metafields.judgeme.all_reviews_rating` | Note moyenne |
| `shop.metafields.judgeme.all_reviews_header` | Histogramme — fréquence par étoile, d'où sont déduits les avis positifs (4★ + 5★) |

Aucune valeur n'est écrite en dur : un nouvel avis publié est pris en compte
automatiquement, dès que Judge.me a mis ses métachamps à jour. Si les métachamps sont
absents, le bandeau ne s'affiche pas (aucun « 0 avis » possible).

L'harmonisation cible les classes du widget (`.jdgm-rev`, `.jdgm-star`, …) : tout avis
publié plus tard adopte exactement la même présentation, sans intervention.
