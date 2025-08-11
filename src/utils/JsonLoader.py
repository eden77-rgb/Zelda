import json

class JsonLoader:
    def __init__(self, path):
        self.path = path
        self.data = None


    def load_json(self):
        with open(self.path, "r") as file:
            self.data = json.load(file)

            return self.data
