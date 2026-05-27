/* Network-first for bank + shell so GitHub Pages updates show after deploy */

const CACHE = 'engs32-env-v9';

const SHELL = ['./manifest.json', './icon.svg'];

const NETWORK_FIRST_PARTS = ['questions.js', 'version.js', 'bank.json', 'index.html', 'sw.js'];



self.addEventListener('install', function (e) {

  e.waitUntil(

    caches.open(CACHE).then(function (cache) {

      return cache.addAll(SHELL);

    })

  );

  self.skipWaiting();

});



self.addEventListener('activate', function (e) {

  e.waitUntil(

    caches.keys().then(function (keys) {

      return Promise.all(

        keys

          .filter(function (k) {

            return k !== CACHE;

          })

          .map(function (k) {

            return caches.delete(k);

          })

      );

    })

  );

  self.clients.claim();

});



function isNetworkFirst(url) {

  var path = url.pathname || '';

  return NETWORK_FIRST_PARTS.some(function (s) {

    return path.indexOf(s) !== -1;

  });

}



function shouldCacheResponse(res) {

  if (!res || res.status !== 200) return false;

  var ct = (res.headers.get('content-type') || '').toLowerCase();

  return ct.indexOf('text/html') === -1;

}



self.addEventListener('fetch', function (e) {

  if (e.request.method !== 'GET') return;

  if (!e.request.url.startsWith(self.location.origin)) return;



  if (isNetworkFirst(new URL(e.request.url))) {

    e.respondWith(

      fetch(e.request)

        .then(function (res) {

          if (shouldCacheResponse(res)) {

            var copy = res.clone();

            caches.open(CACHE).then(function (c) {

              c.put(e.request, copy);

            });

          }

          return res;

        })

        .catch(function () {

          return caches.match(e.request).then(function (hit) {

            return (

              hit ||

              new Response('Offline — connect once to load the latest question bank.', {

                status: 503,

                headers: { 'Content-Type': 'text/plain; charset=utf-8' },

              })

            );

          });

        })

    );

    return;

  }



  if (e.request.mode === 'navigate') {

    e.respondWith(

      fetch(e.request)

        .then(function (res) {

          if (shouldCacheResponse(res)) {

            var copy = res.clone();

            caches.open(CACHE).then(function (c) {

              c.put(e.request, copy);

            });

          }

          return res;

        })

        .catch(function () {

          return caches.match('./index.html').then(function (hit) {

            return (

              hit ||

              new Response('Offline — open once online to cache the app.', {

                status: 503,

                headers: { 'Content-Type': 'text/plain; charset=utf-8' },

              })

            );

          });

        })

    );

    return;

  }



  e.respondWith(

    caches.match(e.request).then(function (cached) {

      if (cached) return cached;

      return fetch(e.request).then(function (res) {

        if (shouldCacheResponse(res)) {

          var clone = res.clone();

          caches.open(CACHE).then(function (c) {

            c.put(e.request, clone);

          });

        }

        return res;

      });

    })

  );

});

