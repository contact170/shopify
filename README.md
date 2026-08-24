# Thème Daewoo Security — fichiers de travail

Ce dépôt contient l'export du thème Shopify (`theme_export__…zip`) ainsi que les
fichiers modifiés, extraits à la racine dans l'arborescence du thème, pour que les
modifications restent lisibles dans les diffs Git.

## Fichiers suivis

| Fichier | Rôle |
| --- | --- |
| `theme_export__daewoo-security-fr-concept__18MAY2026-1100am.zip` | Export du thème daté du 18/05/2026 (mis à jour avec les modifications ci-dessous) |
| `templates/page.cloud.json` | Gabarit de la page `/pages/cloud` |

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
