FROM python:3.12-slim-trixie


RUN useradd -m appuser


COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


WORKDIR /src


COPY . .


RUN chown -R appuser:appuser /src


USER root


RUN apt-get update && apt-get install -y curl=7.68.0-1ubuntu2.12 ca-certificates=20210119~20.04.2 --no-install-recommends && rm -rf /var/lib/apt/lists/*


USER appuser


ENV PYTHONPATH=/src


# Добавление HEALTHCHECK для состояния контейнера
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f https://api.telegram.org/bot${tg_bot_token}/getMe || exit 1


RUN uv venv


CMD ["uv", "run", "app/main.py"]