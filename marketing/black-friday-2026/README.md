# Black Friday 2026 : relance des devis et des comptes sans achat

Campagne de 3 e-mails pour relancer deux publics qui ont montré de l'intérêt
sans acheter : les personnes qui ont reçu un devis, et celles qui ont créé un
compte sur daewoo-security.fr.

Chiffres relevés dans Shopify le 13/11/2026.

## 1. Les deux publics

| Public | Volume | Détail |
|---|---|---|
| **A. Devis non finalisés** | 26 devis | Commandes provisoires au statut « Facture envoyée », non payées, créées depuis le 1er novembre 2025. Environ 9 750 € TTC en tout, soit 375 € en moyenne par devis. 25 contacts sur 26 sont abonnés aux e-mails ; 13 devis viennent de personnes qui n'ont jamais commandé. |
| **B. Comptes sans achat** | 1 353 contacts | Comptes clients actifs, aucune commande, abonnés aux e-mails (1 607 comptes au total, dont 400 créés ces 12 derniers mois). |

Le public A est petit mais très qualifié : un devis à 375 € en moyenne, c'est un
projet concret. Il mérite un traitement presque individuel (voir l'étape 3).

**Leçon des Black Friday précédents** : le code `BLACK10` de 2024 (-10 % dès
500 € d'achat, une fois par client) n'a été utilisé **aucune fois**. Le code
`BLACK` de 2020 (-7 % sur 3 collections, sans minimum) a été utilisé 10 fois.
Le minimum de 500 € a très probablement freiné les achats : l'offre proposée
ici n'a pas de minimum.

## 2. L'offre (à valider)

- **-10 % sur tout le site, sans minimum d'achat**
- Code : **`BLACKFRIDAY26`**, une utilisation par client
- Valable du **mardi 24 novembre** (accès anticipé pour les devis) au
  **lundi 30 novembre à 23h59** (Cyber Monday)

À décider avant la création du code :

- **Le pourcentage.** Il apparaît dans les 3 e-mails : s'il change, les
  fichiers sont régénérés en une commande (`python3 generer.py` après
  modification des constantes en tête du fichier).
- **Les packs « OFFRE EXCLUSIVE ».** Ils sont déjà remisés d'environ 25 %
  (Pack ÉLITE à 593,90 € au lieu de 794,20 €). Par défaut, le code s'ajoute à
  cette remise. Pour l'éviter, limitez le code aux autres collections.

Les liens des e-mails passent par `daewoo-security.fr/discount/BLACKFRIDAY26`,
ce qui **applique le code automatiquement** au panier. Ces liens ne marchent
qu'une fois le code créé dans Shopify.

## 3. Calendrier

| Date d'envoi | E-mail | Public |
|---|---|---|
| **Mar. 24/11, 10h** | `1-devis-acces-anticipe.html` : accès anticipé | A. Devis |
| **Ven. 27/11, 8h** | `2-comptes-sans-achat.html` : lancement | B. Comptes sans achat |
| **Lun. 30/11, 9h** | `3-relance-dernier-jour.html` : dernier jour | A + B, sauf ceux qui ont commandé depuis le 24/11 |

**Le plus efficace pour le public A** : le 24/11, en plus de l'e-mail (ou à
sa place), ouvrir chacun des devis concernés dans *Commandes > Commandes
provisoires*, appliquer la remise de 10 %, puis cliquer sur **« Envoyer la
facture »** en y collant le message ci-dessous. Le client reçoit son devis
recalculé avec un bouton de paiement : il n'a plus rien à refaire. Comptez
environ une heure pour les 26 devis.

> Bonjour,
>
> Comme promis, voici votre devis mis à jour au tarif Black Friday : -10 %
> sur l'ensemble de votre configuration, jusqu'au lundi 30 novembre à 23h59.
> Vous pouvez le régler en toute sécurité depuis le bouton ci-dessous.
>
> Votre projet a évolué ? Répondez simplement à cet e-mail : nous ajustons
> votre configuration avec plaisir.
>
> À très vite,
> L'équipe Daewoo Security

## 4. Mise en place pas à pas

1. **Créer le code** dans *Réductions > Créer une réduction > Montant de
   réduction sur la commande* : `BLACKFRIDAY26`, 10 %, sans minimum, une
   utilisation par client, du 24/11 00h00 au 30/11 23h59.
2. **Étiqueter les clients du public A** avec le tag `devis-bf26` : ouvrir
   chaque devis « Facture envoyée » depuis novembre 2025, cliquer sur le
   client, ajouter le tag. Si des devis ont été faits uniquement par e-mail,
   en dehors de Shopify, ajoutez aussi ces clients.
3. **Créer les segments** dans *Clients > Segments* (requêtes testées le
   13/11/2026) :
   - **BF26 – Devis non finalisés**
     ```
     customer_tags CONTAINS 'devis-bf26'
     ```
   - **BF26 – Comptes sans achat**
     ```
     customer_account_status = 'ENABLED' AND number_of_orders = 0 AND email_subscription_status = 'SUBSCRIBED' AND customer_tags NOT CONTAINS 'devis-bf26'
     ```
   - **BF26 – Relance dernier jour** (exclut ceux qui ont commandé depuis le 24/11)
     ```
     email_subscription_status = 'SUBSCRIBED' AND (customer_tags CONTAINS 'devis-bf26' OR (customer_account_status = 'ENABLED' AND number_of_orders = 0)) AND (number_of_orders = 0 OR last_order_date < 2026-11-24)
     ```
4. **Créer les 3 campagnes** et programmer les envois aux dates du calendrier.
   - Si l'outil accepte un e-mail en HTML, collez le contenu du fichier
     `.html`.
   - Dans l'éditeur par blocs de Shopify Email, reprenez textes, boutons et
     liens bloc par bloc depuis les fichiers.
   - La salutation utilise `{{ customer.first_name }}` (syntaxe Shopify).
     Dans Klaviyo, remplacez-la par `{{ first_name|default:'' }}`.
5. **S'envoyer un test** de chaque e-mail, sur ordinateur et sur téléphone,
   et cliquer sur chaque lien.

**Consentement** : n'envoyez ces e-mails qu'aux contacts abonnés (Shopify
Email le fait automatiquement). Un des 26 devis vient d'une personne non
abonnée : pour elle, pas de campagne, uniquement le renvoi de son devis
décrit à l'étape 3.

## 5. Objets et textes d'aperçu

Pour chaque e-mail, l'objet principal est en premier ; la variante peut
servir à un test A/B si votre outil le permet.

**E-mail 1, devis (24/11)**
- Objet : `Votre devis passe au tarif Black Friday (avant tout le monde)`
- Variante : `Accès anticipé : -10 % sur votre devis Daewoo Security`
- Aperçu : `Votre devis à -10 % avant tout le monde, jusqu'au 30/11 à 23h59. Sans abonnement, garantie 2 ans.`

**E-mail 2, comptes sans achat (27/11)**
- Objet : `Black Friday : -10 % sur toutes nos alarmes sans abonnement`
- Variante : `Votre alarme sans abonnement, à prix Black Friday`
- Aperçu : `-10 % sur tout le site, jusqu'au 30/11 à 23h59. Livraison offerte dès 50 €, garantie 2 ans.`

**E-mail 3, dernier jour (30/11)**
- Objet : `Dernier jour : -10 % jusqu'à minuit`
- Variante : `Plus que quelques heures pour votre alarme à -10 %`
- Aperçu : `Le Black Friday se termine ce soir à minuit. Votre code : BLACKFRIDAY26`

## 6. Ce qui est affirmé dans les e-mails (vérifié sur le site)

Sans abonnement · Garantie 2 ans · Livraison offerte dès 50 € en France
métropolitaine et en Belgique, sous 24 à 48 h ouvrées · 14 jours de
rétractation · Équipe technique basée près de Bordeaux · Configurateur en
ligne (`/pages/configurateur_2`). Les prix des 4 packs mis en avant sont ceux
du 13/11/2026 : à revérifier la veille de l'envoi.

## 7. Suivi des résultats

À regarder le 1er décembre :

- **Taux d'ouverture et de clic** de chaque e-mail (rapport de campagne).
- **Nombre d'utilisations** du code `BLACKFRIDAY26` (*Réductions*).
- **Devis transformés** : commandes provisoires du public A passées en
  « Terminée ».
- **Chiffre d'affaires attribué** à chaque campagne.

## Fichiers

| Fichier | Rôle |
|---|---|
| `1-devis-acces-anticipe.html` | E-mail 1, public A |
| `2-comptes-sans-achat.html` | E-mail 2, public B |
| `3-relance-dernier-jour.html` | E-mail 3, A + B |
| `generer.py` | Régénère les 3 e-mails (offre, code et dates en tête du fichier) |
