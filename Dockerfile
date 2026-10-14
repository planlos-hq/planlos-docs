FROM docker.io/python:3.13-slim AS builder
RUN pip install --no-cache-dir zensical
WORKDIR /app
COPY zensical.toml settings.yml build.py ./
COPY docs ./docs
COPY overrides ./overrides
RUN python build.py

FROM docker.io/nginx:alpine
COPY --from=builder /app/site /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
