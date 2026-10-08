# Audit des incohérences – daewoo-security.fr

*Audit du 8 octobre 2026. Lecture seule : rien n'a été modifié sur le site.*
*Périmètre : 233 adresses, soit 107 fiches produits, 27 collections, 21 pages, 69 articles de blog, les politiques et la page d'accueil.*

Pour chaque point : **ce qui ne va pas**, **où**, et **la décision à prendre**.
Les points juridiques sont des signalements, pas un avis juridique : à faire valider par votre juriste ou expert-comptable si besoin.

---

## 🔴 PRIORITÉ 1 – Retours, rétractation, garantie (juridique et confiance)

### 1.1 « Retour gratuit » encore affiché sur la collection Élite
Le retour en cas de rétractation est **à la charge du client** (CGV, page Livraison & Retour, politique de remboursement, page Retours SAV), mais la collection Élite promet le contraire **à 5 endroits** :
- « Garantie 2 ans **Retour gratuit sous 14 jours** »
- « **Retour Gratuit**, 14 jours »
- « 14 jours pour changer d'avis **avec retour gratuit** »
- « Expédition rapide, **retour gratuit sous 14 jours** »
- « **Retour gratuit 14 jours** »

📍 `/collections/systeme-dalarme-pa501z`
✅ À faire : remplacer par « Retour possible sous 14 jours », comme sur la collection Touch.

### 1.2 « Satisfait ou remboursé » dans 4 articles de blog
Cette formule laisse entendre un remboursement sans condition ni frais, ce qui contredit votre politique.
- « 2 ans + 14 jours **satisfait ou remboursé** » : `/blogs/news/alarme-maison-sans-abonnement-amazon`, `…-castorama`, `…-leroy-merlin`
- « 14 jours de **satisfaction garantie** » : `/blogs/news/alarme-maison-sans-abonnement-sans-wifi`

✅ À faire : remplacer par « 14 jours pour changer d'avis ».

### 1.3 Remboursement des frais de livraison : la page Livraison contredit les CGV
- **Page Livraison & Retour** : « Le remboursement (**hors frais de livraison initiaux**) intervient sous 14 jours ».
- **CGV art. 9.4** : « Le remboursement **inclut** les frais de livraison standard initiaux ». C'est ce que prévoit le Code de la consommation (L221-24).

📍 `/pages/livraison-retour`
✅ À faire : aligner la page sur les CGV.

### 1.4 La politique de remboursement contient des clauses contraires aux CGV, et probablement à la loi
C'est la page que Shopify indique en priorité aux IA, via `/agents.md`.
- « Le produit doit être intact, **non ouvert** » : le client a le droit d'ouvrir et de tester le produit. Les CGV le reconnaissent elles-mêmes (dépréciation seulement en cas de manipulation excessive).
- « 14 jours (**hors week-end et jours fériés**) » : le délai légal se compte en jours calendaires.
- « Le droit de rétractation ne peut être exercé pour **les produits descellés** » : cette exception vise l'hygiène et la santé, pas les alarmes. La même phrase figure sur la page Livraison & Retour.
- Barème de décote (−50 % / −20 % / −10 %) : il n'existe pas dans les CGV. À valider.

📍 `/policies/refund-policy`, avec une partie aussi sur `/pages/livraison-retour`
✅ À faire : réécrire la politique de remboursement à partir de l'article 9 des CGV, qui est propre.

### 1.5 Garantie : « frais de retour à la charge de l'acheteur » et « 1 an pour le déstockage »
Le bloc Garantie de la page Livraison & Retour indique :
- « Frais de retour : **À la charge de l'acheteur** ». Or, au titre de la garantie légale de conformité, la réparation ou le remplacement se fait **sans frais** pour le client (CGV art. 10.1).
- « 2 ans (**1 an pour les produits déstockage**) ». Pour un produit **neuf**, la garantie légale de conformité est de 2 ans. Une réduction à 1 an n'est possible que pour du matériel d'occasion.

📍 `/pages/livraison-retour`
✅ À faire : confirmer avec votre juriste, puis corriger.

### 1.6 🚨 Adresse e-mail d'un client affichée publiquement (RGPD)
Le widget d'avis affiche **« gerardmottais@gmail.com »** comme nom d'auteur d'un avis (« Télécommande améliorée… »).
📍 Visible sur **42 pages** (collections et fiches produits).
✅ À faire **en premier** : dans l'application d'avis, modifier le nom affiché pour cet avis (par exemple « Gérard M. »).

### 1.7 La politique de confidentialité ne couvre que l'application, pas le site
`/policies/privacy-policy` s'intitule « Politique de confidentialité – **Application Daewoo Home Connect** ». Rien ne couvre les données du site : commandes, cookies, newsletter, paiement. Pourtant, les mentions légales renvoient vers cette page pour le site.
✅ À faire : ajouter une section « Site daewoo-security.fr » ou créer une politique dédiée.

