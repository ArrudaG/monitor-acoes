import json
import os

class EstadoService:
    def __init__(self, file_path="estado.json"):
        self.file_path = file_path

    def carregar_estado(self):

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                return json.load(f)

        return {}


    def salvar_estado(self, alertas):

        with open(self.file_path, "w") as f:
            json.dump(alertas, f, indent=2)
