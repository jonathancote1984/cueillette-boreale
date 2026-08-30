/* Service worker — cache-first PWA (édition Memphis).
   ⚠️ RÈGLE : à CHAQUE mise à jour de l'app, AUGMENTEZ le numéro de CACHE.
   Le bump IS le mécanisme de mise à jour pour les utilisateurs. */
const CACHE = 'cqb-v6';
const FICHIERS = [
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './fonts/fredoka.woff2'
];

self.addEventListener('install', e => {
  // AUDIT M8 (2026-08) : une ressource manquante ne doit plus tuer l'installation —
  // socle critique en addAll, images en add() individuel tolérant
  e.waitUntil(caches.open(CACHE).then(c =>
    c.addAll(SOCLE).catch(() => {}).then(() =>
      Promise.allSettled(IMAGES.map(f => c.add(f)))
    )
  ).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(cles => Promise.all(cles.filter(c => c.startsWith('cqb-') && c !== CACHE).map(c => caches.delete(c))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  // API et requêtes avec clé : jamais de cache (résultats frais, clé jamais stockée)
  // Wiki docsify (/docs/) et guide (/guide/) : jamais mis en cache ni interceptés — toujours à jour
  if (url.origin === self.location.origin && (url.pathname.includes('/docs/') || url.pathname.includes('/guide/'))) return;
  if (url.hostname.endsWith('wikimedia.org') || url.hostname.endsWith('googleapis.com') || url.hostname.endsWith('mycoquebec.org') || url.search.includes('key=')) return;
  e.respondWith(
    caches.match(e.request).then(reponse => reponse || fetch(e.request).then(r => {
      // AUDIT M13 : ne jamais empoisonner le cache avec une réponse d'erreur
      if (r.ok || r.type === 'opaque') {
        const copie = r.clone();
        caches.open(CACHE).then(c => c.put(e.request, copie)).catch(() => {});
      }
      return r;
    }).catch(() => {
      // AUDIT M9 : le fallback HTML est réservé aux navigations — jamais aux images/JSON
      if (e.request.mode === 'navigate') return caches.match('./index.html');
      return Response.error();
    }))
  );
});
