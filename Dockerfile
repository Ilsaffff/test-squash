FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml .
RUN poetry install --no-root
COPY . .