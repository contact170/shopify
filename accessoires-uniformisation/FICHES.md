# Fiches accessoires passées au modèle premium

Thème d'aperçu : « Fiche accessoire uniformisee v1 (Claude) » — `202527113556`

| Réf. | Produit | Template | Titre de page |
|---|---|---|---|
| WDV301 | Contacteur d'ouverture / vibration 2-en-1 | `accessoires-sans-details` | Deux détections. Un seul capteur. |
| WVD301 | Détecteur de vibration | `accessoires` | Le choc suffit. |
| WDG301 | Contacteur de porte de garage | `accessoires` | Le garage aussi est une porte d'entrée. |
| WPS305 | Détecteur de mouvement animaux | `accessoires` | Il voit l'intrus, pas le chat. |
| WMO301 | Détecteur de mouvement extérieur | `accessoires` | La détection commence avant la porte. |
| WSD301 | Détecteur de fumée connecté | `accessoires` | 85 dB dans la maison. Une alerte dans votre poche. |
| BIR301 | Barrières infrarouge | `accessoires-sans-details` | Franchir le faisceau suffit. |
| WWF301 | Détecteur de fuite d'eau | `accessoires` | Les premières gouttes suffisent. |
| WOS305S | Sirène extérieure solaire | `accessoires-sans-details` | 110 dB, alimentés par le soleil. |
| WOS305 | Sirène extérieure | `accessoires-sans-details` | 110 dB, et un cri si on la décroche. |
| SPWOS305 | Panneau solaire pour WOS305 | `cam-spw502` | La WOS305, sans jamais la rebrancher. |
| WIS305 | Sirène intérieure 100 dB | `accessoires` | Impossible de savoir d'où ça vient. |
| SOS301 | Bracelet SOS d'urgence | `accessoires` | Un seul appui. Même alarme éteinte. |

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
