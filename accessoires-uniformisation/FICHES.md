# Fiches accessoires passées au modèle premium

Thème d'aperçu : « Fiche accessoire uniformisee v2 (Claude) » — `202545004884`
(le v1, `202527113556`, est obsolète — voir « Gabarits dédiés » plus bas)

| Réf. | Produit | Template | Titre de page |
|---|---|---|---|
| WDV301 | Contacteur d'ouverture / vibration 2-en-1 | `acc-premium-sd` | Deux détections. Un seul capteur. |
| WVD301 | Détecteur de vibration | `acc-premium` | Le choc suffit. |
| WDG301 | Contacteur de porte de garage | `acc-premium` | Le garage aussi est une porte d'entrée. |
| WPS305 | Détecteur de mouvement animaux | `acc-premium` | Il voit l'intrus, pas le chat. |
| WMO301 | Détecteur de mouvement extérieur | `acc-premium` | La détection commence avant la porte. |
| WSD301 | Détecteur de fumée connecté | `acc-premium` | 85 dB dans la maison. Une alerte dans votre poche. |
| BIR301 | Barrières infrarouge | `acc-premium-sd` | Franchir le faisceau suffit. |
| WWF301 | Détecteur de fuite d'eau | `acc-premium` | Les premières gouttes suffisent. |
| WOS305S | Sirène extérieure solaire | `acc-premium-sd` | 110 dB, alimentés par le soleil. |
| WOS305 | Sirène extérieure | `acc-premium-sd` | 110 dB, et un cri si on la décroche. |
| SPWOS305 | Panneau solaire pour WOS305 | `acc-premium` (cam-spw502) | La WOS305, sans jamais la rebrancher. |
| WIS305 | Sirène intérieure 100 dB | `acc-premium` | Impossible de savoir d'où ça vient. |
| SOS301 | Bracelet SOS d'urgence | `acc-premium` | Un seul appui. Même alarme éteinte. |
| WKE301 | Clavier sans fil + 2 badges | `acc-premium` | Sans sortir le téléphone. |
| WRF301 | Pack de 2 badges RFID | `acc-premium-sd` | Pas de code à retenir. |
| WRC305 | Télécommande à clapet | `acc-premium-sd` | Dans la poche, sans appui accidentel. |

Pour chaque fiche : type de produit Shopify, `titre_page`, `accroche`,
`conseil_quantite`, `note_compatibilite`, métaobjet `bandeau_caracteristiques`,
textes alternatifs des visuels, balises SEO et description longue.

## Points de vigilance relevés

- Les descriptions annonçaient souvent « Compatible TOUCH / TOUCH XL » sans
  mentionner Vigilia, alors que ces accessoires le sont. Corrigé au fil des fiches.
- Pile du WDG301 : CR2032 (le métachamp indiquait CR2450).
- `contenu_du_pack` valait « Accessoire / Adhésive de fixation / Manuel » sur
  toute la gamme. Remplacé par le contenu réel, fiche par fiche.

## WMO301 — avertissement d'exposition au soleil