---

## 🟠 PRIORITÉ 2 – Coordonnées de l'entreprise

### 2.1 Quatre numéros de téléphone différents
| Numéro | Où | Commentaire |
|---|---|---|
| **05 47 74 29 40** | Accueil, À propos, mentions légales, CGV, coordonnées | Numéro officiel |
| **06 60 89 74 83** | `/pages/livraison-retour`, `/pages/retours-sav` | ❓ Portable, à remplacer ? |
| 09 70 80 65 12 | 3 fiches cartes SIM Afone | OK, c'est le numéro d'Afone |
| 04 82 53 93 06 | CGV, rubrique médiateur | OK, c'est le médiateur |

✅ À décider : le 06 doit-il rester sur les pages de retour ?

### 2.2 Deux adresses pour la société
- **15 allée James Watt, Immeuble 2000 Watt, 33700 Mérignac** : partout.
- **« 6 Léon Maurane, 33700 Mérignac »** : `/pages/demandes-rgpd-confidentialite`, comme adresse du DPO. ❓ Ancienne adresse ?
- (35 rue Jacques Prévert : point relais de retour sur `/pages/retours-sav`. Normal.)

### 2.3 Horaires du service client
- Accueil : « 05 47 74 29 40 du **lundi au samedi, 9 h – 19 h** ».
- Collection Touch, blogs : « équipe joignable **5j/7** » (donc pas le samedi ?).

✅ À décider : 5 ou 6 jours ? Quels horaires ?

---

## 🟠 PRIORITÉ 3 – Délais d'expédition et de livraison

Au moins **7 versions différentes** coexistent :
| Message | Où |
|---|---|
| « Expédié sous **24 h** » / « avant midi, expédiée le jour même » | Accueil, packs Touch et Touch XL, offre spéciale, page Livraison |
| « Livraison sous **24 à 48 h** » | ~50 fiches accessoires |
| « Expédié sous **2 jours** » / « Livraison sous **2 jours ouvrés** » | Packs Vigilia, caméras (~39 fiches) |
| « En stock ! Expédié sous **2 jours ouvrables** » | 16 fiches, dont les 4 packs Sécurité Intégrale |
| « Expédition sous 2 jours · Livraison sous **4 à 5 jours** » | 8 fiches Élite |
| « livraison en **48 h** » | Blog `comment-choisir-le-bon-systeme-d-alarme-pour-votre-maison` |
| « **2 à 3 jours ouvrés** à compter de l'expédition » | CGV art. 7.1 |

✅ À décider : un seul message de référence (par exemple « Expédié sous 24 h ouvrées si commandé avant midi, livré en 2 à 3 jours ouvrés »). On l'applique ensuite partout, de préférence via un bloc du thème pour ne le modifier qu'une fois.

### 3.1 Livraison offerte en Belgique ?
- Pied de page, toutes les pages : « Livraison offerte dès 50 € **en France et en Belgique** ».
- Mêmes mentions sur 3 collections d'accessoires.
- Mais la page Livraison et la politique d'expédition disent : offerte **France métropolitaine** uniquement, Europe « calculé au paiement ».

✅ À décider : la Belgique est-elle offerte dès 50 € ? Il faut ensuite corriger l'un ou l'autre.

---

## 🟡 PRIORITÉ 4 – Caractéristiques techniques contradictoires

