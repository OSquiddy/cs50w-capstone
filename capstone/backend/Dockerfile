# capstone/backend/Dockerfile
# Django REST Framework API, served by gunicorn.
# Multi-stage: build wheels in one layer, install into a slim runtime.

# ---------- build ----------
FROM python:3.8-slim AS build

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# libpq-dev  -> psycopg2
# libjpeg/zlib -> Pillow (patient report images)
# libfreetype  -> ReportLab PDF generation
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        libjpeg-dev \
        zlib1g-dev \
        libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip wheel --wheel-dir /wheels -r requirements.txt \
    && pip wheel --wheel-dir /wheels gunicorn psycopg2-binary


# ---------- runtime ----------
FROM python:3.8-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DJANGO_SETTINGS_MODULE=capstone.settings

# Runtime shared libs only - no compilers in the final image
RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq5 \
        libjpeg62-turbo \
        zlib1g \
        libfreetype6 \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Never run the container as root
RUN groupadd --system app && useradd --system --gid app --home /app app

WORKDIR /app

COPY --from=build /wheels /wheels
COPY requirements.txt .
RUN pip install --no-index --find-links=/wheels -r requirements.txt \
    && pip install --no-index --find-links=/wheels gunicorn psycopg2-binary \
    && rm -rf /wheels

COPY --chown=app:app . .

# collectstatic needs *some* value for these at build time; the real ones
# are injected at runtime from SSM Parameter Store.
RUN DJANGO_SECRET_KEY=build-time-only \
    DJANGO_ALLOWED_HOSTS=localhost \
    python manage.py collectstatic --noinput

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD curl -fsS http://localhost:8000/healthz/ || exit 1

# 3 workers is a starting point. Rule of thumb is (2 x vCPU) + 1 -
# tune it against your actual Fargate task size, and be able to say why.
CMD ["gunicorn", "capstone.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "3", \
     "--threads", "2", \
     "--timeout", "120", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]