Le capteur ne doit jamais être orienté face aux rayons du soleil : la variation
brutale de chaleur sur la lentille est interprétée comme un mouvement et provoque
de fausses détections. L'avertissement figure à trois endroits de la fiche —
description (« Où l'installer »), volet « Sécurité et détection », et ligne
« Pose » de la fiche technique.

La consigne ne concerne que les détecteurs d'extérieur : le WPS305 est un
modèle d'intérieur. Reste à vérifier sur le WMO501.

## WSD301 — données complétées

Le métachamp « Alimentation / Autonomie » contenait un argument commercial
(« Sécurité permanente… ») au lieu des données attendues. Complété depuis :

- alimentation : 1 pile CR123A longue autonomie (durée volontairement non chiffrée) ;
- certification : EN 14604 ;
- pose : visserie et kit de fixation inclus.

La pile CR123A est fournie avec le produit. Restent à confirmer : les dimensions.

## BIR301 — balise titre absente

Le produit n'avait aucune balise titre SEO (`seo.title` vide) : Google reprenait
le titre brut du produit. Une balise a été rédigée.

Ses caractéristiques (portée de 10 m, IP66, dimensions 33 x 3,5 cm, 4 piles
ER15505H 3,6 V incluses, autonomie de 2 ans, anti-démontage) étaient présentes
dans les métachamps mais peu visibles sur la page ; elles remontent dans la
fiche technique.

Piles fournies, comme celle du WSD301 : indiqué dans le contenu de la boîte.

## Bandeau « Complétez votre système »

Les recommandations automatiques de Shopify piochaient dans tout le catalogue et
remontaient des centrales d'alarme. Elles sont remplacées par
`sections/acc-complements.liquid`, qui affiche les autres produits de la
collection **« Compatible … »** à laquelle appartient le produit courant — donc
toujours la même gamme. Sans collection de ce type, la section reste masquée
plutôt que d'afficher une gamme étrangère.

La section écarte aussi les doublons « Configurateur | … » et accepte une liste
de handles à exclure.

### Donnée à corriger

Les centrales **Touch AM301** (`centrale-touch-am301-avec-ecran-tactile-4-3`) et
**Touch XL AM302** (`centrale-am302`) portent le métachamp
`custom.categorie_de_produit` = « Accessoires ». Elles entrent donc dans la
collection « Compatible gamme Vigilia / Touch », qui sert de source au bandeau.
Elles sont écartées par la liste d'exclusions, mais la vraie correction est de
changer leur catégorie — à valider, car cela les retirerait aussi de la page de
cette collection.

## WWF301 — éléments manquants

- **FAQ produit** : elle n'existait pas. Un métaobjet `faq_produit` a été rédigé
  à partir des données du produit (7 questions). À relire avant publication :
  le contenu est déduit des métachamps, il n'a pas été validé par le SAV.
- **Lien vers le manuel** : `custom.manuel_produit` est vide, la ligne de
  téléchargement ne s'affiche donc pas. La section Installation ne montre le lien
  que si le métachamp est renseigné — aucune correction nécessaire.

Le titre du produit annonçait « Compatible Touch (AM301/AM302) » sans Vigilia,
alors que la description et le métachamp de compatibilité l'incluent. Aligné sur
la convention de la gamme : « | Compatible Touch/Vigilia (AM30x) ». L'URL du
produit est inchangée.

## Manuels non fournis en version papier

Le guide d'installation du **BIR301** n'est pas livré dans la boîte. Le contenu
de la boîte et la description l'indiquent explicitement et renvoient vers le PDF
téléchargeable depuis la page. À vérifier sur les autres références : le contenu
de la boîte annonce « 1 manuel d'utilisation » sur toutes, ce qui vient du texte
générique d'origine.

## Vente croisée : l'option associée

Nouveau métachamp `custom.option_associee` (référence produit) et section
`sections/acc-option.liquid` : une carte compacte sous la zone d'achat, avec
visuel, nom, prix et un bouton qui ajoute directement le produit au panier.
Masquée si le métachamp est vide ou le produit indisponible.

Premier usage : la sirène **WOS305** propose le panneau solaire **SPWOS305**.

## SPWOS305 — template

Le panneau utilise le template `cam-spw502`, partagé avec les panneaux solaires
de caméras (SPW502, SPW502P2, SPW502P3). Une version premium de ce template a
été créée sur le brouillon ; les autres panneaux en héritent et afficheront
moins de sections tant que leurs métachamps ne sont pas renseignés.

## Longueur du câble du panneau solaire

Les sources divergeaient : 280 cm côté WOS305S, « environ 2 mètres » côté
SPWOS305. Valeur retenue partout : **environ 2 m**.

## Carrousel vidéo Moast

Le bloc d'application Moast était présent dans les anciens templates, à
l'intérieur de la zone d'achat. Il est rétabli sur les trois templates premium,
sous forme de section `apps` placée juste après la zone d'achat, en pleine
largeur — les vidéos verticales y respirent mieux que dans une colonne étroite.

Le bloc reste en mode dynamique : Moast sert les vidéos correspondant au produit
depuis son propre service, rien n'est stocké côté Shopify.

## WIS305 — description d'origine polluée

La description du produit contenait le balisage HTML complet d'une interface de
chat (div imbriquées, classes utilitaires, attributs `aria-*`) collé tel quel.
Une centaine de balises pour une dizaine de paragraphes utiles : lourd à charger
et illisible pour les moteurs. Réécrite en HTML propre (`<p>`, `<h2>`, `<ul>`),
avec la compatibilité Touch / Vigilia qui manquait entièrement et un lien
interne vers la sirène extérieure WOS305.

À vérifier : d'autres fiches du catalogue peuvent avoir la même pollution.

## WIS305 — contenu de la boîte

Confirmé par le client : sirène, kit de fixation murale, câble USB Type-C,
adaptateur secteur et manuel d'utilisation. Le fait que le câble et la prise
soient fournis est repris dans la description, car c'est une question d'achat
récurrente sur un produit alimenté en USB.

Réponse de FAQ nettoyée au passage : elle contenait une note de rédaction entre
parenthèses (« La durée d'autonomie sur batterie seule n'est pas précisée dans
la fiche. »), visible côté client.

## SOS301 — pile et étanchéité

**Pile : réglé.** Alcaline 27A 12 V, fournie — vendue partout sous les
références A27 ou MN27. Remplaçable par le client, sans outil. C'est un argument
et non un détail technique : pas de batterie propriétaire, pas de socle de
recharge à penser à utiliser, rien à renvoyer en atelier. Traité comme tel dans
la description, la fiche technique, la FAQ et le contenu de la boîte.

**Étanchéité : toujours inconnue.** Rien n'est affirmé sur la page tant que
l'information n'est pas disponible. C'est pourtant le point le plus important
qui reste ouvert sur cette fiche : la salle de bain est le lieu de chute le plus
fréquent, et un bracelet qu'on retire pour se doucher n'est pas porté au moment
où il servirait. Dès que la donnée arrive, elle mérite d'être mise en avant
dans le bandeau de caractéristiques.

## Descriptions polluées par du balisage colle

Deux motifs distincts repérés dans le catalogue, tous deux issus de
copier-coller depuis une interface de chat :

- **WIS305, SOS301** : balisage complet d'interface (`<div>` imbriquées,
  classes `font-claude-response-body`, attributs `aria-*`). Lourd et illisible
  pour les moteurs. Corrigé sur ces deux fiches.
