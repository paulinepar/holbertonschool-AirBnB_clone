#!/usr/bin/python3
""" Doc """

import json


class FileStorage:
    """ class who serialize and deserialize """

    __file_path = "file.json"
    __objects = {}

    def get(self, id):
        return self.all().get(id)
    
    def all(self):
        return FileStorage.__objects
    
    def destroy(self, id):
        if FileStorage.__objects.get(id):
            del FileStorage.__objects[id]
            self.save()
            return True
        return False
        
    def new(self, obj):
        """ adds the instance of an object to the dictionary """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ cette méthode sérialise le dictionnaire __objects et l'enregistre dans le fichier JSON """
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            d = {}
            for k, v in FileStorage.__objects.items():
                d[k] = v.to_dict()
            file.write(json.dumps(d))

            
    def reload(self):
        """ cette méthode désérialise le fichier JSON pour créer des instances d'objets. """
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.amenity import Amenity

        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
                data = json.loads(file.read())
                for k in data.keys(): 
                    v = data[k]
                    FileStorage.__objects[k] = BaseModel(**v)

                return FileStorage.__objects
        except:
            return {}