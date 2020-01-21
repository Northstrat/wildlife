import wikipedia
import json

print("Starting to download mammals")
mammals = wikipedia.page("List_of_mammals_of_Great_Britain")

class Mammal():
    def __init__(self,name, status):
        self.name = name
        self.status = status
    def __repr__(self):
        return self.status + ' : '+self.name
    def to_json(self):
        return json.dumps(self.__dict__)

class Category():
    def __init__(self,name):
        self.name = name
        self.animals=[]
        self.desc = ""
    def __repr__(self):
        return self.name + ":" + str(len(self.animals))
    def addAnimal(self,animal):
        self.animals += [animal]
    def addDesc(self,desc):
        self.desc = desc
    def printAll(self):
        print(self.name)
        print('\t' + self.desc)
        for a in self.animals:
            print('\t\t'+str(a))
    def to_json(self):
        return '{"category_name":"'+self.name+'","category_animals":'+\
        str([x.to_json() for x in self.animals]) +'}'

categories = {}

currCat = ""

blacklist = ['Genus','Subfamily','Suborder','Superfamily','Family','Superorder','Order','(Excluding ceta']
statuses = ['EX','EW','CR','EN','VU','NT','LC','DD']

for line in mammals.content.split('\n'):
    l = line.strip()
    if l == "":
        continue
    if l.startswith("=="):
        currCat = l.replace("== ","").replace(" ==","")
        continue
    for status in statuses:
        if status in l:
            animalName = l.split(',')[0]
            if currCat not in categories:
                categories[currCat] = Category(currCat)
                categories[currCat].addAnimal(Mammal(animalName,status))
            else:
                categories[currCat].addAnimal(Mammal(animalName, status))
            break

for c in categories:
    print(categories[c].to_json())