- **WRC501 et probablement d'autres** : attributs `data-start` / `data-end` sur
  chaque balise. Moins grave — la structure `h2`/`h3`/`p` reste correcte — mais
  c'est du bruit inutile dans le HTML.

Le filtre `body:*...*` de l'API de recherche produits ne fonctionne pas : il
renvoie tout le catalogue sans filtrer (vérifié avec un motif témoin
inexistant). Un balayage fiable demande de parcourir les descriptions une à une
ou via une opération en masse. Non fait à ce stade.

## Gabarits dédiés : pourquoi le thème v1 a été abandonné

Le premier thème d'aperçu réécrivait directement `product.accessoires.json` et
`product.accessoires-sans-details.json`. Or ces deux gabarits ne sont pas
réservés à la gamme Touch/Vigilia : **plus de 50 produits** les portent, dont
toute la gamme Key, toute la gamme Élite, les caméras, les cartes SIM, les
autocollants et des packs d'alarme complets. Tous héritaient donc du design
premium, en version appauvrie faute de métachamps.

Le `templateSuffix` étant une propriété du **produit** et non du thème, on ne
pouvait pas simplement créer un suffixe dédié : le thème en ligne, dépourvu du
fichier, serait retombé sur le gabarit produit par défaut et aurait cassé les
pages en production.

Architecture retenue :

1. Sur le thème **en ligne**, deux copies conformes des gabarits actuels :
   `product.acc-premium.json` (copie de `accessoires`) et
   `product.acc-premium-sd.json` (copie de `accessoires-sans-details`).
   Vérifiées identiques à la source au caractère près.
2. Le thème en ligne est **dupliqué** en « Fiche accessoire uniformisee v2 ».
3. Sur ce duplicata, les deux gabarits `acc-premium*` reçoivent la mise en page
   premium, et les 14 fichiers `acc-*` sont réinstallés.
4. Les 13 fiches traitées passent sur le suffixe correspondant à leur ancien
   gabarit, pour que la page en production reste rigoureusement identique.

Résultat : en production rien ne change, et sur l'aperçu seules les fiches
traitées adoptent le nouveau design. Le reste du catalogue s'y affiche
exactement comme sur le site.

## cam-spw502 : gabarit absent du thème en ligne

