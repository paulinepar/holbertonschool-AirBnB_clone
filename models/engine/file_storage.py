#!/usr/bin/python3
""" Doc """

import json


class FileStorage:
    """ class who serialize and deserialize """

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
        
    def new(self, obj):
        """ adds the instance of an object to the dictionary """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ cette méthode sérialise le dictionnaire __objects et l'enregistre dans le fichier JSON """
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            file.write(json.dumps(FileStorage.__objects))
        print("[FileStorage] File saved")

            
    def reload(self):
        """ cette méthode désérialise le fichier JSON pour créer des instances d'objets. """
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
                data = file.read()
                FileStorage.__objects = json.loads(data)
                return json.loads(FileStorage.__objects)
        except:
            return {};
