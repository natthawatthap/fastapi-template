python -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
uvicorn app.main:app --reload