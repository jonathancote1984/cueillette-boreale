# Guide d'identification

> **Wiki Cueillette Boréale** · [Accueil du dépôt](../README.md) · [Index du wiki](README.md)

> ⚠️ Ce guide est un outil d'aide à la décision. Il ne remplace pas un botaniste ni un
> expert en plantes sauvages. **En cas de doute, on ne mange pas.** Centre antipoison du
> Québec : **1-800-463-5060**.

## Sommaire

- [Méthode en cinq critères](#méthode-en-cinq-critères)
- [Les 17 espèces documentées](#les-17-espèces-documentées)
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

1. **Déterrer la base de la plante au besoin** — tige enterrée, bulbe ou racine : certaines
   confusions mortelles se tranchent sous le sol (la racine à cloisons transversales de la
   ciguë aquatique).
2. **Vérifier les cinq critères, pas un seul.** Une feuille qui ressemble ne prouve rien.

## Les 17 espèces documentées

Statuts : ✅ comestible · ⚠️ comestible mais **cuisson ou prudence obligatoire** ·
☣️ toxique · ☠️ **mortel**.

La liste complète (nom, latin, saison, habitat, description, confusions) fait l'objet de la
page [Espèces boréales](especes-boreales.md) et du fichier `especes-boreales.json` — la
source de vérité technique. Répartition :

| Statut | Espèces |
|---|---|
| ✅ Comestibles | 8 — bleuet nain, camarine noire, chicouté, framboisier, fraise sauvage, amélanchier, vigne des rivages, aralie à grappes |
| ⚠️ Comestibles avec prudence | 3 — ail des bois (confusion scille penchée, espèce vulnérable), fougère-aigle (jeunes crosses bien cuites), sureau du Canada (fleurs et baies toujours cuites) |
| ☣️ Toxiques | 3 — morelle noire, raisin d'Amérique (phytolacque), berce laineuse (sève phototoxique) |
| ☠️ Mortelles | 3 — ciguë maculée, ciguë aquatique, datura stramoine |

Total : **17 espèces**, 11 comestibles (dont 4 à prudence si l'on compte la fougère-aigle
comme comestible conditionnelle), 3 toxiques, 3 mortelles.

## Confusions à connaître au Québec

Ces couples sont la raison d'être de la checklist. Chaque fiche du guide nomme les
confusions de l'espèce concernée ; voici les plus coûteuses.

| On cherche… | On risque de ramasser… | Ce qui tranche |
|---|---|---|
| Carotte sauvage | **Ciguë maculée**, mortelle | la ciguë a une **tige lisse à taches pourpres** et une **odeur de souris** ; la carotte sauvage a une **tige poilue** et une odeur de carotte. *La confusion qui tue.* |
| Certaines ombellifères de berges | **Ciguë aquatique**, la plus mortelle d'Amérique du Nord | déterrer la racine : elle porte des **cloisons transversales** (chambres en nid d'abeille à la coupe). En cas de doute devant une ombellifère de milieu humide : on ne cueille pas. |
| Angélique / carotte sauvage | **Berce laineuse** (toxique) | sève **phototoxique** : contact + soleil = brûlures graves. Grande ombellifère à tige couverte de poils laineux. |
| Oignon sauvage | **Ail des bois vs scille penchée** | l'ail des bois **sent l'ail** au froissage de la feuille ; la scille penchée, toxique, n'a **aucune odeur d'ail**. Espèce vulnérable : récolte encadrée. |
| Petites baies noires | **Morelle noire** (toxique) | baies noires en grappes **sans « couronne »** au sommet — contrairement au bleuet ou à la cerise de terre |
| Baies rouges de bord de champ | **Raisin d'Amérique / phytolacque** (toxique) | grappes pendantes sur axe rouge pourpre ; **toute la plante est toxique, racine très toxique** |

Règle générale : **toute ombellifère non identifiée avec certitude reste dans le bois.**
Deux espèces mortelles sur trois du guide en sont.

## Lire les verdicts de la checklist

| Verdict | Quand il apparaît | Ce qu'il veut dire |
|---|---|---|
| ⚠️ ambre, 0 critère | à l'ouverture de la fiche | « Rien n'est encore vérifié » — ne consommez pas |
| ⚠️ ambre, n/5 | critères partiellement cochés | il manque des vérifications — **en cas de doute, on ne mange pas** |
| ✅ vert | tous les critères cochés **et** espèce comestible (ou à prudence) | récolte possible en respectant la prudence indiquée |
| ☠️ rouge | espèce non comestible, peu importe le nombre de critères | ne pas consommer, jamais |

Le verdict vert est **impossible** sur une espèce toxique ou mortelle : cocher les cinq
critères d'une ciguë maculée donne un verdict rouge avec le numéro du centre antipoison.

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
  répondrait « comestible, 95 % » sur une ciguë affiche quand même MORTEL.
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
