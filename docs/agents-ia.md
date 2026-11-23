# Agents IA Daewoo Security : note de reprise

Cette note permet à une nouvelle session Claude de reprendre le système
d'agents IA sans contexte préalable. Elle décrit l'existant et les règles à
respecter. Dernières évolutions dans « Historique ».

## Vue d'ensemble

### Agents (fiches dans `.claude/agents/`)

| Agent | Fiche | État |
|---|---|---|
| Analyste ventes | `analyste-ventes.md` | Actif, testé, fusionné dans `main` |
| Rédacteur SEO (blog) | `redacteur-seo.md` | Actif, testé sur données réelles le 29/10/2026 (GSC Wizard) |
| Optimisation du site | `optimisation-site.md` + `scripts/audit-site.js` | Actif, testé sur données réelles le 29/10/2026 |
| Community manager Instagram | `community-manager-instagram.md` + `scripts/instagram-reel.py` | Testé sur données réelles le 23/11/2026 (page « Posts Instagram – semaine 48 »), tâche active ; fiche sur la branche `claude/jolly-keller-dcap4c`, pas encore dans `main` |

L'agent « Optimisation du site » remplace l'agent proposé « Audit fiches
produits / SEO » (fusion décidée par le dirigeant le 29/10/2026).

### Tableau de bord Notion (privé)

- Page « 🤖 Centre des agents Daewoo » :
  https://app.notion.com/p/40883a31dd678196a7ebed4cedbc057f
  Sections : 📬 Rapports à lire (vue filtrée Statut = À lire), 🤖 Mes agents,
  🗂️ Historique des rapports.
- Base « 🔒 Résultats des agents » : data source
  `collection://7911a038-548e-452c-ad97-e12aa51b0349`.
  Propriétés : `Rapport` (titre), `Agent` (Analyste ventes, Veille stock,
  Optimisation du site, Veille concurrence, Rédacteur SEO, Community
  manager Instagram), `Date`,
  `Priorité` (Haute, Normale, Basse), `Statut` (À lire, À traiter, Fait),
  `Résumé`.
- Base « Agents » : data source
  `collection://bcaaf2ff-48d8-4334-8599-6d734584e81d`.
  Propriétés : `Agent` (titre), `État` (Actif, En attente, En pause, Proposé),
  `Mission`, `Planning`, `Accès autorisés`, `Notification`,
  `Fiche technique`. Lignes : « Rédacteur SEO (blog) », page
  `40883a31dd678125a908e9e046bf4fb1` ; « Optimisation du site », page
  `40883a31dd6781ba9ba4dcf80cccc6fe`.

### Connecteur GSC Wizard (Search Console)

- Connecteur claude.ai `https://mcp.gscwizard.com/mcp`, dont les outils
  s'appellent `mcp__GSC__*`. Compte `contact@be-connected.com`, plan
  starter. Une seule propriété : `https://daewoo-security.fr/`.
- Le plugin `seo-gsc-wizard` (serveur `plugin:seo-gsc-wizard:gsc-wizard`)
  échoue au démarrage (erreur proxy 403). Il n'est pas nécessaire : le
  connecteur `GSC` suffit.
- **Le connecteur n'est pas entièrement en lecture seule.** L'accès Google
  Search Console l'est (`webmasters.readonly`), mais la clé GSC Wizard est en
  écriture et certains outils modifient des réglages ou consomment des
  quotas (sites, IndexNow, annotations, URL suivies, inspections…). Chaque
  agent n'a donc accès qu'à des outils de lecture : `score_opportunities` et
  `query_search_analytics` pour le rédacteur SEO, `audit_onpage_seo` et
  `query_top_pages` pour l'optimisation du site.
- `get_core_web_vitals` (vitesse mesurée chez les vrais visiteurs) renvoie
  `notConfigured` : il faut enregistrer une clé d'API Chrome UX Report dans
  l'application GSC Wizard (propriété › Core Web Vitals › « API Key »).
  L'API PageSpeed Insights sans clé répond 429. L'agent d'optimisation
  mesure donc la vitesse lui-même avec `scripts/audit-site.js`.
