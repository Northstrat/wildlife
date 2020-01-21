import json
import flask

class Mammal():
    def __init__(self,name, status):
        self.name = name
        self.status = status
    def serialize(self):
        return {
            "name":self.name,
            "status":self.status
        }

class Bird():
    def __init__(self,name, order, family, genus):
        self.name = name
        self.order = order
        self.family = family
        self.genus = genus
    def serialize(self):
        return {
            "name":self.name
        }

class Category():
    def __init__(self,name):
        self.category_name = name
        self.category_animals=[]
        self.desc = ""
    def addAnimal(self,animal):
        self.category_animals += [animal]
    def addDesc(self,desc):
        self.desc = desc
    def serialize(self):
        return {
            "category_name":self.category_name,
            "category_animals":[
                a.serialize() for a in self.category_animals
            ]
        }

class Animals():
    def __init__(self):
        self.birds = {}
        self.mammals = {}
    def addMammals(self,mammals):
        self.mammals = mammals
    def addBirds(self,birds):
        self.birds = birds
    def addMammal(self,category,mammal):
        if category not in self.mammals:
            self.mammals[category] = []
        self.mammals[category] += [mammal]
    def addBird(self,order, family, genus,bird):
        if order not in self.birds:
            self.birds[order] = {}
        if family not in self.birds[order]:
            self.birds[order][family] = {}
        if genus not in self.birds[order][family]:
            self.birds[order][family][genus] = []
        self.birds[order][family][genus] += [bird]
    def getMammals(self):
        return {
            c:[m.serialize() for m in self.mammals[c]] for c in self.mammals
        }
    def getBirds(self):
        return {
            o: {
                f: {
                    g: [
                        b.serialize() for b in self.birds[o][f][g]
                    ] for g in self.birds[o][f]
                } for f in self.birds[o]
            } for o in self.birds
        }