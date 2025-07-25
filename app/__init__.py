"""
Archivo de inicialización de la aplicación Flask.
"""
from flask import Flask, render_template
from config import Config
from app.routes import main

def create_app():
    """
    Función para crear y configurar la aplicación Flask.
    """
    # Crear la instancia de Flask
    app = Flask(__name__)

    # Cargar configuración desde config.py
    app.config.from_object(Config)

    # Registrar las rutas (blueprints en aplicaciones más grandes)
    app.register_blueprint(main)

    # Configurar manejo de errores personalizado
    @app.errorhandler(404)
    def not_found_error(error):
        """
        Maneja errores 404 (página no encontrada)
        """
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        """
        Maneja errores 500 (error interno del servidor)
        """
        return render_template('500.html'), 500

    return app
