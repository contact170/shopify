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
| SPWOS305 | Panneau solaire pour WOS305 | `acc-premium-sd` | La WOS305, sans jamais la rebrancher. |
| WIS305 | Sirène intérieure 100 dB | `acc-premium` | Impossible de savoir d'où ça vient. |
| SOS301 | Bracelet SOS d'urgence | `acc-premium` | Un seul appui. Même alarme éteinte. |
| WKE301 | Clavier sans fil + 2 badges | `acc-premium` | Sans sortir le téléphone. |
| WRF301 | Pack de 2 badges RFID | `acc-premium-sd` | Pas de code à retenir. |
| WRC305 | Télécommande à clapet | `acc-premium-sd` | Dans la poche, sans appui accidentel. |
| EXT301 | Amplificateur de signal | `acc-premium` | Quand la centrale n'entend plus l'accessoire. |
| AM302S | Centrale Touch XL seule | `centrale-seule-touchxl` | Sept pouces. Tout se lit d'un coup d'œil. |
| AM301S | Centrale Touch seule | `centrale-seule-touch` | Le cœur du système, vendu seul. |

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

## WRC305 : 868 MHz corrigé en 433 MHz

Erreur confirmée par le client : les centrales Touch et Vigilia ne gèrent pas
le 868 MHz. La valeur figurait à deux endroits, tous deux corrigés :

- fiche **WRC305** : métachamps `connectivite`, `securite_detection`,
  `note_compatibilite`, bandeau de caractéristiques et description ;
- fiche **« Configurateur | Télécommande WRC301 »** (WRC301C), où le même
  « RF868 MHz » traînait dans `connectivite`.

Balayage effectué sur les 29 produits de la collection « Compatible gamme
Vigilia / Touch » (métachamps `connectivite`, `securite_detection`,
`evolutivite_compatibilite`) : **aucune autre occurrence de 868 MHz**. Le reste
de la gamme annonce bien 433 MHz, ou 433,92 MHz pour le WVD301.

La portée annoncée, **20 m**, est également faible pour une télécommande —
cohérente avec un porte-clés, mais à confirmer.

Créé au passage : la fiche n'avait **aucune FAQ**, contrairement aux autres
accessoires. Sept questions rédigées, dont l'incompatibilité avec les gammes
Key et Élite, qui n'apparaissait que dans une ligne rouge en bas de la
description d'origine.

Type de produit corrigé : il valait « Pour armer/désarmer votre alarme », ce qui
aurait donné le titre « Daewoo Pour armer/désarmer votre alarme WRC305 ».

## Mentions de Vigilia encore manquantes

Repéré pendant le balayage, non corrigé faute de certitude :

- **WDS301** (contacteur de porte) : `connectivite` annonce « les centrales
  Daewoo TOUCH (AM301 / AM302) », sans Vigilia — alors que le produit est dans
  la collection Vigilia / Touch.
- **WOS301** (sirène filaire) : « Compatible uniquement avec les centrales TOUCH
  et TOUCH XL ». S'agissant d'une sirène filaire, la restriction est peut-être
  réelle. À confirmer avant de modifier.

À noter aussi : un produit **« Détecteur de fumée WSD301 — GRATUIT »**
(WSD301CGRATUIT) coexiste avec le WSD301 standard, avec ses propres textes.

## EXT301 : gabarit dédié absent, comme cam-spw502

`templates/product.ext301.json` **n'existe sur aucun thème**, alors que le
produit porte le suffixe `ext301`. La fiche retombe donc sur le gabarit produit
par défaut en production. Deuxième cas après `cam-spw502` : les deux méritent
d'être corrigés côté thème en ligne.

Le gabarit a été créé sur le thème v2 avec la mise en page premium. Le suffixe
du produit n'a pas été modifié : la page en production reste exactement ce
qu'elle est aujourd'hui.

## EXT301 : corrections de contenu

- **Nom du produit** : la description, les balises SEO et le métaobjet
  « À quoi ça sert » appelaient le produit **« AM30X »** — qui est le nom de la
  famille de centrales, pas la référence de l'amplificateur. Remplacé par
  EXT301 partout.
- **Vigilia absent** : la description disait « exclusivement compatible avec
  TOUCH (AM301) et TOUCH XL (AM302) », alors que le métachamp `connectivite`,
  le titre, la collection et l'un des visuels annoncent Vigilia. La description
  était l'unique source discordante ; Vigilia rétabli.
