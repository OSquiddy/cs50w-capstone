# capstone/frontend/Dockerfile
# Vue 2 SPA -> static bundle -> nginx.

# ---------- build ----------
# NOTE: node:16, not 18 or 20, on purpose.
# Vue CLI 4 uses webpack 4, which breaks on Node 17+ with
# "error:0308010C:digital envelope routines::unsupported" (OpenSSL 3).
# If you upgrade Node later you will need NODE_OPTIONS=--openssl-legacy-provider
# or a vue-cli upgrade. Know this answer - it is a common interview aside.
FROM node:16-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

# Baked in at BUILD time, not runtime - this is a static bundle, so the API
# URL is compiled into the JS. Passed via --build-arg from CI.
ARG VUE_APP_API_URL=/api
ENV VUE_APP_API_URL=$VUE_APP_API_URL

RUN npm run build


# ---------- runtime ----------
FROM nginx:1.25-alpine AS runtime

# !! CHECK THIS PATH FIRST !!
# Vue CLI defaults to /app/dist, but your README refers to a `build` directory.
# Look at `outputDir` in vue.config.js. If it is "build", change the line below.
COPY --from=build /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN addgroup -S web && adduser -S -G web web \
    && chown -R web:web /usr/share/nginx/html \
    && touch /var/run/nginx.pid \
    && chown -R web:web /var/run/nginx.pid /var/cache/nginx

USER web

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD wget -qO- http://localhost/healthz || exit 1

CMD ["nginx", "-g", "daemon off;"]
