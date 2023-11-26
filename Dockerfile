FROM python:3.10.12

WORKDIR /app

COPY pyproject.toml /app
COPY poetry.lock /app
COPY README.md /app
COPY .env /app

RUN pip install poetry

RUN poetry install

EXPOSE 6600

COPY . /app


CMD [ "poetry", "run", "start" ]