- **Type de produit vide** : renseigné en « Amplificateur de signal », sans quoi
  le h1 se serait réduit à « Daewoo EXT301 ».
- **Aucune FAQ** n'existait. Huit questions rédigées, centrées sur le placement
  à mi-distance — l'erreur d'installation qui rend le produit inutile.
- La liste des accessoires relayés, reprise du fabricant, cite la
  **télécommande WRC301**, désormais en brouillon. Mention rendue générique dans
  la description ; la liste d'origine subsiste dans `note_compatibilite`, à
  actualiser si le fabricant confirme la prise en charge des références 305.

Le contenu de la boîte annonçait le générique « Accessoire / Adhésive de
fixation / Manuel ». Remplacé par l'amplificateur, le câble USB vers micro-USB
de 90 cm et le manuel — **aucune source ne mentionne de kit de fixation**, il
n'a donc pas été inventé alors que la fiche évoque une pose murale.

## Les deux centrales vendues seules

Premières fiches qui ne sont pas des accessoires. Le modèle s'y applique
pourtant sans réserve : l'acheteur d'une centrale seule sait déjà ce qu'il
veut — il remplace, il équipe un second site, ou il monte son installation
pièce par pièce. Il s'agit de l'aiguiller, pas de le convaincre.

`conseil_quantite`, sous le prix, sert ici d'avertissement d'achat :
**la centrale est vendue seule, sans détecteur ni sirène**, et un pack revient
moins cher pour une première installation. C'est l'information qui évite une
commande décevante et un retour.

L'écart entre les deux modèles est traité frontalement, dans les deux sens :
écran de 4,3 vs 7 pouces, et 90 vs 200 accessoires. La capacité de 200 ne sert
à rien dans un appartement ; la fiche le dit.

### AM301S : gabarit dédié créé

`pack-touch-2` est utilisé par **16 produits** : packs Touch et Touch XL, offres
Black Friday et Noël, packs AM340 à AM343 et AM350 à AM353, offres exclusives.
Y appliquer la mise en page premium aurait contaminé toutes ces fiches — la
même erreur qu'au départ avec `product.accessoires.json`.

Résolu : le client a créé `product.centrale-seule-touch.json` sur le thème en
ligne, copie conforme de `pack-touch-2` (**même empreinte MD5**, `30e5bc94…`).
L'AM301S a été basculée sur ce suffixe, et le gabarit premium installé sous ce
nom sur le thème v2. Les 16 produits de `pack-touch-2` ne bougent pas.

Pour l'AM302S, `centrale-seule-touchxl` n'était utilisé que par elle : rien à
créer côté thème en ligne.

### Balises SEO absentes

Les deux centrales avaient une **balise titre nulle**. L'AM302S n'avait ni titre
ni méta-description — une fiche à 219,90 € invisible en recherche. Les deux sont
désormais renseignées, et les titres produit reformulés pour porter la mention
« seule », qui est le point de confusion de ces deux pages.

Aucune n'avait de FAQ : huit questions rédigées pour chacune, centrées sur les
deux questions qui décident — ce qu'il y a dans la boîte, et 4,3 ou 7 pouces.

## Centrales : contenu de la boîte et catégorie

**Contenu de la boîte, confirmé pour les deux** : centrale, câble USB,
adaptateur secteur, kit de fixation murale et visserie. Renseigné dans
`contenu_du_pack` et dans la description. L'AM302S annonçait auparavant la
seule centrale, ce qui sous-vendait le produit.

**Catégorie : décision de ne rien changer.** Les deux centrales restent taguées
« Accessoires » et rangées dans « Tous les accessoires ». C'est délibéré : elles
ne sont pas destinées à être vendues seules à un nouveau client, mais à dépanner
quelqu'un dont la centrale est en panne. Leur place est donc bien dans la
logique accessoire.

Corollaire à conserver : elles restent dans la liste d'exclusions du bandeau
« Complétez votre système » (`acc-complements`, réglage `exclusions`). Sans
cela, une fiche détecteur à 30 € proposerait une centrale à 119,90 € ou
219,90 € comme complément, ce qui n'a pas de sens pour un client qui possède
déjà la sienne.

## Réglages typographiques et image principale

