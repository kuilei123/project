
from .category import cat

def dog_blueprint(app):
    app.register_blueprint(cat)