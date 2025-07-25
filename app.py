"""
# app.py
# Punto de entrada de la aplicación DevBlog"""
import os
from app import create_app
from config import Config

# Crear la aplicación usando la factory function
app = create_app()

if __name__ == '__main__':
    """
    Punto de entrada de la aplicación
    
    ¿Qué hace if __name__ == '__main__'?
    - Solo se ejecuta si corres este archivo directamente
    - No se ejecuta si importas este archivo desde otro lugar
    - Patrón estándar en Python
    """

    #configuración para producción
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'

    print("Iniciando DevBlog...")
    # print(f"Servidor corriendo en: http://{Config.HOST}:{Config.PORT}")
    # print("Presiona Ctrl+C para detener el servidor")
    print(f"Puerto: {port}")
    print(f"Debug: {debug}")
    print(f"Entorno: {os.environ.get('FLASK_ENV', 'development')}")

    # Iniciar el servidor Flask
    app.run(
        # host=Config.HOST,      # 0.0.0.0 permite conexiones externas
        # port=Config.PORT,      # Puerto configurado (5000 por defecto)
        # debug=Config.DEBUG     # Modo debug para desarrollo
        host='0.0.0.0',      # 0.0.0.0 permite conexiones externas
        port=port,      # Puerto configurado (5000 por defecto)
        debug=debug     # Modo debug para desarrollo
    )
