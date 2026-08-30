# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Utilisateur principal : Jonathan (le propriétaire), sur son téléphone, en forêt et à la maison. Partage possible à des proches (export/import JSON) — pas un outil public.

## Product Purpose

Carnet de chasse personnel + guide d'identification des plantes et baies boréales du Québec, 100 % hors-ligne, dans un style « carnet de forêt » vert sapin. Le succès = retrouver ses coins secrets, noter ses récoltes, identifier une plante avec confiance, et prendre du plaisir à le faire.

## Positioning

Le carnet vit sur le téléphone, sans compte ni serveur : les données ne quittent jamais l'appareil, tout fonctionne en forêt sans réseau. Le guide combine 8 espèces comestibles documentées du Québec (dont 4 à récolter avec prudence), l'identification par photo (IA) et des variétés personnelles enrichies par IA — avec un parti pris sécurité systématique (espèces à usage encadré, centre antipoison). Aucun champignon : l'app est volontairement concentrée sur la flore boréale.

## Operating Context

- Terrain : forêts du Québec, téléphone en main, souvent sans réseau — PWA installable, 100 % hors-ligne dès la première visite.
- Saisons de cueillette : feuilles au printemps-été, baies à la fin de l'été, chatons et feuilles persistantes en automne-hiver.
- Utilisation : noter un spot (GPS), identifier sur place (photo), journaliser la récolte (poids, météo, spot), consulter les stats.
- Partage : export/import JSON complet (version 5, inclut espèces masquées, supprimées et illustrations).

## Capabilities and Constraints

- Spots : nom, description, GPS (précision affichée), photo, lien Google Maps.
- Guide : 8 espèces avec photos Wikimedia embarquées, badges comestible / prudence / immangeable / toxique, saison, habitat, caractéristiques clés, confusions avec des espèces toxiques ressemblantes.
- Fiches hybrides : 5 spécificités d'identification par espèce (feuille, fruit, tige, odeur, habitat) avec photo réelle embarquée (22 photos Wikimedia dans `img/specs/`), description de ce qu'il faut vérifier, checklist terrain interactive (cases à cocher, compteur, verdict ⚠️/✅) persistée localement.
- Identification par photo : Gemini ou OpenRouter (appareil ou galerie), avec niveau de confiance et alertes de sécurité.
- Variétés perso : ajout / modification / suppression, masquage / restauration sélective, fiche générée par IA, photo Wikimedia Commons ou illustration IA (par spécificité : feuilles, tige, fleur, fruit, habitat).
- Cueillettes : date, espèce (suggestions + libre), poids kg (virgule acceptée), spot lié, météo, note, photo.
- Stats : total récolté, sorties, espèces distinctes, dernière sortie, tops espèces/spots, barres mensuelles.
- Sauvegarde : export/import JSON, effacement complet avec double confirmation.
- Contrainte technique : PWA statique mono-fichier (`index.html`, ~190 Ko, zéro framework, pas de build), service worker cache-first avec bump `cqb-vN` à chaque changement (le numéro courant vit dans `sw.js`, jamais dans cette doc). API Wikimedia/Gemini/OpenRouter exclues du cache. Déployée sur GitHub Pages (jonathancote1984.github.io/cueillette-boreale), push main → déploiement auto.
- Données : IndexedDB (`cqb_bd` v5 : spots, cueillettes, especes, caches, illustrations, supprimees, checklist) avec repli localStorage ; clé IA stockée localement, jamais envoyée ailleurs. Paramètres : unités kg/lb (affichage + saisie), fournisseur d'IA (Gemini/OpenRouter) et clé API. Suppression d'espèces d'origine = store `supprimees` + double confirmation.
- Langue : français du Québec.

## Brand Commitments

- Nom : « Cueillette Boréale » (court : Cueillette).
- Style « carnet de forêt » : bordures noires épaisses (3 px), coins cassés, ombres dures sans flou, formes géométriques, titres légèrement inclinés, zigzags/pois.
- Palette VERT SAPIN : fond crème sapin `#EFF3EC`, primaire sapin `#1E4D33`, mousse `#5E8C4A`, vert forêt `#3A5C42`, pruche `#4C7A55`, terracotta `#B5651D`, blanc `#F8FBF6`, noir `#0F2418`, rouge mortel `#A32633`.
- Typographie : Fredoka (arrondie) avec repli système.
- Icône : 3 bleuets sur fond vert sapin (générée par `generer_icones.py`).
- Jamais de boîtes système navigateur (confirm/alert) : modales stylées.
- Avertissements de sécurité non négociables : espèces à prudence (cuisson obligatoire / usage encadré) + centre antipoison Québec 1-800-463-5060.

## Evidence on Hand

- Photos réelles des 8 espèces dans `img/especes/` avec crédits Wikimedia (`credits.json`).
- 22 photos de spécificités dans `img/specs/` (8 espèces × 2-3 critères) avec crédits Wikimedia (`credits.json`).
- Icônes PWA (`icons/`), scripts de génération (`generer_icones.py`, `scripts/telecharger_photos.py`).
- README documenté. Aucun témoignage ni donnée utilisateur publique — les données sont privées et locales.

## Product Principles

1. La sécurité prime : toute ambiguïté d'identification penche vers la prudence et le centre antipoison.
2. Le terrain d'abord : conçue pour une utilisation en forêt, une main, sans réseau — rapide et hors-ligne.
3. Le carnet est privé : données 100 % locales, aucune donnée envoyée sans action explicite de l'utilisateur.
4. Le plaisir de la récolte : l'identité « carnet de forêt » verte et chaleureuse rend le carnet ludique, pas clinique.
5. Zéro friction : pas de compte, pas de serveur, pas d'abonnement — l'app est libre et installable.
6. La forêt d'abord : on cueille avec respect — l'ail des bois (espèce vulnérable) est encadré, et la récolte se fait selon les règles locales.
