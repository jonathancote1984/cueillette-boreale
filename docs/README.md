# Wiki — Cueillette Boréale

> Documentation du dépôt [cueillette-boreale](../README.md) · app en ligne :
> <https://jonathancote1984.github.io/cueillette-boreale/>

Ce dossier est le wiki du projet : une page par sujet, en français du Québec, avec des liens
relatifs qui fonctionnent aussi bien sur GitHub que dans un éditeur local.

Cueillette Boréale est un **fork boréal** de l'app de cueillette champignons « Memphis » :
l'app est réorientée vers les **8 plantes et baies boréales du Québec, toutes comestibles
(dont 4 avec prudence)**. Les champignons sont **retirés du fork** : aucune fiche de
champignon n'y subsiste. La source de vérité du contenu est
[especes-boreales.md](especes-boreales.md) et son jumeau `especes-boreales.json`.

## Par où commencer

| Si vous voulez… | Lisez |
|---|---|
| installer l'app sur un téléphone | [Installation](installation.md) |
| savoir ce que l'app fait, écran par écran | [Fonctionnalités](fonctionnalites.md) |
| identifier une plante ou une baie correctement | [Guide d'identification](guide-identification.md) |
| voir la liste des espèces et leurs statuts | [Espèces boréales](especes-boreales.md) |
| comprendre les règles de sécurité | [Sécurité alimentaire](securite-alimentaire.md) |
| savoir où vont vos données | [Données et confidentialité](donnees-confidentialite.md) |
| respecter l'identité visuelle | [Design](design.md) puis [DESIGN.md](../DESIGN.md) |
| publier une mise à jour | [Déploiement](deploiement.md) |
| modifier le code | [Contribution](contribution.md) |
| retracer l'évolution du projet | [Journal des versions](changelog.md) |
| citer les photos correctement | [Licences et crédits](licences-credits.md) |

## Pages du wiki

- **[Installation](installation.md)** — hébergement GitHub Pages, ajout à l'écran d'accueil,
  serveur local, mise à jour du cache `cqb-vN`, dépannage.
- **[Fonctionnalités](fonctionnalites.md)** — spots, identification, cueillettes, stats,
  sauvegarde, paramètres.
- **[Guide d'identification](guide-identification.md)** — les 8 espèces documentées, la
  checklist terrain à 5 critères (feuille, fruit, tige, odeur, habitat), l'identification
  par photo et ses limites.
- **[Espèces boréales](especes-boreales.md)** — la liste des 8 espèces, leurs statuts et
  leurs confusions dangereuses ; source de vérité du contenu.
- **[Sécurité alimentaire](securite-alimentaire.md)** — badges de statut, règle « plus grave
  gagne », centre antipoison, confusions ail des bois/muguet et thé du Labrador/laurier des
  marais, primauté du guide sur l'IA.
- **[Données et confidentialité](donnees-confidentialite.md)** — IndexedDB `cqb_bd` v5, clés
  Gemini/OpenRouter locales, ré-encodage des photos, export/import JSON version 5.
- **[Design](design.md)** — palette vert sapin (ivoire `#EFF3EC`, primaire `#1E4D33`,
  mousse `#5E8C4A`, cuivre `#B5651D`, danger `#A32633`), style carnet de terrain, tokens,
  composants clés.
- **[Déploiement](deploiement.md)** — publication par branche, option GitHub Actions, bump du
  cache du service worker, vérifications après déploiement.
- **[Licences et crédits](licences-credits.md)** — origine et attribution des photos.
- **[Contribution](contribution.md)** — conventions de code et de commit, checklist avant
  livraison, documents à tenir à jour.
- **[Journal des versions](changelog.md)** — itérations héritées du projet d'origine et
  entrées du fork boréal.

## Documents de référence hors wiki

Ces fichiers restent la source de vérité de leur domaine ; le wiki les résume et y renvoie.

| Document | Contenu |
|---|---|
| [../DESIGN.md](../DESIGN.md) | Système de design complet : tokens, couleurs nommées, composants, règles do/don't. |
| [../PRODUCT.md](../PRODUCT.md) | Vérité produit : usagers, contexte d'usage, capacités, contraintes, principes. |
| [especes-boreales.json](especes-boreales.json) | Jumeau machine des 8 fiches de plantes (schéma documenté dans especes-boreales.md). |
| [AUDIT_RAPPORT.md](AUDIT_RAPPORT.md) | Audit webapp consolidé (sécurité, qualité, performance) avec plan de correction. |
| [AUDIT_SECU.md](AUDIT_SECU.md) | Constats de sécurité détaillés. |
| [AUDIT_QUALITE.md](AUDIT_QUALITE.md) | Constats de qualité de code. |
| [AUDIT_PERF.md](AUDIT_PERF.md) | Constats performance, PWA et UX. |
| [archive/](archive/) | Rapports de revue de design et d'exécution des passes de critique (historique, avant le fork). |

## Conventions du wiki

- Une page = un sujet ; en-tête identique (titre, fil d'Ariane, sommaire si la page est
  longue).
- Liens **relatifs** seulement (`installation.md`, `../DESIGN.md`) — jamais d'URL absolue
  vers GitHub pour un fichier du dépôt.
- Le numéro de cache du service worker n'est **jamais** recopié dans la documentation : il
  vit dans `sw.js` (`const CACHE = 'cqb-vN'`) et nulle part ailleurs.
- Ton factuel, français du Québec, pas de promesse commerciale.
- Les messages de sécurité (« en cas de doute, on ne mange pas », centre antipoison
  1-800-463-5060) sont repris mot pour mot, sans reformulation atténuante.
