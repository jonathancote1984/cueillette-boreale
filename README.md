# Cueillette Boréale

[![App en ligne sur GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-en%20ligne-5E8C4A?style=flat-square&labelColor=1E4D33)](https://jonathancote1984.github.io/cueillette-boreale/)
[![PWA hors-ligne](https://img.shields.io/badge/PWA-100%20%25%20hors--ligne-5E8C4A?style=flat-square&labelColor=1E4D33)](docs/installation.md)
[![Sans build](https://img.shields.io/badge/build-aucun%20%C2%B7%20statique-B5651D?style=flat-square&labelColor=1E4D33)](docs/deploiement.md)

**App en ligne : <https://jonathancote1984.github.io/cueillette-boreale/>**

Carnet de cueillette de **plantes et baies boréales du Québec** et guide d'identification, livré
comme application web installable (PWA) qui fonctionne à 100 % hors-ligne, en forêt, sans réseau.
Pas de compte, pas de serveur applicatif : les données restent sur l'appareil.

## Sommaire

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Design](#design)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Sécurité](#sécurité)
- [Licence et droits des photos](#licence-et-droits-des-photos)
- [Structure du dépôt](#structure-du-dépôt)
- [Documentation (wiki)](#documentation-wiki)

## Présentation

L'app est un carnet de chasse personnel : elle sert à retrouver ses coins secrets (GPS),
journaliser ses récoltes (poids, météo, photo), consulter un guide de **8 plantes comestibles du
Québec** (dont 4 à récolter avec prudence) et vérifier une identification sur le terrain à l'aide
d'une liste de critères à cocher. Aucun champignon : le guide porte exclusivement sur la flore
boréale — plantes aromatiques, théiers et petits fruits.

Caractéristiques techniques principales :

- PWA statique **mono-fichier** : toute l'app tient dans `index.html` (≈ 190 Ko), sans
  framework et sans étape de compilation.
- Service worker `sw.js` en stratégie *cache-first* : l'app, les icônes, la police et les
  photos embarquées sont disponibles hors-ligne dès la première visite.
- Données locales seulement : IndexedDB `cqb_bd` (version 5) avec repli `localStorage`.
- Fonctions d'IA **facultatives** (Google Gemini ou OpenRouter), activées uniquement si
  l'utilisateur colle sa propre clé API dans les paramètres.

## Fonctionnalités

| Onglet | Ce qu'il fait |
|---|---|
| **Spots** | Coins de cueillette : nom, description, GPS avec précision affichée, photo, espèces attendues, lien Google Maps, partage (Web Share API avec repli presse-papiers). |
| **Identifier** | Guide de 8 plantes comestibles du Québec (saison, habitat, description, caractéristiques, confusions avec des espèces toxiques ressemblantes), recherche, filtres comestibilité et saison, fiches à checklist terrain, identification par photo (IA), variétés personnelles. |
| **Cueillettes** | Journal : date, espèce (suggestions ou saisie libre), poids en kg ou lb, spot lié, météo, note, photo. |
| **Stats** | Total récolté, nombre de sorties, espèces distinctes, dernière sortie, tops espèces et spots, barres mensuelles. Contient aussi l'export/import et l'effacement complet. |
| **Paramètres** | Unités kg/lb, fournisseur d'IA (Gemini ou OpenRouter) et clé API, ordre de priorité des sources d'images, crédits photos, rappel de la méthode d'identification. |

Détail complet : [docs/fonctionnalites.md](docs/fonctionnalites.md).

## Design

Style assumé « carnet de forêt » sur une **palette vert sapin** — la forêt boréale en tout temps.

| Rôle | Nom | Code |
|---|---|---|
| Accent principal | Sapin | `#1E4D33` |
| Signal | Pruche | `#4C7A55` |
| Énergie (FAB, accents) | Terracotta | `#B5651D` |
| Confiance (comestible) | Mousse | `#5E8C4A` |
| Action secondaire | Vert forêt | `#3A5C42` |
| Fond | Crème sapin | `#EFF3EC` |
| Surfaces | Blanc | `#F8FBF6` |
| Trait et texte | Noir | `#0F2418` |
| Danger absolu | Rouge | `#A32633` |

Règles structurantes : bordure noire de 3 px sur toute surface colorée, ombres dures sans
flou (décalage 3 à 6 px), un coin cassé par carte, titres inclinés de -1 à -2°, typographie
Fredoka auto-hébergée (`fonts/fredoka.woff2`), rouge réservé au danger et à la destruction.

Le système de design complet (tokens, composants, do/don't) est dans
[DESIGN.md](DESIGN.md) ; la synthèse orientée wiki est dans [docs/design.md](docs/design.md).

## Installation

### Héberger sur GitHub Pages

1. Pousser le dépôt sur GitHub (branche `main`).
2. *Settings → Pages → Build and deployment* : source **Deploy from a branch**, branche
   `main`, dossier `/ (root)`.
3. L'app est servie à `https://<utilisateur>.github.io/<dépôt>/` — ici
   <https://jonathancote1984.github.io/cueillette-boreale/>.

Aucun réglage supplémentaire : tous les chemins de l'app sont relatifs (`./index.html`,
`./img/...`), donc le sous-dossier de Pages fonctionne tel quel.

### Ajouter à l'écran d'accueil

Ouvrir l'adresse dans Chrome (Android) ou Safari (iOS), puis
**menu → « Ajouter à l'écran d'accueil »**. L'app s'ouvre ensuite en plein écran
(`display: standalone`), en orientation portrait, et fonctionne sans réseau.

### Servir en local

```bash
python3 -m http.server 8091     # puis http://localhost:8091
# ou
npx serve -l 8091
```

Le service worker exige `https://` ou `localhost` : `file://` ne fonctionne pas.

Procédure détaillée, mise à jour du cache `cqb-vN` et dépannage :
[docs/installation.md](docs/installation.md).

## Utilisation

1. **Noter un spot** : onglet Spots → bouton flottant 📍 → nom, GPS (bouton de
   localisation), photo, espèces attendues.
2. **Identifier** : onglet Identifier → chercher ou filtrer une espèce → ouvrir la fiche →
   cocher les critères (feuille, fruit, tige, odeur, habitat) devant la plante réelle. Le
   verdict n'est jamais confiant avant que tous les critères concordent, et reste prudent
   sur les espèces à usage encadré.
3. **Identifier par photo** (facultatif, requiert une clé Gemini ou OpenRouter) : bouton
   d'identification photo → appareil ou galerie → l'IA propose une espèce avec un niveau de
   confiance. Le guide a toujours le dernier mot sur le statut de comestibilité.
4. **Journaliser** : onglet Cueillettes → date, espèce, poids, spot, météo, note, photo.
5. **Sauvegarder** : onglet Stats → *Exporter* (fichier JSON complet) ; *Importer* remplace
   toutes les données après confirmation chiffrée.

Guide d'utilisation de l'identification : [docs/guide-identification.md](docs/guide-identification.md).

## Sécurité

L'app est un outil d'aide à la décision, **pas** un avis botanique. Elle ne remplace ni un
expert ni un cours d'identification.

- **En cas de doute, on ne mange pas.**
- **Centre antipoison du Québec : 1-800-463-5060** (affiché dans l'app avec chaque alerte et
  à chaque verdict incertain).
- Statuts possibles : comestible, prudence, immangeable, toxique, et `inconnu` quand
  l'information est incertaine — le doute penche toujours du côté prudent. Le guide ne
  documente que des espèces comestibles ; **4 d'elles exigent de la prudence** (cuisson
  obligatoire, espèce vulnérable ou usage réservé aux cueilleurs expérimentés) :
  l'ail des bois, le thé du Labrador, le poivre des dunes et le myrique baumier.
- Les fiches listent les **confusions possibles avec des espèces toxiques ressemblantes** et
  comment les distinguer.

Voir [docs/securite-alimentaire.md](docs/securite-alimentaire.md) pour les règles complètes
et [docs/donnees-confidentialite.md](docs/donnees-confidentialite.md) pour la sécurité des
données (clé API, photos, import/export).

## Licence et droits des photos

- **Code** : projet personnel, aucune licence explicite n'est déclarée dans le dépôt. Sans
  fichier `LICENSE`, tous droits réservés par défaut — ajouter une licence si le code doit
  être réutilisé.
- **Photos** : les 8 photos d'espèces (`img/especes/`) et les 22 photos de spécificités
  (`img/specs/`) proviennent de **Wikimedia Commons**, sous licences libres (CC0, CC BY,
  CC BY-SA). Auteur, licence et page source sont conservés dans
  `img/especes/credits.json` et `img/specs/credits.json`, et affichés dans l'app
  (Paramètres → Crédits photos).

Détail et état des crédits : [docs/licences-credits.md](docs/licences-credits.md).

## Structure du dépôt

| Chemin | Rôle |
|---|---|
| `index.html` | L'application complète (HTML, CSS, JS — aucune dépendance externe). |
| `sw.js` | Service worker hors-ligne ; **incrémenter `cqb-vN` à chaque mise à jour**. |
| `manifest.json` | Manifeste PWA (nom, icônes, `theme_color` vert sapin `#1E4D33`, portrait, standalone). |
| `fonts/fredoka.woff2` | Police auto-hébergée (aucun appel à Google Fonts). |
| `icons/` | Icônes PWA 192/512 et maskable (3 bleuets). |
| `generer_icones.py` | Régénère les icônes (Pillow). |
| `img/especes/` | 8 photos d'espèces + `credits.json`. |
| `img/specs/` | 22 photos de spécificités (8 espèces × 2-3 critères) + `credits.json`. |
| `scripts/telecharger_photos.py` | Re-télécharge les photos depuis Wikimedia Commons. |
| `DESIGN.md` | Système de design complet (source de vérité visuelle). |
| `PRODUCT.md` | Vérité produit : usagers, contexte, contraintes, principes. |
| `docs/` | Wiki de documentation + rapports d'audit et archives. |

## Documentation (wiki)

Point d'entrée : **[docs/README.md](docs/README.md)**

- [Installation](docs/installation.md) — GitHub Pages, écran d'accueil, serveur local, cache `cqb-vN`
- [Fonctionnalités](docs/fonctionnalites.md) — spots, identification, cueillettes, stats, sauvegarde
- [Guide d'identification](docs/guide-identification.md) — les 8 espèces, checklist terrain, IA
- [Sécurité alimentaire](docs/securite-alimentaire.md) — badges, verdicts, antipoison, anti-injection
- [Données et confidentialité](docs/donnees-confidentialite.md) — IndexedDB, clé IA, photos, export/import
- [Design](docs/design.md) — style carnet de forêt, palette vert sapin, tokens
- [Déploiement](docs/deploiement.md) — publication, bump du cache, vérifications
- [Licences et crédits](docs/licences-credits.md) — photos Wikimedia, attribution
- [Contribution](docs/contribution.md) — conventions, checklist avant commit
- [Journal des versions](docs/changelog.md) — grandes itérations du projet
