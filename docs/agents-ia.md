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
| Optimisation du site | `optimisation-site.md` + `scripts/audit-site.js` | En test sur données réelles (29/10/2026) |

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
  Optimisation du site, Veille concurrence, Rédacteur SEO), `Date`,
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
