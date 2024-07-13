from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all the models here to ensure they are registered properly
# def register_models():
#     from app.db.models.user import User
#     from app.db.models.content import Content

# register_models()