`templates/product.cam-spw502.json` n'existe pas sur le thème publié, alors que
le panneau SPWOS305 et le panneau SPW502 réclament ce suffixe. Ces deux fiches
retombent donc aujourd'hui sur le gabarit produit par défaut en production.
Anomalie préexistante, à corriger séparément.

En attendant, le gabarit a été créé sur le thème v2 avec la mise en page
premium, pour que le SPWOS305 garde sa fiche. Conséquence : le SPW502, panneau
solaire de caméra hors gamme Touch/Vigilia, hérite lui aussi du design premium
sur l'aperçu. C'est le seul produit dans ce cas.

## WRF301 : le lecteur RFID n'est pas sur toutes les centrales

Point découvert dans la FAQ existante du produit, et absent de tous les
métachamps : **la centrale Vigilia intègre un lecteur RFID**, les centrales
Touch AM301 et Touch XL AM302 non. Sur Touch, le badge est donc inutilisable
sans le clavier WKE301.

C'est une information décisive à l'achat — un client Touch qui commande des
badges seuls reçoit un produit qu'il ne peut pas utiliser. Elle est désormais
en tête de la description, dans la note de compatibilité et dans le bandeau de
caractéristiques.

Corollaire côté WKE301 : le clavier est l'accessoire qui *ouvre* l'usage des
badges sur Touch. Argument de vente ajouté à sa fiche, avec le WRF301 en
option associée sous la zone d'achat.

## WRF301 : doublon supprimé

La fiche `daewoo-pack-de-2-badges-rfid-wrf301` a été supprimée par le client.
Vérifié : elle n'existe plus, et une redirection 301 est en place.

Réserve : cette redirection pointe vers la collection
`compatible-gamme-vigilia-touch`, pas vers la fiche qui remplace réellement le
produit. Rediriger vers `/products/pack-de-2-badges-rfid-wrf301` transmettrait
le signal SEO à la page équivalente plutôt qu'à une page de liste.

## WKE301 : dimensions contradictoires

- Description d'origine : **140 × 90 × 20 mm**
- Métachamp `evolutivite_compatibilite` : **180 × 96 × 27 mm**

Aucune source ne permet de trancher. La dimension a donc été retirée du bandeau
de caractéristiques plutôt que d'afficher une valeur au hasard. À mesurer sur
un exemplaire.

Corrigé au passage : le métaobjet « À quoi ça sert » du WKE301 annonçait
« jusqu'à 1 an d'autonomie sur piles », alors que le clavier fonctionne sur
batterie rechargeable avec 1 à 2 mois d'autonomie. Ce texte s'affiche dans la
bande sombre de la fiche.

## WRC301 : mise en brouillon

Vérifié : la fiche est bien en brouillon, stock à zéro, et la redirection
`/products/telecommande-wrc301` → `/products/telecommande-compatible-vigilia-touch`
existe déjà. Un visiteur arrivant sur l'ancienne URL atterrit sur la WRC305,
qui la remplace. C'est exactement ce qu'il fallait.

Reste actif en revanche : **« Configurateur | Télécommande WRC301 »**
(SKU WRC301C), stock à zéro, dans la collection « Accessoires configurateurs ».
Tant qu'il est actif, la référence abandonnée reste proposée dans le parcours du
configurateur. À passer en brouillon également, ou à remplacer par la WRC305.

## WRC305 : 868 MHz, à confirmer

Le métachamp `connectivite` annonçait une liaison **868 MHz**, alors que les
autres accessoires de la même gamme communiquent en **433 MHz** (WKE301, WIS305,
SOS301, tous compatibles avec les mêmes centrales). La valeur d'origine a été
reprise telle quelle, mais l'écart mérite vérification : si c'est une erreur,
elle est reprise dans le bandeau de caractéristiques et la FAQ.

La portée annoncée, **20 m**, est également faible pour une télécommande —
cohérente avec un porte-clés, mais à confirmer.

Créé au passage : la fiche n'avait **aucune FAQ**, contrairement aux autres
accessoires. Sept questions rédigées, dont l'incompatibilité avec les gammes
Key et Élite, qui n'apparaissait que dans une ligne rouge en bas de la
description d'origine.

Type de produit corrigé : il valait « Pour armer/désarmer votre alarme », ce qui
aurait donné le titre « Daewoo Pour armer/désarmer votre alarme WRC305 ».
