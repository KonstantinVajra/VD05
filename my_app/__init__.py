from flask import Flask

def create_app():
    app = Flask(__name__)

    # Импортируем маршруты
    from my_app.routes import main
    app.register_blueprint(main)  # Регистрируем маршруты

    return app