Trois demandes traitées d'un coup sur les fichiers partagés — donc sur les
**19 fiches** à la fois.

**La police n'était pas la même selon l'appareil.** C'était un vrai défaut, pas
une impression. Les tokens définissaient :

    --accp-sans: -apple-system, BlinkMacSystemFont, "SF Pro Display",
                 "SF Pro Text", "Inter Tight", "Segoe UI", Roboto, sans-serif

Sur Mac et iPhone, `-apple-system` l'emportait et la page s'affichait en
**San Francisco**. Sur Windows et Android, ces polices n'existent pas et le
navigateur retombait sur **Inter Tight**, chargée depuis Google Fonts. Deux
typographies distinctes pour un même design.

Corrigé en plaçant `"Inter Tight"` en tête : tout le monde voit la même chose,
les polices système ne servant plus que de secours si Google Fonts ne répond
pas.

Second foyer d'incohérence : le bloc description est rendu dans un conteneur
`.rte`, la classe de texte enrichi du thème, qui impose sa propre police. La
section `acc-description` la neutralise désormais explicitement.

Restent en police du thème, et c'est normal : les widgets Judge.me, Alma et
Moast, qui ne sont pas sous notre contrôle.

**Image principale** : `max-width` de la galerie portée de 340 à 430 px,
vignettes de 54 à 60 px.

**Textes** : environ +1 px sur les tailles courantes — corps de description
16 → 17 px, réponses de FAQ 16 → 17 px, lignes de fiche technique 15 → 16 px,
contenu de la boîte 15 → 16 px, conseil de quantité 14 → 15 px, prix 21 → 23 px,
bouton 17 → 18 px, chapô jusqu'à 22 px. Interlignes ajustés en conséquence.

Les cinq fichiers ont été vérifiés par empreinte MD5 après envoi : le thème est
identique au miroir du dépôt.

## Second cran

Toujours un peu juste au premier passage. Deuxième palier appliqué :

**Image** : galerie 430 → **540 px**, vignettes 60 → **72 px**, avec plus d'air
entre elles. Depuis le point de départ, la photo principale a gagné 59 %.

**Textes**, +1 px de plus sur l'ensemble : description 17 → 18 px, réponses de
FAQ 17 → 18, fiche technique 16 → 17, contenu de la boîte 16 → 17, conseil de
quantité 15 → 16, chapô jusqu'à 24 px, prix 23 → 25, bouton 18 → 19, titres de
FAQ 18 → 19. Le sélecteur de quantité passe de 38 à 42 px de haut pour rester
proportionné au bouton d'achat, et les rembourrages suivent — un texte plus
gros dans un contenant inchangé finit par étouffer.

Cinq fichiers, vérifiés par empreinte MD5 après envoi.

## État final et mise en ligne

**Thème à publier : « Fiche accessoire uniformisee v2 (Claude) » — `202545004884`.**

### Vérifications faites avant publication

**Le thème n'a pas divergé.** Onze fichiers de référence comparés entre le thème
en ligne et le duplicata — `config/settings_data.json`, `settings_schema.json`,
`layout/theme.liquid`, `snippets/product-card.liquid`, les trois groupes de
sections (en-tête, pied, superposition) et les gabarits `index`, `product`,
`collection`, `cart` : **empreintes MD5 identiques**. Rien n'a été touché sur le
thème en ligne depuis la duplication, publier ne perdra donc aucun réglage.

**Les 15 fichiers `acc-*`** du thème correspondent au caractère près au miroir
de ce dépôt.

**Les 19 fiches** n'utilisent plus que quatre gabarits — `acc-premium`,
`acc-premium-sd`, `centrale-seule-touch`, `centrale-seule-touchxl` — tous
identiques entre eux (`b1e96322…`) et tous présents sur le thème en ligne avec
leur contenu classique.

### Un débordement évité de justesse

Les gabarits `cam-spw502` et `ext301` avaient reçu la mise en page premium pour
servir le SPWOS305 et l'EXT301. Or ils sont partagés avec **quatre autres
produits** : le panneau solaire de caméra SPW502 et trois fiches
« Configurateur ». Publier en l'état leur aurait imposé une page premium vide,
alors qu'elles s'affichent aujourd'hui avec le gabarit produit par défaut.

