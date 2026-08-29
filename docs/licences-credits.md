# Licences et crédits

> **Wiki Cueillette Boréale** · [Accueil du dépôt](../README.md) · [Index du wiki](README.md)

## Sommaire

- [Code de l'application](#code-de-lapplication)
- [Photos des plantes](#photos-des-plantes)
- [Police de caractères](#police-de-caractères)
- [Comment l'attribution est affichée](#comment-lattribution-est-affichée)
- [Ajouter une photo en respectant la licence](#ajouter-une-photo-en-respectant-la-licence)

## Code de l'application

Aucun fichier `LICENSE` n'est présent dans le dépôt. En l'absence de licence explicite, le
code reste **sous droit d'auteur, tous droits réservés** : personne ne peut légalement le
réutiliser, le modifier ou le redistribuer sans autorisation.

Le fork hérite du code de l'app champignons « Cueillette Québec — édition Memphis »
(`cueillette-memphis`), qui reste en ligne séparément.

Si le projet doit être réutilisable, ajouter un fichier `LICENSE` à la racine (MIT ou
Apache-2.0 pour du permissif) et le mentionner dans le [README](../README.md).

## Photos des plantes

- Emplacement : `img/` — une photo par plante du guide quand elle est embarquée
  (`img/especes/` et `img/specs/` pour les spécificités), sinon la fiche s'affiche sans
  vignette (`img: null` dans `especes-boreales.json`).
- Source : **Wikimedia Commons**.
- Licences rencontrées : CC0, CC BY 2.0/4.0, CC BY-SA 2.0/3.0/4.0.
- Attribution : fichiers `credits.json` du dossier concerné — pour chaque identifiant
  d'espèce, le fichier local, la plante photographiée, l'auteur, la licence et l'URL de la
  page Commons.

Exemple d'entrée :

```json
"bleuet": {
  "fichier": "img/especes/bleuet.jpg",
  "espece": "Vaccinium angustifolium",
  "auteur": "…",
  "licence": "CC BY 2.0",
  "page": "https://commons.wikimedia.org/wiki/File:…"
}
```

## Police de caractères

`fonts/fredoka.woff2` — **Fredoka**, police libre distribuée sous SIL Open Font License 1.1,
auto-hébergée pour éviter tout appel à Google Fonts (confidentialité et fonctionnement
hors-ligne). Conserver le fichier de licence de la fonte si la police est mise à jour.

## Comment l'attribution est affichée

Dans l'app : **Paramètres → Crédits photos**. L'écran liste, pour chaque photo embarquée,
l'espèce, l'auteur, la licence et un lien vers la page Commons d'origine. Les fichiers
`credits.json` sont mis en cache par le service worker, donc l'attribution reste consultable
hors-ligne — c'est une exigence des licences CC BY et CC BY-SA.

## Ajouter une photo en respectant la licence

1. Choisir une image sur Wikimedia Commons dont la licence permet la réutilisation (CC0,
   CC BY, CC BY-SA).
2. Télécharger, recompresser (côté long ≈ 1 200 px, qualité 80) et déposer le fichier dans
   `img/especes/` ou `img/specs/`.
3. Ajouter l'entrée d'attribution complète (fichier, espèce, auteur, licence, page) dans le
   `credits.json` du dossier.
4. Ajouter le chemin au tableau `FICHIERS` de `sw.js`.
5. Incrémenter `cqb-vN` (voir [Déploiement](deploiement.md)).

Ne jamais embarquer une image sans entrée de crédit : sans attribution, la redistribution
d'une image CC BY ou CC BY-SA n'est pas conforme.

Voir aussi : [Design](design.md) · [Contribution](contribution.md) ·
[Guide d'identification](guide-identification.md)
