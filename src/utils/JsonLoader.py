import json

class JsonLoader:
    def __init__(self, path):
        self.path = path
        self.data = None
        self.data_dict = {}


    def load_json(self):
        with open(self.path, "r") as file:
            self.data = json.load(file)

            return self.data


    def save_json(self, player, camera):
        self.data_dict["player"] = {
            "x": player.x,
            "y": player.y,
            "life": player.life,
            "max_life": player.max_life,
            "ruby": player.ruby
        }
        
        self.data_dict["camera"] = {
            "x": camera.x,
            "y": camera.y,
            "current_id": camera.current_id
        }
        
        with open(self.path, "w") as file:
            file.write(json.dumps(self.data_dict))

        print("Données sauvegarder")
