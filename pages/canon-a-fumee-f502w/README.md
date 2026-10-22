# Page produit — Canon à fumée F502W

Page dédiée au canon à fumée (`/products/canon-a-fumee-f502w`), construite
avec le même style que les autres fiches accessoires (`accp`), mais avec un
discours propre : **la protection la plus efficace contre le vol** et **les
trois modes de déclenchement**.

Source des chiffres : manuel fabricant du modèle FS-C100T (le F502W est ce
modèle sous marque Daewoo).

## Ce que contient le dossier

| Fichier | Rôle |
| --- | --- |
| `templates/product.canon-fumee.json` | Template réservé au canon à fumée. Les autres accessoires restent sur `acc-premium`. |
| `sections/fumee-video.liquid` | Vidéo de démonstration (fichier Shopify ou lien YouTube / Vimeo). Masquée sur la boutique tant qu'aucune vidéo n'est choisie. |
| `sections/fumee-efficacite.liquid` | « Les autres alertent. Lui, il arrête le vol. » : sirène / caméra / canon à fumée. |
| `sections/fumee-chrono.liquid` | Grand compteur 0 → 8 s et frise 0 s / 1 s / 3 s / 8 s. Chaque étape s'allume quand le compteur l'atteint. |
| `sections/fumee-declenchement.liquid` | Bouton panique, télécommande, application Daewoo Home Connect + encart « box internet coupée ». |
| `sections/fumee-specs.liquid` | Fiche technique complète (18 lignes) et cartes « Bon à savoir ». |
| `sections/fumee-seo.liquid` | Invisible. Données structurées Produit (marque Daewoo, GTIN, 11 caractéristiques, note clients, offre, retour 14 jours). |
| `sections/acc-hero.liquid` | Section partagée. Réglages facultatifs : surtitre, sous-titre, accroche, et case pour masquer les données structurées Shopify. |
| `sections/acc-boite.liquid` | Section partagée. Réglages facultatifs : contenu de la boîte, grille 4 colonnes. |
| `sections/acc-faq-produit.liquid` | Section partagée. Accepte des questions en plus, ajoutées depuis le template. |
| `seo/` | Titre SEO, méta-description et description produit appliqués, plus la sauvegarde des anciennes valeurs (`ancien-avant-maj.json`). |

Les réglages ajoutés aux sections partagées sont **vides ou désactivés par
défaut** : tant qu'ils ne sont pas remplis, les sections se comportent comme
avant, donc aucune autre fiche ne change.

## SEO / GEO

Déjà en ligne (données produit, visibles quel que soit le template) :

- Titre SEO : « Canon à fumée anti-intrusion Daewoo F502W | Sans abonnement » (59 car.)
- Méta-description (146 car.) : 8 s, 150 m³, bouton panique et télécommande, sans abonnement
- Description produit réécrite : chiffres justes (8 s au lieu de « moins de
  30 secondes »), synonymes (générateur de fumée, générateur de brouillard),
  trois modes de déclenchement, liens internes (caméras, recharge F502R,
  configurateur d'alarme)
- FAQ, réponse 6 : refroidissement « environ 2 heures » (manuel fabricant)
  au lieu de « au moins une heure »

Dans le thème de travail (actif à la publication) :

- Données structurées : la marque devient « Daewoo » (Shopify affichait
  « Compatible toutes gammes », le champ fournisseur)
- Titres H2 avec « canon à fumée »
- 6 questions FAQ en plus, à réponse directe (12 au total dans les données
  structurées FAQPage) : durée, danger, sans internet, abonnement,
  installation, après un déclenchement
- Bloc « En résumé » qui reprend la description produit

## Ordre de la page

1. En-tête (prix, panier) — surtitre « La protection la plus efficace contre le vol »
2. Option recharge F502R
3. Vidéo de démonstration (dès qu'elle est ajoutée)
4. Pourquoi c'est la plus efficace
5. 8 secondes (compteur animé)
6. Trois façons de le déclencher
7. Stories vidéo (app Moast)
8. Compatibilité
9. Installation
10. Dans la boîte (bouton panique ajouté)
11. Fiche technique + Bon à savoir
12. Avis, FAQ, produits complémentaires, barre d'achat fixe

Les sections « Son rôle dans votre sécurité » et « En détail » (description
produit) ne sont plus affichées : leur contenu est repris, à jour, dans les
nouvelles sections.

## Mise en ligne

1. Thème de travail : **« Canon à fumée 17102026 (Claude) »** (copie du thème
   publié « Guide Elite 12102026 »).
2. Aperçu : `https://daewoo-security.fr/products/canon-a-fumee-f502w?view=canon-fumee&preview_theme_id=206209450324`
3. Pour publier : publier ce thème depuis l'admin Shopify, **puis** passer le
   produit sur le template `canon-fumee` (fiche produit > Modèle de thème).
   Dans cet ordre : si le produit passe sur `canon-fumee` avant la
   publication, la page s'afficherait avec le template par défaut.

## Vidéo

La vidéo de démonstration est hébergée sur Shopify (Contenu > Fichiers :
`canon-a-fumee-daewoo-f502w-demonstration.mp4`, 1280×720, 45 s). Elle démarre
en sourdine quand elle arrive à l'écran et se met en pause quand on la
quitte. La section « Video — SEO » la décrit pour Google (VideoObject :
adresse du MP4, vignette, durée calculée).

Le lien YouTube reste en secours dans les réglages : il ne sert que si la
vidéo Shopify est retirée. Dans ce cas, la page affiche une vignette et ne
charge le lecteur YouTube qu'au clic, pour éviter le contrôle « Confirmez
que vous n'êtes pas un robot ».
