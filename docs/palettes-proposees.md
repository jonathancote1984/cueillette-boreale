# Palettes « boréal » proposées — Cueillette Boréale

Trois variantes de la palette Memphis existante, pensées pour une ambiance boréal québécoise.
Seuls les 10 tokens CSS du `:root` changent — aucune règle, aucune structure modifiée.
Captures : `.qa/palette-{1,2,3}.png` (accueil) + `.qa/palette-{n}-identifier.png` et
`.qa/palette-{n}-badges.png` (onglet Identifier, badges comestible / MORTEL).
Rendues depuis des copies temporaires `.qa/preview-palette-{1,2,3}.html` — **`index.html`
du repo n'a pas été modifié**.

Contrastes calculés (ratio WCAG) sur fond `--creme` (corps) et pour les badges
(texte `--blanc` sur `--rouge` / `--olive`). Cible AA : ≥ 4,5 pour le texte courant ;
≥ 4,5 pour les badges (petits libellés), ≥ 3,0 toléré pour gros libellés.

---

## 1. « Lac et lichen » — froide, nordique, la plus distinctive

| Token | Hex |
|---|---|
| --creme | `#EAF0F2` |
| --noir | `#0E1B24` |
| --blanc | `#F6FAFB` |
| --rouge (MORTEL) | `#8E1F2F` |
| --gris | `#7D97A6` |
| --ambre → primaire | `#3D7EA6` |
| --olive → secondaire | `#5C7F52` |
| --cuir | `#33566B` |
| --rouille | `#4C7A99` |
| --terracotta | `#A5384A` |

**Ambiance.** Brouillard matinal sur un lac. La seule famille chaude qui reste est le
rouge mortel (et le terracotta « baie ») — il ressort d'autant plus, ce qui est
sémantiquement idéal pour le danger.

**Contraste sur --creme.** noir 15,2 · rouge 7,6 · cuir 6,8 · terracotta 5,6 ·
rouille 4,0 · olive 3,9 · primaire 3,9 (boutons : utiliser texte --blanc, comme le
thème actuel) · gris 2,7 (décoratif seulement).

**Badges.** MORTEL rouge/blanc **8,4** (AAA) ; comestible olive/blanc **4,3** (AA) ;
écart visuel rouge↔olive très large (ΔRGB ≈ 114) — confusion impossible.

**Captures :** `.qa/palette-1.png`, `.qa/palette-1-identifier.png`, `.qa/palette-1-badges.png`.
La plus audacieuse : elle change vraiment la personnalité de l'app en gardant le
squelette Memphis intact.

---

## 2. « Mousse et canneberge » — chaude, forestière, la transition la plus douce

| Token | Hex |
|---|---|
| --creme | `#EFEAD8` |
| --noir | `#1C2416` |
| --blanc | `#F9F7EA` |
| --rouge (MORTEL) | `#8E1F2F` |
| --gris | `#93997F` |
| --ambre → primaire | `#C4841D` |
| --olive → secondaire | `#4E6B32` |
| --cuir | `#5C4326` |
| --rouille | `#8A4A0F` |
| --terracotta | `#A64B2A` |

**Ambiance.** Sous-bois de fin d'été : mousse, aiguilles, canneberges. Un utilisateur
existant de la palette actuelle ne sera pas dépaysé — c'est une version « plus forêt ».

**Contraste sur --creme.** noir 13,3 · rouge 7,3 · cuir 7,6 · rouille 5,7 ·
terracotta 4,8 · olive 5,0 · primaire 2,6 sur creme mais réservé aux fonds de gros
boutons avec texte --noir (ambre/noir = **5,1**, AA) · gris 2,5 (décoratif).

**Badges.** MORTEL rouge/blanc **8,2** (AAA) ; comestible olive/blanc **5,6** — le
meilleur des trois (AA) ; ΔRGB rouge↔olive ≈ 99, nettement distincts.
Meilleure lisibilité globale : tous les tokens porteurs de texte ≥ 4,5.

**Captures :** `.qa/palette-2.png`, `.qa/palette-2-identifier.png`, `.qa/palette-2-badges.png`.
**Recommandée** pour un changement sûr, sans surprise.

---

## 3. « Aulnaie » — terreuse, feutrée, l'option rustique

| Token | Hex |
|---|---|
| --creme | `#EDE6D2` |
| --noir | `#24170C` |
| --blanc | `#F8F1DE` |
| --rouge (MORTEL) | `#7A1A1A` |
| --gris | `#8A8270` |
| --ambre → primaire | `#B07A2A` |
| --olive → secondaire | `#63742E` |
| --cuir | `#5F4326` |
| --rouille | `#8F4E1C` |
| --terracotta | `#9C4522` |

**Ambiance.** Berge d'aulnes en octobre : écorces, bois mort, feuilles rousses.
Palette monochrome chaude, la plus discrète — presque sépia, très « carnet de terrain ».

**Contraste sur --creme.** noir 14,0 · rouge 8,5 · cuir 7,3 · rouille 5,2 ·
terracotta 5,1 · olive 4,1 · primaire 3,0 (boutons : texte --noir sur primaire =
**4,7**, AA) · gris 3,1 (décoratif).

**Badges.** MORTEL rouge/blanc **9,4** (AAA, le plus contrasté des trois) ;
comestible olive/blanc **4,6** (AA) ; ΔRGB rouge↔olive ≈ 95 — distincts, et le rouge
très assombri ne se confond avec aucun vert.

**Captures :** `.qa/palette-3.png`, `.qa/palette-3-identifier.png`, `.qa/palette-3-badges.png`.

---

## Verdict rapide

- **Sûr et chaleureux** → « Mousse et canneberge » (#2).
- **Changeant et mémorable** → « Lac et lichen » (#1) — le bleu lac rend l'app
  immédiatement reconnaissable, et le rouge mortel ressort encore mieux.
- **Rustique / carnet de terrain** → « Aulnaie » (#3).

Previews temporaires : `.qa/preview-palette-{1,2,3}.html` (à supprimer une fois la palette choisie).