Corrigé : les deux gabarits sont redevenus des copies conformes de
`templates/product.json` (même empreinte, `891590bd…`), et le SPWOS305 et
l'EXT301 ont été bascules sur `acc-premium-sd` et `acc-premium`. Les quatre
produits tiers retrouvent exactement leur comportement actuel.

### Ce que la publication corrige au passage

`templates/product.ext301.json` et `templates/product.cam-spw502.json`
n'existent pas sur le thème en ligne : le SPWOS305, l'EXT301, le SPW502 et les
fiches configurateur associées retombent aujourd'hui sur le gabarit par défaut.
Après publication, les fichiers existent et ces pages cessent de dépendre d'un
repli.

### Reste à traiter dans la gamme Touch / Vigilia

Produits **actifs** non encore passés au modèle :

- **SIM1MOIS** et **DASIM1AN** — les deux cartes SIM (gabarits `carte-sim` et
  `carte-sim-1-an`, communs à d'autres gammes).
- **DAADAWOS301S** — adaptateur secteur pour sirène WOS301S. À noter : la
  **WOS301S elle-même est archivée**, cet accessoire n'a donc plus de produit
  principal actif.

Sans objet car archivés ou en brouillon : WDS301, WOS301, WOS301S, WPS301
(archivés), WRC301, SIM1VIG, WSD301CGRATUIT (brouillons). Les alertes
précédentes sur les mentions de Vigilia manquantes du WDS301 et du WOS301
tombent donc d'elles-mêmes.

## AM302 : 90 accessoires, pas 200

Erreur corrigée sur toute la fiche : la Touch XL accepte **90 accessoires**,
comme l'AM301. La valeur figurait à sept endroits — bandeau de caractéristiques,
`note_compatibilite`, `securite_detection`, deux réponses de FAQ, la description
et la méta-description.

Elle avait surtout servi d'argument de vente : le titre de page annonçait
« Sept pouces. Deux cents accessoires. » et une section entière de la
description était bâtie dessus. Tout a été repris.

L'angle change en conséquence : **la seule différence entre l'AM301 et l'AM302
est la taille de l'écran**, 4,3 contre 7 pouces. La fiche le dit maintenant
franchement, et précise que si l'on pilote tout depuis l'application, l'AM301
suffit. Un client qui découvre après coup que les deux centrales font la même
chose se sent floué ; autant l'annoncer et le laisser choisir sur le confort
d'usage.

Corrigé aussi côté AM301 : sa FAQ comparait « 90 accessoires contre 200 ».

## Présentation uniformisée sur le style du site

La FAQ des fiches accessoires reprend désormais la présentation de celle du
site : bande bleutée très claire, en-tête centré avec surtitre bleu, questions
en cartes blanches à coins arrondis et ombre douce, chevron bleu à droite.

Le même traitement a été étendu aux **accordéons de la fiche technique**, qui
partagent la classe `.accp-faq` : sans cela, deux blocs dépliants voisins
auraient eu deux allures différentes sur la même page.

Palette alignée sur celle du site, dans la famille bleu nuit :

| Rôle | Avant | Après |
|---|---|---|
| Texte fort et titres | `#14161a` (quasi noir) | `#101f47` (bleu nuit) |
| Texte courant | `#6e7480` (gris neutre) | `#5b6480` (gris bleuté) |
| Bandes claires | `#f2f3f5` (gris) | `#eef2fd` (bleuté) |
| Bande sombre | `#0b0d10` | `#0a1230` |
| Filets | `#e2e4e8` | `#e3e8f5` |

Autres alignements :

- **Surtitres** : passaient en police mono, gris, minuscules espacées. Ils
  reprennent le traitement du site — sans-serif, bleu, gras, capitales. La mono
  ne sert plus que pour les repères numérotés (01, 02, 03), où elle reste un
  détail de composition et non un style concurrent.
- **En-têtes de bloc centrés** sur l'ensemble des sections, comme l'en-tête de
  la FAQ et celui de la page. Le corps de texte reste aligné à gauche.
- **Même carte pour tous les blocs** : rayon de 16 px et ombre commune sur la
  fiche technique, le contenu de la boîte, les accordéons et le conseil de
  quantité. Le tableau technique était jusque-là posé à nu sur la bande.
- **Sélecteur de quantité** en blanc bordé plutôt qu'en gris : le gris neutre
  devenait terne sur la nouvelle bande bleutée.
