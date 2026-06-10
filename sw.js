/* Grammar Heroes — Service Worker
   Strategi:
   - App shell (HTML, ikon, manifest) di-cache masa pasang → offline serta-merta.
   - Font Google (CSS + .woff2) di-cache masa guna pertama → offline selepas itu.
   Tukar nama CACHE bila Cikgu kemas kini app supaya pengguna dapat versi baru.   */

const CACHE = "grammar-heroes-v1";

const APP_SHELL = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icon-192.png",
  "./icon-512.png",
  "./icon-maskable.png",
  "./apple-touch-icon.png",
  "./favicon.png"
];

// Pasang: simpan app shell
self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(APP_SHELL)).then(() => self.skipWaiting())
  );
});

// Aktif: buang cache lama
self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Fetch: cache-first, kemudian rangkaian (dan simpan font untuk kali seterusnya)
self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);
  const isFont =
    url.origin.includes("fonts.googleapis.com") ||
    url.origin.includes("fonts.gstatic.com");

  e.respondWith(
    caches.match(req).then((hit) => {
      if (hit) return hit;
      return fetch(req)
        .then((res) => {
          // simpan salinan: app shell sendiri + font Google
          if (isFont || url.origin === self.location.origin) {
            const copy = res.clone();
            caches.open(CACHE).then((c) => c.put(req, copy));
          }
          return res;
        })
        .catch(() => {
          // offline & tiada dalam cache → bagi halaman utama untuk navigasi
          if (req.mode === "navigate") return caches.match("./index.html");
        });
    })
  );
});
