# Agents IA Daewoo Security : note de reprise

Cette note permet à une nouvelle session Claude de reprendre le système
d'agents IA sans contexte préalable. Elle décrit l'existant, les règles à
respecter et la tâche en cours : basculer le rédacteur SEO vers GSC Wizard.

## Vue d'ensemble

### Agents (fiches dans `.claude/agents/`)

| Agent | Fiche | État |
|---|---|---|
| Analyste ventes | `analyste-ventes.md` | Actif, testé, fusionné dans `main` |
| Rédacteur SEO (blog) | `redacteur-seo.md` | En attente : bascule de Windsor vers GSC Wizard, non testé, pas encore dans `main` |

### Tableau de bord Notion (privé)

- Page « 🤖 Centre des agents Daewoo » :
  https://app.notion.com/p/40883a31dd678196a7ebed4cedbc057f
  Sections : 📬 Rapports à lire (vue filtrée Statut = À lire), 🤖 Mes agents,
  🗂️ Historique des rapports.
- Base « 🔒 Résultats des agents » : data source
  `collection://7911a038-548e-452c-ad97-e12aa51b0349`.
  Propriétés : `Rapport` (titre), `Agent` (Analyste ventes, Veille stock,
  Audit fiches produits, Veille concurrence, Rédacteur SEO), `Date`,
  `Priorité` (Haute, Normale, Basse), `Statut` (À lire, À traiter, Fait),
  `Résumé`.
- Base « Agents » : data source
  `collection://bcaaf2ff-48d8-4334-8599-6d734584e81d`.
  Propriétés : `Agent` (titre), `État` (Actif, En attente, En pause, Proposé),
  `Mission`, `Planning`, `Accès autorisés`, `Notification`,
  `Fiche technique`. Ligne « Rédacteur SEO (blog) » : page
  `40883a31dd678125a908e9e046bf4fb1`.

### Notifications

À la fin de chaque exécution planifiée, la session envoie une notification
avec l'outil `PushNotification` (application Claude sur le téléphone du
dirigeant). Notion ne peut pas notifier : les agents y écrivent sous le nom
du dirigeant, et Notion ne notifie pas ses propres actions.

### Tâches planifiées

Elles sont rattachées à la session d'origine
`session_01LiMrJG4zhCAQ3781eUKv2r` (« Agents et tableau de bord ») :

| Nom | ID | Planning (Europe/Paris) | État |
|---|---|---|---|
| Rapport ventes hebdo | `trig_0168PGipkh2FwEwHAbrbgbVH` | lundi 6h41 | actif |
| Article SEO hebdo | `trig_012dv29VRoSUDy4swhx2yeYv` | mercredi 6h44 | désactivé jusqu'à la bascule |

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
- **Blog :** l'ancien outil Sorank (en pause, bientôt désactivé) produisait
  des articles en doublon et hors sujet. Le rédacteur SEO donne la priorité à
  la vérification des doublons et à la pertinence. Il ne publie rien : il
  propose dans Notion.
- **Processus :** tester un agent sur des données réelles avant de fusionner
  sa fiche dans `main`. Le dirigeant valide les fusions.

## Reprise : basculer le rédacteur SEO vers GSC Wizard

Prérequis : le connecteur GSC Wizard (`https://mcp.gscwizard.com/mcp`) est
ajouté sur claude.ai, et une **nouvelle** session est ouverte, car les
connecteurs ne sont chargés qu'au démarrage d'une session.

1. **Récupérer le travail :**
   `git fetch origin claude/beautiful-rubin-p673kt`, puis fusionner cette
   branche dans la branche de travail de la session.
2. **Tester GSC Wizard :**
   - charger ses outils (ToolSearch avec « gsc » ou « wizard ») et les lister ;
   - vérifier qu'ils sont en lecture seule ;
   - interroger daewoo-security.fr sur 28 jours, par requête et par page :
     clics, impressions, CTR, position.
3. **Mettre à jour `.claude/agents/redacteur-seo.md` :**
   - dans `tools:`, remplacer les outils Windsor par les outils de lecture
     GSC Wizard ;
   - réécrire l'« Étape 1 » avec l'appel testé ;
   - adapter les règles de sécurité 3 et la ligne « sources » du livrable.
4. **Tester l'agent sur données réelles.** Utiliser le sous-agent
   `redacteur-seo`, ou un agent `general-purpose` avec la fiche si le type
   n'est pas encore chargé. Vérifier la page Notion produite :
   - pas de doublon ;
   - sujet pertinent ;
   - liens produits valides ;
   - images issues du CDN Shopify ;
   - HTML correct.
5. **Fusionner :** ouvrir une pull request vers `main` (fiches + cette note)
   et la fusionner après validation du dirigeant.
6. **Déplacer les tâches planifiées :**
   - recréer les deux tâches dans la nouvelle session avec les consignes
     ci-dessous (`CRON_TZ=Europe/Paris 41 6 * * 1` et
     `CRON_TZ=Europe/Paris 44 6 * * 3`) ;
   - supprimer ensuite les deux anciennes (`delete_trigger` sur les deux
     ID ci-dessus).
7. **Mettre à jour Notion :** dans la ligne « Rédacteur SEO (blog) », passer
   `État` à « Actif » et mettre à jour `Planning`, `Accès autorisés` (GSC
   Wizard) et `Fiche technique` (lien vers `main`).

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