- Différences avec Windsor : le CTR est un pourcentage de 0 à 100, la
  période par défaut est les 28 derniers jours consolidés (2 à 3 jours de
  retard), et les adresses `/fr-ch/`, `/fr-com/`… sont des variantes de
  pays d'une même page.

### Instagram (compte `@daewoosecurity`)

- **Connecteur Windsor.ai** (`mcp__Windsor_ai__*`), connecteur `instagram`,
  compte `17841433847232059`, formule gratuite. La lecture et la
  publication fonctionnent ; `force_refresh` est refusé (les données ont
  plusieurs heures de retard). Les actions d'écriture ont été activées par
  le dirigeant le 23/11/2026 (Windsor › Settings › API Access).
- **Supermetrics** voit aussi le compte, mais son essai a expiré le
  10/07/2026 : la publication y est refusée. Ne pas l'utiliser pour écrire.
- **Qui publie.** L'agent `community-manager-instagram` ne fait que lire et
  proposer dans Notion. La publication est faite par Claude dans la
  conversation Instagram, avec `execute_action`, uniquement quand le
  dirigeant l'écrit lui-même (« publie le post 1 »), en reprenant le bloc
  « Paramètres de publication » de la page Notion. Même règle pour répondre
  à un commentaire, le masquer ou le supprimer.
- **Si `execute_action` ne répond pas dans le délai**, ne pas relancer
  aussitôt : lire d'abord `media_count` (sans `force_refresh`) pour vérifier
  que rien n'a été publié, sinon le post part en double.
- **Images.** Instagram n'accepte que le JPEG. Les visuels du CDN Shopify
  (souvent en WebP) se convertissent en ajoutant `&width=1080&format=pjpg`
  à l'URL. Rapport largeur/hauteur entre 0,8 et 1,91.
- **Vidéos (reels).** `scripts/instagram-reel.py` monte un reel vertical à
  partir d'un plan JSON et de visuels produits. Deux leçons du premier reel
  (W512MW, publié le 23/11/2026) y sont intégrées :
  - *zone sûre* : Instagram affiche le nom du compte et la ligne audio en
    haut, la légende et les boutons en bas ; tout texte reste entre 270 px
    et 1 500 px de hauteur (sur 1 920). Un bandeau placé à 130 px s'est
    retrouvé sous le nom du compte ;
  - *piste son* : une piste AAC quasi vide (2 kbit/s) a fait échouer le
    traitement côté Instagram (`container status: ERROR`) ; la sortie porte
    désormais une piste AAC 48 kHz à 128 kbit/s.
  Une publication par l'API ne peut pas utiliser la bibliothèque musicale
  d'Instagram.
- **Hébergement des vidéos.** Instagram va chercher la vidéo à une adresse
  publique. L'envoi d'un fichier vers Shopify depuis une session Claude est
  bloqué par le contrôle de sécurité : c'est le dirigeant qui dépose le
  fichier dans Shopify › Contenu › Fichiers et donne le lien. Les images
  n'ont pas ce problème (elles sont déjà sur le CDN).
- **Constats sur le compte au 23/11/2026** : 497 abonnés, 22 publications,
  aucune entre le 24/06 et le 23/11/2026. Les reels touchent bien plus de
  comptes que les carrousels et images (60 à 180), surtout les vidéos
  filmées (déballage Touch XL : 2 190 comptes). À faire trancher par le
  dirigeant : « 60 000 foyers » en Europe (bio) ou en France (un post).

### Notifications

À la fin de chaque exécution planifiée, la session envoie une notification
avec l'outil `PushNotification` (application Claude sur le téléphone du
dirigeant). Notion ne peut pas notifier : les agents y écrivent sous le nom
du dirigeant, et Notion ne notifie pas ses propres actions.

### Tâches planifiées

Elles sont rattachées à la session
`session_01LiMrJGgZbi75nzwpQWg7uB` (« Agents et tableau de bord »), qui
possède les connecteurs Shopify, Notion et GSC Wizard. L'ancienne session
`session_01LiMrJG4zhCAQ3781eUKv2r` (renommée « … (ancienne, sans GSC
Wizard) ») n'a plus de tâche.

