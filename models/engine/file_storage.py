#!/usr/bin/python3
"""Defines the FileStorage class.
"""
import json
import os.path


class FileStorage:
    """Class FileStorage - serializes instances to a JSON file and
       deserializes JSON file to instances
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        class_dict = {'BaseModel': BaseModel, 'User': User,
                      'Amenity': Amenity, 'City': City,
                      'Place': Place, 'Review': Review,
                      'State': State}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r',) as f:
                for key, value in json.load(f).items():
                    self.new(class_dict[value["__class__"]](**value))
