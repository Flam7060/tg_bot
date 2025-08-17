# Используем официальный образ uv с Python 3.12
FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Рабочая папка, в которую копируем проект
WORKDIR /src

# Копируем весь проект сюда
COPY . .

# Добавляем /src в PYTHONPATH для видимости пакета app
ENV PYTHONPATH=/src

# Опционально создаем виртуальное окружение (если нужно)
RUN uv venv

# Запускаем бот
CMD ["uv", "run", "app/main.py"]

## ХУЙНЯ НАПИСАННАЯ ГПТ, БЫЛО В ПАДЛУ!