| Nom | ID | Planning (Europe/Paris) | État |
|---|---|---|---|
| Rapport ventes hebdo | `trig_0135d9x7u61HvZ5HS9uD9fyU` | lundi 6h41 | actif |
| Article SEO hebdo | `trig_01SwJUzM3793Tso6WRRn6Wbv` | mercredi 6h44 | actif |
| Audit du site hebdo | `trig_01Qs6W29kZhAavyhtwjPZxdG` | vendredi 6h47 | actif à partir du 6/11/2026 (mis en pause pour sauter le 30/10, réactivation automatique le 30/10 à 7h30) |
| Posts Instagram hebdo | `trig_01THxGEY9FyymZkavU7NhQ5E` | lundi 6h52 | actif, **rattachée à la conversation Instagram** `session_01LiMrJH5CsBEPZPJ4EaHaPc` (c'est là que le dirigeant valide et que Claude publie) |

Le paramètre `connectors` de `create_trigger` n'est pas disponible pour
cette organisation. Une tâche lancée dans une nouvelle session à chaque fois
n'aurait donc ni Shopify, ni Notion, ni la recherche Google. Il faut
**rattacher la tâche à une session qui possède ces connecteurs** (mode par
défaut de `create_trigger`, sans `create_new_session_on_fire`).

## Règles à respecter

- **Sécurité :**
  - les agents sont en lecture seule sur la boutique ;
  - aucune donnée client (nom, e-mail, adresse) ne figure dans les rapports ;
  - les agents écrivent dans Notion uniquement dans la base « Résultats » ;
  - le Centre des agents reste privé et n'est jamais partagé avec les
    intégrations Notion « chatbase » ni « Franck – Base de connaissances
    Daewoo ».
- **Ventes :** chaque montant porte la mention HT ou TTC. Le rapport commence
  par le total des ventes TTC (le chiffre affiché par Shopify), suivi des
  ventes nettes HT.
- **Optimisation du site :** seul agent à disposer de Bash, pour lancer
  `node scripts/audit-site.js` (Playwright, pages publiques de
  daewoo-security.fr uniquement : le script refuse les autres domaines) et
  `curl` en lecture sur le site et le CDN Shopify. Sa fiche lui interdit
  `git` et toute écriture hors de son dossier de travail. Il ne modifie rien
  sur la boutique : le dirigeant demande à Claude d'appliquer les
  corrections numérotées qu'il retient.
- **Blog :** l'ancien outil Sorank (en pause, bientôt désactivé) produisait
  des articles en doublon et hors sujet. Le rédacteur SEO donne la priorité à
  la vérification des doublons et à la pertinence. Il ne publie rien : il
  propose dans Notion.
- **Processus :** tester un agent sur des données réelles avant de fusionner
  sa fiche dans `main`. Le dirigeant valide les fusions.

## Reprendre dans une nouvelle session

Les connecteurs ne sont chargés qu'au démarrage d'une session. Si un
connecteur est ajouté ou si la session « Agents et tableau de bord »
disparaît :

1. ouvrir une nouvelle session sur ce dépôt et vérifier que les outils
   `mcp__Shopify__*`, `mcp__Notion__*` et `mcp__GSC__*` sont disponibles ;
2. recréer les tâches dans cette session avec les consignes ci-dessous
   (`CRON_TZ=Europe/Paris 41 6 * * 1`, `CRON_TZ=Europe/Paris 44 6 * * 3` et
   `CRON_TZ=Europe/Paris 47 6 * * 5`, mode par défaut de `create_trigger`) ;
3. supprimer ensuite les anciennes (`delete_trigger`) et mettre à jour la
   section « Tâches planifiées » de cette note.

## Historique

### Bascule du rédacteur SEO vers GSC Wizard (29/10/2026)

- Outils GSC Wizard testés sur daewoo-security.fr (28 jours : 4 785 clics,
  148 102 impressions). `analyze_cannibalization` a été écarté : il est
  dominé par les requêtes de marque, ne filtre ni la marque ni le blog, et sa
  réponse est trop volumineuse pour un sous-agent sans accès aux fichiers.
- Fiche réécrite : outils, Étape 1 (trois appels testés), règle de sécurité
  3, ligne « sources », plus les retours du premier test (articles masqués
  avec `isPublished`, vérification des redirections avec `urlRedirects`,
  produits « Configurateur | » écartés, consignes clarifiées).
- Premier test réel : « Interrupteur pour volet roulant connecté : comment
  bien le choisir ? » (groupe de requêtes : 1 393 impressions, 2 clics).
  Vérifié : pas de doublon, liens produits et images du CDN Shopify en
  ligne, faits conformes à la fiche produit IVR501W, HTML correct.
- Tâches planifiées déplacées dans la session « Agents et tableau de bord »,
  anciennes tâches supprimées.

### Création de l'agent « Optimisation du site » (29/10/2026)

- Choix du dirigeant : vitesse, images et textes alternatifs, contrôle
  visuel, SEO technique ; lecture seule (il propose, Claude applique sur
  demande) ; chaque vendredi ; fusion avec l'agent proposé « Audit fiches
  produits / SEO » (option Notion renommée « Optimisation du site »).
- `scripts/audit-site.js` écrit et testé : environ 1 minute par page en 4G
  lente simulée. Le préchargement du paiement Shopify (environ 900 Ko par
  page, basse priorité) est compté à part pour ne pas fausser les poids.
- Premier test réel (17 min 30) : rapport « Optimisation du site – semaine
  44 », priorité Haute, 2 problèmes Fort (collection Caméras à 6,8 s,
  fiche Montre SW101 à 4,2 s et 3,1 Mo à cause de 4 vidéos), 10 Moyen,
  13 Faible, 15 corrections numérotées. Vérifiés à la main : longueurs des
  titres proposés, vidéos de la SW101, logo invisible sur l'en-tête
  transparent des articles.
- Retours du test intégrés : produits par lots de 15 (au-delà, la réponse
  est trop volumineuse), script en deux lots de 4 pages (limite de 10 min
  de Bash), services tiers bloqués par l'environnement de mesure à ne pas
  signaler comme erreurs, rangs numérotés à partir de 0, 3 images au plus
  par fiche, comptage des caractères avec `node -e`.

## Consignes des tâches planifiées

### Rapport ventes hebdo (lundi 6h41)

> Exécution hebdomadaire planifiée du rapport de ventes Daewoo Security
> (demandée par le dirigeant).
>
> 1. À partir de la date du jour, calcule la semaine précédente complète, du
>    lundi au dimanche (fuseau Europe/Paris), son numéro de semaine ISO,
>    ainsi que les dates de la semaine d'avant (pour la comparaison).
> 2. Lance le sous-agent `analyste-ventes` avec l'outil Agent
>    (subagent_type « analyste-ventes »), en lui donnant la date du jour et
>    les dates exactes des deux semaines. C'est lui qui interroge Shopify et
>    dépose le rapport dans la base Notion privée « 🔒 Résultats des agents »
>    (page « Centre des agents Daewoo »).
> 3. Ne fais rien d'autre que les étapes 1, 2 et 5 : n'utilise pas toi-même
>    les outils Shopify ou Notion, ne modifie aucun fichier, ne crée ni
>    commit, ni branche, ni pull request.
> 4. Si le sous-agent `analyste-ventes` n'est pas disponible ou échoue, ne
>    fais pas l'analyse à sa place (ses restrictions d'accès sont volontaires
>    pour protéger les données).
> 5. Préviens le dirigeant avec l'outil PushNotification (charge-le avec
>    ToolSearch « select:PushNotification » si besoin ; status « proactive »).
>    Message d'une ligne, moins de 200 caractères, sans markdown. Exemple en
>    cas de succès : « 📊 Rapport ventes S44 prêt : 32 186 € TTC (+3 %). À
>    lire dans Notion › Centre des agents. » En cas d'échec : « ⚠️ Rapport
>    ventes S44 non produit : voir la conversation Agents et tableau de
>    bord. »
> 6. Termine par une réponse courte en français : lien de la page Notion
>    créée, priorité choisie et résumé en une phrase (total des ventes TTC,
>    puis ventes nettes HT), ou l'explication du problème.