| Sujet | Version A | Version B | À trancher |
|---|---|---|---|
| **Batterie centrale Élite** | **10 h** : accueil, 8 fiches packs Élite, starter pack | **12 h** : collection Élite, `comment-choisir-son-alarme`, comparateur, fiche détecteur de fumée WSD501 | ❓ |
| **Accessoires max Vigilia** | **60** : fiches Vigilia, accueil, comment-choisir | **90** : collection Vigilia (« Jusqu'à 90 accessoires compatibles »), qui dit aussi 60 sur la même page | ❓ probablement 60 |
| **Sirène Touch XL (7")** | **95 dB** : collection Touch, comparateur | **90 dB** : 4 fiches AM350 à AM353 (« écran 7'', sirène intégrée 90 dB ») | ❓ |
| **Temps d'installation** | 20 min (VIG501, offres Vigilia) | 30 min (autres Vigilia, accueil, blogs) | Harmoniser (« environ 30 min ») |
| **Nombre de gammes** | « **3 gammes** » : À propos, page configurateur | La gamme **Key (SA501)** est vendue et présente dans le comparateur | ❓ La Key compte-t-elle ? |

---

## 🟡 PRIORITÉ 5 – Textes anglais et modèles par défaut

### 5.1 Textes de modèle anglais visibles sur 5 fiches caméras
« Need help? … We'll get back to you… », « Shipping Information – **Use this text to answer questions…** », « Customer Support », « FAQ's ».
📍 `camera-daewoo-w503-autonome-haute-resolution-wifi-1080p`, `camera-daewoo-w503-avec-panneau-solaire-…`, `camera-ep506-exterieure-rotative-filaire`, `camera-interieure-rotative-ip506p`, `camera-w512mw-exterieure-rotative-1440p-avec-panneau-solaire`
✅ À faire : supprimer ce bloc dans le modèle de fiche caméra.

### 5.2 Widget d'avis en anglais
- « **Let customers speak for us from 1057 reviews** » : 42 pages.
- « **Write a review** » : 15 pages.
- Dates au format américain (10/05/2026 pour le 5 octobre).

✅ À faire : traduire dans les réglages de l'application d'avis et passer au format JJ/MM/AAAA.

---

## 🟢 PRIORITÉ 6 – Catalogue

### 6.1 Offres en double, toutes indexées par Google
| Produit | Prix |
|---|---|
| OFFRE EXCLUSIVE \| Pack ÉLITE (`…-elite-…-sans-abonnement`) | 593,90 € |
| OFFRE EXCLUSIVE \| Pack ÉLITE PA501Z Double Caméra Solaire (`…-copie`) | 699,90 € |
| OFFRE EXCLUSIVE \| Pack TOUCH (`…-touch-…`) | 499,90 € |
| OFFRE EXCLUSIVE \| Pack TOUCH XL (`…-touch-…-1`) | 809,90 € |
| OFFRE EXCLUSIVE \| Pack Vigilia 2 caméras (`…-vigilia-…`) | 359,90 € |
| OFFRE EXCLUSIVE \| Pack Vigilia Compatible animaux (`…-vigilia-…-2`) | 249,90 € |

Ce sont des produits différents, mais leurs adresses se terminent par `-copie`, `-1` ou `-2`.
✅ À faire : renommer ces adresses (Shopify crée automatiquement la redirection). Coquille au passage : « WiFI GSM ».

### 6.2 Produits « configurateur » indexés par Google
5 produits internes au configurateur sont dans le sitemap, donc visibles dans Google : `configurateur-detecteur-de-fumee-wsd301`, `configurateur-pack-de-3-…` (×4).
✅ À faire : les masquer des moteurs de recherche, ou les retirer du canal Boutique en ligne si le configurateur n'en a pas besoin.

### 6.3 Prix barré égal au prix de vente (fausse promotion)
`configurateur-kit-vigilia-wi-fi` et `daewoo-vigilia-starter-pack` (139,90 / 139,90), `detecteur-de-mouvement-exterieur-wmo501-compatible-avec-lala…` (79,90 / 79,90).
✅ À faire : vider le champ « prix avant réduction ».

### 6.4 Produit en rupture mais toujours indexé
`carte-sd-kingston-64-gb`.

---

## 🟢 PRIORITÉ 7 – Liens et référencement

- **1 lien cassé (404)** : `/apps/gbb/easybundle/2` dans l'article `nathalie-a-securise-sa-residence-secondaire…`
- **Liens de blog vers des produits supprimés**, redirigés vers une collection. Le lecteur ne trouve pas le produit cité :
  - `comment-marc-a-securise-sa-maison…` : WDS301, WPS301, sirène WOS301, caméra EF502
  - `proteger-une-maison-isolee…` : WPS301, sirène solaire WOS301S
  - `nathalie-a-securise…` : sirène WIS502
- **`/collections/systemes-dalarme` redirige vers l'accueil** : liens dans 3 articles. Mieux vaut viser une vraie collection.
- **Liens avec préfixes de marché** `/fr-ch/…` et `/fr-com/…` dans 3 articles (`meilleurs-detecteurs-d-alarme`, `top-5-sirenes-d-alarme`, `alarme-maison-sans-abonnement-amazon`) : remplacer par des liens directs.
- **Page Livraison & Retour** : le lien « SAV » pointe vers `/pages/sav`, qui redirige vers Contact au lieu de `/pages/retours-sav`.
- **Pages sans meta description** : les 7 politiques et `/collections/offres-du-mois-1`. Faible priorité.

---

## Ordre proposé pour demain

1. **5 min** : masquer l'e-mail du client dans le widget d'avis (1.6).
2. **15 min** : corriger « retour gratuit » sur la collection Élite et « satisfait ou remboursé » dans les blogs (1.1, 1.2).
3. **Décisions à prendre ensemble** : téléphone, adresse DPO, horaires, délai d'expédition unique, Belgique, batterie Élite, accessoires Vigilia, sirène Touch XL, gamme Key.
4. **30 min** : réécrire la politique de remboursement et la page Livraison & Retour à partir des CGV (1.3, 1.4, 1.5).
5. Appliquer les décisions de l'étape 3 sur toutes les pages concernées.
6. Textes anglais, catalogue, liens.

Je peux appliquer directement dans Shopify la plupart des corrections des étapes 2, 4, 5 et 6 dès que les décisions sont prises. L'étape 1 se fait dans l'application d'avis.
