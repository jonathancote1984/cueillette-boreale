# Espèces boréales — contenu de l'application

**17 espèces** : 11 comestibles (dont 4 à manipuler/manger avec prudence), 3 toxiques, 3 mortelles.
Format identique à la base champignons (`ESPECES` de `index.html`), champignons conservés en bonus.

Source de vérité technique : `/home/jo/workspace/.qa/especes-boreales.json` (copié dans le repo à
l'intégration). Chaque fiche suit le schéma :

```json
{
  "id": "bleuet",
  "img": null,
  "nom": "Bleuet nain",
  "latin": "Vaccinium angustifolium",
  "statut": "comestible | toxique | mortel | inconnu",
  "prudence": true | false,
  "saison": "...",
  "habitat": "...",
  "desc": "...",
  "carac": ["...", "..."],
  "confusions": "..."
}
```

## Liste des espèces

### Comestibles (prudence: false)
| # | Nom | Latin | Saison |
|---|---|---|---|
| 1 | Bleuet nain | *Vaccinium angustifolium* | Juillet–août |
| 2 | Camarine noire | *Empetrum nigrum* | Août–septembre |
| 3 | Chicouté (plaquebière) | *Rubus chamaemorus* | Mi-juillet–août |
| 4 | Framboisier commun | *Rubus idaeus* | Juillet–septembre |
| 5 | Fraise sauvage | *Fragaria virginiana* | Juin–juillet |
| 6 | Amélanchier | *Amelanchier alnifolia* | Juillet–août |
| 7 | Vigne des rivages | *Vitis riparia* | Septembre–octobre |
| 8 | Aralie à grappes | *Aralia racemosa* | Août–septembre |

### Comestibles avec prudence (prudence: true — vigilance accrue)
| # | Nom | Raison de prudence |
|---|---|---|
| 9 | Ail des bois | confusion mortelle possible avec la **scille penchée** (sans odeur d'ail) ; espèce vulnérable, récolte encadrée |
| 10 | Fougère-aigle (crosses) | toxique adulte ; seules les jeunes crosses bien enroulées, bien cuites |
| 11 | Sureau du Canada | fleurs et baies **toujours cuites** (glycosides cyanogènes à l'état cru) |

### Toxiques
| # | Nom | Danger |
|---|---|---|
| 12 | Morelle noire | solanine ; baies noires en grappes, sans « couronne » |
| 13 | Raisin d'Amérique (phytolacque) | toute la plante toxique, racine très toxique |
| 14 | Berce laineuse | sève **phototoxique** (brûlures au soleil) ; confusion avec angélique/carotte sauvage |

### Mortelles
| # | Nom | Danger |
|---|---|---|
| 15 | Ciguë maculée | paralysie respiratoire ; tiges à taches pourpres, odeur de souris. **La confusion qui tue : carotte sauvage** (tige poilue, odeur de carotte) |
| 16 | Ciguë aquatique | la plus mortelle d'Amérique du Nord ; racine à cloisons transversales |
| 17 | Datura stramoine | alcaloïdes tropaniques ; fleur en trompette, capsule épineuse |

## Règles de sécurité intégrées
- Le statut **mortel l'emporte toujours** sur tout autre réglage (logique « plus grave gagne » de l'app).
- Les fiches **toxiques/mortelles** portent des **confusions explicites** avec les comestibles.
- Champignons : conservés comme **section bonus** (21 espèces existantes).

## Sources principales
- *Flore laurentienne* (Frère Marie-Victorin) — référence botanique du Québec
- Gouvernement du Québec (MFFP, quebec.ca) — statuts, espèces vulnérables (ail des bois)
- Centre antipoison du Québec : **1-800-463-5060** (inchangé dans l'app)
