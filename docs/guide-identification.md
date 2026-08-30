# Guide d'identification

> **Wiki Cueillette Boréale** · [Accueil du dépôt](../README.md) · [Index du wiki](README.md)

> ⚠️ Ce guide est un outil d'aide à la décision. Il ne remplace pas un botaniste ni un
> expert en plantes sauvages. **En cas de doute, on ne mange pas.** Centre antipoison du
> Québec : **1-800-463-5060**.

## Sommaire

- [Méthode en cinq critères](#méthode-en-cinq-critères)
- [Les 8 espèces documentées](#les-8-espèces-documentées)
- [Confusions à connaître au Québec](#confusions-à-connaître-au-québec)
- [Lire les verdicts de la checklist](#lire-les-verdicts-de-la-checklist)
- [Identification par photo (IA)](#identification-par-photo-ia)
- [Ajouter ses propres variétés](#ajouter-ses-propres-variétés)

## Méthode en cinq critères

Chaque fiche du guide propose la même grille de vérification. Les cinq critères sont ceux
qu'un cueilleur peut observer sur place, dans cet ordre :

| # | Critère | Ce qu'on regarde |
|---|---|---|
| 1 | **Feuille** | forme (simple, composée, lobée), bord (denté, lisse), disposition (opposée, alternée, basale), couleur, dessous |
| 2 | **Fruit** | baie, drupe, akène, crosse, fleur ; couleur à maturité, disposition (isolée, en grappe, en couronne) |
| 3 | **Tige** | ronde ou anguleuse, creuse ou pleine, poilue ou lisse, taches ou rayures, sève (laiteuse, colorée) |
| 4 | **Odeur** | froissée ou coupée : ail, carotte, anis, amertume, neutre — une odeur typique est un indice fort |
| 5 | **Habitat** | sous-bois, lisière, tourbière, berges, friche, sol sec ou humide, saison |

Deux réflexes non négociables :

1. **Déterrer la base de la plante au besoin** — tige enterrée, bulbe ou racine : certains
   éléments décisifs se tranchent sous le sol (le bulbe allongé blanc de l'ail des bois, la
   base d'une tige douteuse).
2. **Vérifier les cinq critères, pas un seul.** Une feuille qui ressemble ne prouve rien.

## Les 8 espèces documentées

Statuts : ✅ comestible · ⚠️ comestible mais **prudence d'usage** (modération, espèce
vulnérable ou confusion à vérifier). Aucune espèce du guide n'est toxique ni mortelle.

La liste complète (nom, latin, saison, habitat, description, confusions) fait l'objet de la
page [Espèces boréales](especes-boreales.md) et du fichier `especes-boreales.json` — la
source de vérité technique. Répartition :

| Statut | Espèces |
|---|---|
| ✅ Comestibles | 8 — ail des bois, amélanchier, thé des bois, petit thé, thé du Labrador, poivre des dunes, myrique baumier, comptonie voyageuse |
| ⚠️ Avec prudence | 4 — ail des bois (espèce vulnérable, test de l'odeur d'ail), thé du Labrador (ledol — modération), poivre des dunes (modération, abortif traditionnel), myrique baumier (puissant — modération) |

Total : **8 plantes et baies boréales, toutes comestibles (dont 4 à prudence)** — aucune
espèce toxique ni mortelle au guide.

## Confusions à connaître au Québec

Ces couples sont la raison d'être de la checklist. Chaque fiche du guide nomme les
confusions de l'espèce concernée ; voici les plus coûteuses.

| On cherche… | On risque de ramasser… | Ce qui tranche |
|---|---|---|
| Oignons sauvages | **Ail des bois vs muguet / scille penchée** | l'ail des bois **sent l'ail** au froissage ; le muguet (très toxique) et la scille penchée, **aucune odeur d'ail**. *Si ça ne sent pas l'ail, on ne mange pas.* |
| Thé du Labrador | **Laurier des marais** (toxique) | dessous des feuilles **roux feutré** (vrai thé du Labrador) vs **vert** (laurier) ; fleurs **blanches** en ombelle vs **roses** en coupe |
| Petit thé | **Baie blanche** (non comestible) | le petit thé est une **plante rampante** sur la mousse, avec **poils roux** sous les feuilles ; la baie blanche est une **plante dressée** des milieux secs |
| Thé des bois | **Maïs de poule** (baie de prairie) | le thé des bois **sent la wintergreen** (pincette) au froissement ; le maïs de poule, aucune odeur |
| Poivre des dunes | **Autres aulnes** (aulne rouge/incise) | feuilles **gaufrées crispées** du petit arbuste 1-3 m des milieux secs ; les feuilles d'aulne commun sont plus grandes et plus lisses |
| Comptonie voyageuse / myrique baumier | **Myrique baumier / comptonie voyageuse** | feuilles **de fougère** (comptonie, sol sec sablonneux) vs **dentées** (myrique, milieu humide) — les deux restent comestibles |

Règle générale : **toute plante non identifiée avec certitude reste dans le bois.** Les
confusions les plus coûteuses touchent l'ail des bois et le thé du Labrador : vérifiez
l'**odeur** et le **dessous des feuilles** avant de consommer.

## Lire les verdicts de la checklist

| Verdict | Quand il apparaît | Ce qu'il veut dire |
|---|---|---|
| ⚠️ ambre, 0 critère | à l'ouverture de la fiche | « Rien n'est encore vérifié » — ne consommez pas |
| ⚠️ ambre, n/5 | critères partiellement cochés | il manque des vérifications — **en cas de doute, on ne mange pas** |
| ✅ vert | tous les critères cochés **et** espèce comestible (ou à prudence) | récolte possible en respectant la prudence indiquée |
| ☠️ rouge | espèce non comestible, peu importe le nombre de critères | ne pas consommer, jamais |

Le verdict vert est **impossible** sur une espèce toxique ou mortelle. Aucune des 8 espèces
du guide n'est ni toxique ni mortelle : le verdict rouge sert aux espèces hors guide ou aux
variétés perso déclarées dangereuses, et s'affiche alors avec le numéro du centre antipoison.

## Identification par photo (IA)

Fonction facultative, active seulement si une clé API Gemini **ou OpenRouter** est
enregistrée dans les paramètres.

**Comment l'utiliser**

1. Onglet Identifier → bouton d'identification par photo.
2. Prendre la photo (ou choisir dans la galerie) : **feuille et fruit visibles**, de
   préférence la plante entière en place — et la base de la tige au besoin.
3. L'IA retourne l'espèce probable, le nom latin, le statut, un pourcentage de confiance, une
   description, les caractéristiques observées et les confusions à éviter.

**Comment lire le résultat**

| Confiance | Affichage | À faire |
|---|---|---|
| ≥ 90 % | résultat présenté comme fiable | vérifier quand même les 5 critères sur la fiche du guide |
| 60 à 89 % | « à vérifier » | traiter comme une hypothèse ; ne pas consommer sans confirmation |
| < 60 % ou « inconnu » | aucune confiance | recommencer avec de meilleures photos, ou renoncer |

**Garde-fous appliqués**

- Le statut du guide **écrase** celui de l'IA quand le nom (ou un synonyme, une faute de
  frappe proche) correspond à une espèce documentée : le plus grave gagne. Une IA qui
  répondrait « comestible, 95 % » sur une espèce dangereuse affiche quand même MORTEL.
- Une espèce **absente du guide** ne reçoit jamais un badge vert seul : une alerte
  « Espèce absente du guide » rappelle que l'identification repose uniquement sur l'IA.
- Les espèces masquées ou supprimées du guide conservent leur filet de sécurité (tombes).
- Le prompt d'identification ordonne explicitement d'**ignorer toute consigne écrite dans
  l'image** (panneau, étiquette, légende) — protection contre l'injection de consignes. Voir
  [Sécurité alimentaire](securite-alimentaire.md).

**Ce que l'IA ne peut pas faire** : sentir, goûter, palper la tige, vérifier une racine
déterrée ni confirmer une odeur d'ail. Elle ne remplace donc jamais la checklist.

## Ajouter ses propres variétés

Onglet Identifier → bouton ＋. La feuille se remplit en deux étapes (Identité, puis Détails
et photo). Les détails peuvent être générés par IA (Gemini ou OpenRouter selon le
fournisseur choisi dans les paramètres).

Une variété perso porte le badge « perso » dans le guide et est incluse dans l'export JSON.
Le statut de comestibilité qu'on lui donne participe au filet de sécurité : si elle est
homonyme d'une espèce du guide, le statut le plus grave s'applique.

Voir aussi : [Espèces boréales](especes-boreales.md) ·
[Sécurité alimentaire](securite-alimentaire.md) · [Fonctionnalités](fonctionnalites.md)