### Article SEO hebdo (mercredi 6h44)

> Exécution hebdomadaire planifiée : proposition d'article de blog SEO pour
> Daewoo Security (demandée par le dirigeant).
>
> 1. Lance le sous-agent `redacteur-seo` avec l'outil Agent (subagent_type
>    « redacteur-seo »), en lui donnant la date du jour. Il analyse la Google
>    Search Console (via GSC Wizard), vérifie les doublons et la pertinence,
>    puis dépose sa proposition dans la base Notion privée « 🔒 Résultats des
>    agents » (page « Centre des agents Daewoo »). Si le type d'agent
>    « redacteur-seo » n'est pas disponible, lis
>    `.claude/agents/redacteur-seo.md` et lance un agent general-purpose avec
>    exactement ces consignes, en lui imposant de n'utiliser que les outils
>    listés dans l'en-tête de la fiche.
> 2. Ne fais rien d'autre que les étapes 1 et 3 : n'utilise pas toi-même GSC
>    Wizard, Shopify ou Notion, ne modifie aucun fichier, ne crée ni commit,
>    ni branche, ni pull request, et ne publie rien sur la boutique.
> 3. Préviens le dirigeant avec l'outil PushNotification (charge-le avec
>    ToolSearch « select:PushNotification » si besoin ; status
>    « proactive »). Message d'une ligne, moins de 200 caractères, sans
>    markdown. Succès : « ✍️ Article SEO prêt : <titre court> (<mot-clé>,
>    <impressions> impressions). À relire dans Notion › Centre des agents. »
>    Échec : « ⚠️ Article SEO non produit : <raison courte>. Voir la
>    conversation Agents et tableau de bord. »
> 4. Termine par une réponse courte en français : lien de la page Notion,
>    titre de l'article, mot-clé principal et produits mis en avant, ou
>    l'explication du problème.

