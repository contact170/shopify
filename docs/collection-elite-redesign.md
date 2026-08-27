# Refonte de la page collection ÉLITE (PA501Z)

Page concernée : <https://daewoo-security.fr/collections/systeme-dalarme-pa501z>
(collection « Système d'alarme ÉLITE », gabarit `collection-elite-2`).

Même méthode que la refonte Touch : le HTML/CSS vit dans des fichiers de section
(`sections/el-*.liquid`), le gabarit ne contient plus que des références de type.
L'ancien gabarit faisait 63 Ko de `custom-liquid` en dur ; le nouveau fait 6,3 Ko.

## Angle éditorial

La gamme Élite n'a pas de « duel » à raconter comme Touch / Touch XL : il n'y a
qu'une centrale, la **PA501Z**. L'angle retenu est sa particularité réelle :

> **la centrale qu'on n'a pas besoin de voir** — ni écran, ni clavier sur le boîtier,
> donc un hub qu'on peut cacher, et tout le pilotage dans l'application.

Les trois autres piliers : la **triple connexion** (Wi-Fi / Ethernet / 4G avec
bascule automatique), la **passerelle Zigbee intégrée** (200 accessoires, radio
chiffrée, compatible périphériques Zigbee tiers), et la **confidentialité**
(volontairement incompatible Alexa / Google Home).

## Différenciation visuelle

Pour éviter l'effet copier-coller avec Vigilia et Touch :

| | Touch / Touch XL | Élite |
|---|---|---|
| Accents | bleu `#1c5fd0` + ambre `#8f5d0c` | quasi-monochrome + **teal** `#0a6068` / `#12a0ad` |
| Encre / texte | `#0b1220` / `#4a5a75` | `#0d1520` / `#4b5a63` |
| Bande alternée | froide `#eef2f8` | neutre verte `#f1f3f2` |
| Structures | duel 2 panneaux, tableau comparatif, rail numéroté, frise horaire, bento | chaîne de secours 3 nœuds, schéma Zigbee en SVG, tuiles 3×2, stepper vertical, fiche technique en 6 blocs |

Police commune au thème : **Poppins**. Contraste vérifié : **0 élément sous le
seuil WCAG AA** (le gris secondaire a dû passer de `#6a7883` à `#5c6a75` pour
tenir 4,5:1 sur la bande `#f1f3f2`).

## Structure de la page

1. **Hero** — « La centrale qu'on n'a pas besoin de voir », 4 chiffres clés, CTA packs + centrale seule.
2. **Bandeau de confiance** (fond sombre) — installation 30 min, sans abonnement, SAV France, garantie.
3. **Triple connexion** — Wi-Fi / Ethernet / 4G en chaîne de secours, + batterie de secours et rappel « les caméras ont besoin du Wi-Fi ».
4. **Zigbee** — la passerelle Zigbee et son périmètre réel + **schéma SVG deux réseaux** (Zigbee d'un côté, radio Daewoo de l'autre), aucune image externe.
5. **Packs** — 3 cartes de hauteur égale : **Kit de départ à partir de 299,90 €** / **Offre exclusive 593,90 €** (mise en avant) / **Pack Tranquillité+ 739,90 €**.
6. **Anatomie** — bandeau photo + 6 tuiles (ni écran ni clavier, sirène, batterie, arrachement, 4 liaisons, modes + SOS de la télécommande WRC501).
7. **Pilotage app** — ce que fait l'application + carte sombre « armer sans téléphone » (télécommande, badge, clavier).
8. **Confidentialité** — pas d'Alexa ni Google Home, par choix ; renvoi vers Touch / Vigilia et le comparateur.
9. **Installation** — stepper vertical 3 étapes + pré-requis + lien vers le manuel complet PA501Z (PDF).
10. **Accessoires** — grille de 12 références compatibles, 4 colonnes, **sans défilement horizontal**.
11. **Configurateur** — bandeau sombre horizontal avec **« jusqu'à −25 % »**.
12. **Témoignage** — section partagée `tc-temoignage`.
13. **Avis Judge.me** *(section existante conservée)*.
14. **Fiche technique** — 6 blocs thématiques.
15. **FAQ** — 12 questions, accordéon + balisage `FAQPage` (JSON-LD). CTA vers le formulaire de contact.
16. **CTA final**.

Les sections d'origine remplacées ont été retirées du gabarit ; leur contenu reste
consultable dans `theme-src/collection-elite.base.json` et dans le thème publié.

## Données utilisées

- Centrale **PA501Z** à 199,90 € (SKU DAPA501Z), 4,52/5 sur 152 avis
- Wi-Fi 2,4 GHz, Ethernet RJ45, **module GSM 4G+ intégré** (carte SIM en option)
- Passerelle **Zigbee** intégrée, jusqu'à **200 accessoires**
- Batterie de secours intégrée, sirène intégrée, détection d'arrachement
- Modes Total / Partiel (Maison) / Désarmé, temporisation, fonction SOS
- **Non compatible Alexa ni Google Home** (choix de conception, mentionné sur la fiche produit)
- Carte SIM M2M Afone 1 an : 85 €
- 12 accessoires actifs de la collection « Compatible gamme Élite »

### Points de vigilance factuels

- **Batterie de secours : 12 h partout** (tranché par le client). La valeur
  apparaît dans la fiche technique, le bandeau « Et si le courant saute ? » et la
  FAQ (réponse visible et JSON-LD). Ne plus écrire « 10 h » ni « une dizaine
  d'heures ». **La fiche produit de la centrale PA501Z annonce encore 10 h** —
  elle est hors périmètre de cette page et reste à aligner côté produit.
- **Sirène intégrée : 85 dB**, valeur reprise de l'ancienne FAQ de la page.
  Non confirmée par la fiche produit — à valider.
- **Nombre d'accessoires : 200** d'après la fiche de la centrale. Les descriptions
  des deux packs « Offre exclusive » annoncent « jusqu'à 100 accessoires
  supplémentaires ». La page retient 200.
- **Le pack PA570 Zenguard de l'ancienne page n'existe plus** : le produit est
  archivé. Les trois packs affichés sont des produits actifs — le troisième est
  le **Pack Tranquillité+ (PA574) à 739,90 €**, mis en avant à la demande du
  client à la place du pack « double caméra » à 809,90 €. Ce produit n'a **pas de
  prix barré** en base : la carte n'affiche donc ni prix de référence ni badge de
  remise.
- **Remise configurateur de 25 %** : reprise de la page Touch, le configurateur
  étant le même outil. À confirmer si elle diffère pour l'Élite.
- **GSM 4G+ — comportement exact** (corrigé par le client) : en cas de coupure
  Wi-Fi la centrale bascule sur les données mobiles, **ce que ne font ni la
  Vigilia ni la Touch**, et **l'application reste active**. On continue donc
  d'armer et de désarmer à distance, et on reçoit des SMS d'alerte. On ne pilote
  **pas** l'alarme par SMS — l'application suffit. Ne pas écrire « 4G » seul :
  toujours **4G+**. La mention « appel téléphonique » a été retirée de la page
  (elle figure encore sur la fiche produit) — à trancher.
- **Périmètre du Zigbee** (corrigé par le client) : seules **trois références**
  communiquent en Zigbee — **WDS502Z, WVD502Z, WKE502Z**. Tous les autres
  accessoires passent par la **fréquence radio 433 ou 868 MHz**. L'**amplificateur
  EXT501 n'étend donc la portée que de ces trois références**.
- **Accessoires tiers** : Zigbee 3.0 et Tuya, **compatibilité non garantie**.
  Toujours accompagner la mention de cet avertissement.
- **Ne pas écrire que la PA501Z reprend les accessoires de la gamme Key (SA501)**
  ni proposer de remplacer une ancienne centrale SA501 en gardant ses détecteurs.
  Cette affirmation a été retirée de toute la page (Zigbee, accessoires, fiche
  technique, FAQ et JSON-LD).
- **Ne pas écrire qu'un détecteur qui ne répond plus est signalé.** La liaison
  bidirectionnelle Zigbee est bien chiffrée et confirmée, mais la supervision
  d'un accessoire muet n'est pas une fonction à annoncer.
- **Caméras et coupure Internet** : le flux vidéo n'est pas accessible sans
  Internet, **même avec une carte SIM insérée dans la centrale**. Le relais 4G+
  ne sert qu'à la centrale et à l'application, jamais à la vidéo.
- **Le bouton SOS est celui de la télécommande WRC501** (appui 3 secondes), pas
  une touche du boîtier de la centrale — celle-ci n'a ni écran ni clavier.
- **Manuel** : lien direct vers le PDF
  `Manuel_Complet_PA501Z_12_12_23_compressed.pdf` hébergé sur le CDN Shopify.
  Le « guide d'installation pas à pas » a été retiré.
- **La section témoignage parle du système Touch XL** — c'est le contenu existant,
  repris tel quel. À adapter si vous voulez un témoignage Élite.
- **Disponibilité du support** : assistant en ligne 7j/7, équipe 5j/7. Ne jamais
  écrire que l'équipe est joignable au téléphone 7j/7.

## Modifier la page

```bash
python3 theme-src/build-collection-elite.py
```

Le script écrit `sections/el-*.liquid` et
`templates/collection.collection-elite-2.json` à partir de
`theme-src/collection-elite/*.liquid` et de `theme-src/collection-elite.base.json`.

## Aperçu

Thème non publié **« Page ÉLITE PA501Z - refonte (Claude) »** (id `202210017620`),
dupliqué depuis le thème de la refonte Touch — il contient donc **les deux pages** :

<https://daewoo-security.fr/collections/systeme-dalarme-pa501z?preview_theme_id=202210017620>

Le thème publié n'est pas modifié.
