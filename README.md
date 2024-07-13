python -m venv venv
source venv/bin/activate
pip freeze > requirements.txt

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

pytest tests/

uvicorn app.main:app --reload




docker build -t fastapi_template_database -f DockerfilePostgreSQL .
docker run --name fastapi-template-databasecontainer -d -p 5432:5432 fastapi_template_database


docker build -t fastapi-template .
docker run -d --name fastapi_template_container -p 8000:8000 fastapi-template

python script/remove_pycache.py




```
fastapi-template
├─ .dockerignore
├─ .gitignore
├─ .pytest_cache
│  ├─ .gitignore
│  ├─ CACHEDIR.TAG
│  ├─ README.md
│  └─ v
│     └─ cache
│        ├─ lastfailed
│        ├─ nodeids
│        └─ stepwise
├─ .vscode
│  └─ launch.json
├─ Dockerfile
├─ DockerfilePostgreSQL
├─ README.md
├─ alembic
│  ├─ README
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
│     └─ 104bf085f88c_initial_migration.py
├─ alembic.ini
├─ app
│  ├─ api
│  │  └─ v1
│  │     ├─ auth.py
│  │     ├─ content.py
│  │     └─ users.py
│  ├─ core
│  │  ├─ config.py
│  │  ├─ constants.py
│  │  ├─ dependencies.py
│  │  ├─ events.py
│  │  ├─ exceptions.py
│  │  ├─ middleware.py
│  │  ├─ security.py
│  │  └─ settings.py
│  ├─ db
│  │  ├─ base.py
│  │  ├─ models
│  │  │  ├─ content.py
│  │  │  └─ user.py
│  │  └─ session.py
│  ├─ main.py
│  ├─ repositories
│  │  ├─ content.py
│  │  └─ user.py
│  ├─ schemas
│  │  ├─ auth.py
│  │  ├─ content.py
│  │  ├─ token.py
│  │  └─ user.py
│  └─ services
│     ├─ auth.py
│     ├─ content.py
│     └─ user.py
├─ requirements.txt
├─ script
│  └─ remove_pycache.py
└─ tests
   ├─ conftest.py
   ├─ test_auth.py
   ├─ test_content.py
   ├─ test_repositories.py
   ├─ test_services.py
   └─ test_users.py

```