FROM python:3.10 AS base
WORKDIR /
RUN pip install pipenv

WORKDIR /microservice
COPY ./microservice/Pipfile* ./

# NOTE: The combo --deploy --ignore-pipfile ensures reproducible builds

# TODO Keep this DRY (involves having more build stages)

FROM base AS development-build
RUN pipenv install --deploy --ignore-pipfile --dev
COPY ./microservice/setup.py ./microservice/pytest.ini ./
COPY ./microservice/app ./app
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]

FROM base AS production-build
RUN pipenv install --deploy --ignore-pipfile
COPY ./microservice/setup.py ./microservice/pytest.ini ./
COPY ./microservice/app ./app
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]