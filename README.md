python -m venv venv
source venv/bin/activate
pip freeze > requirements.txt

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head


uvicorn app.main:app --reload



docker build -t fastapi_template_database -f DockerfilePostgreSQL .
docker run --name fastapi-template-databasecontainer -d -p 5432:5432 fastapi_template_database


docker build -t fastapi-template .
docker run -d --name fastapi_template_container -p 8000:8000 fastapi-template




```
fastapi-template
├─ .dockerignore
├─ .gitignore
├─ Dockerfile
├─ DockerfilePostgreSQL
├─ README.md
├─ alembic
│  ├─ README
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
├─ alembic.ini
├─ app
│  ├─ api
│  │  ├─ dependencies.py
│  │  └─ v1
│  │     ├─ auth.py
│  │     └─ users.py
│  ├─ core
│  │  └─ config.py
│  ├─ db
│  │  ├─ base.py
│  │  ├─ models
│  │  │  └─ user.py
│  │  └─ session.py
│  ├─ main.py
│  ├─ schemas
│  │  ├─ token.py
│  │  └─ user.py
│  └─ services
│     ├─ auth.py
│     └─ user.py
├─ requirements.txt
└─ tests
   ├─ test_auth.py
   └─ test_users.py

```