### Audit du site hebdo (vendredi 6h47)

> Exécution hebdomadaire planifiée : audit graphique et technique du site
> daewoo-security.fr (demandée par le dirigeant).
>
> 1. Lance le sous-agent `optimisation-site` avec l'outil Agent
>    (subagent_type « optimisation-site »), en lui donnant la date du jour, le
>    numéro de semaine ISO, le chemin du dépôt et un dossier de travail dans
>    ton scratchpad (`audit-site-<AAAA-MM-JJ>`). Il mesure les pages clés,
>    regarde les captures, vérifie les images, les textes alternatifs et le
>    SEO technique, puis dépose son rapport dans la base Notion privée « 🔒
>    Résultats des agents » (page « Centre des agents Daewoo »). Si le type
>    d'agent « optimisation-site » n'est pas disponible, lis
>    `.claude/agents/optimisation-site.md` et lance un agent general-purpose
>    avec exactement ces consignes, en lui imposant de n'utiliser que les
>    outils listés dans l'en-tête de la fiche.
> 2. Ne fais rien d'autre que les étapes 1 et 3 : n'utilise pas toi-même
>    Shopify, GSC Wizard ou Notion, ne modifie aucun fichier, ne crée ni
>    commit, ni branche, ni pull request, et ne modifie rien sur la boutique.
> 3. Préviens le dirigeant avec l'outil PushNotification (charge-le avec
>    ToolSearch « select:PushNotification » si besoin ; status
>    « proactive »). Message d'une ligne, moins de 200 caractères, sans
>    markdown. Succès : « 🎨 Audit du site S44 prêt : <n> corrections
>    proposées, priorité <priorité>. À lire dans Notion › Centre des agents. »
>    Échec : « ⚠️ Audit du site non produit : <raison courte>. Voir la
>    conversation Agents et tableau de bord. »
> 4. Termine par une réponse courte en français : lien de la page Notion,
>    priorité, nombre de problèmes par impact et les 3 premières corrections,
>    ou l'explication du problème.
