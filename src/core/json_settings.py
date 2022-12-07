# Importamos las librerías
from src.core.libraries import json,os

# Configuraciones de la App
class Settings(object):
    json_file = "src/core/settings.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"settings.json\" not found! check in the folder {settings_path}")
        