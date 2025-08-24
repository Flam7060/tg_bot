FROM python:3.12-slim-trixie

RUN useradd -m appuser

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /src

COPY . .

RUN chown -R appuser:appuser /src

USER root
RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*
USER appuser

ENV PYTHONPATH=/src

RUN uv venv

CMD ["uv", "run", "app/main.py"]
