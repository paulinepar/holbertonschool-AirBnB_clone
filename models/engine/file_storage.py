#!/usr/bin/python3
""" Doc """

import json


class FileStorage:
    """ class who serialize and deserialize """

    def __init__(self):
        """ constructor """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
        
    def new(self, obj):
        """ adds the instance of an object to the dictionary """
        key = "{}.{}".format(type(self).__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ cette méthode sérialise le dictionnaire __objects et l'enregistre dans le fichier JSON """
        with open(self.__file_path, "w", encoding='utf-8') as file:
            file.write(json.dumps(self.__objects))
            
    
    def reload(self):
        """ cette méthode désérialise le fichier JSON pour créer des instances d'objets. """
        if not self.__file_path:
            return
        else:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                data = file.read()
            return json.loads(data)
