python -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
uvicorn app.main:app --reload

docker build -t fastapi_template_database -f DockerfilePostgreSQL .
docker run --name fastapi-template-databasecontainer -d -p 5432:5432 fastapi_template_database


docker build -t fastapi-template .
docker run -d --name fastapi_template_container -p 8000:8000 fastapi-template


alembic revision --autogenerate -m "Initial migration"
alembic upgrade head