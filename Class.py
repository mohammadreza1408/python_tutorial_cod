


# class Car:
#     def __init__(self,c,maxSpeed,model):
#         self.color = c
#         self.max_speed = maxSpeed
#         self.model= model
#     def horn(self):
#         print("beep")

class Car2:
    number_of_weels=4
    def __init__(self,color,model):
        self.color=color
        self.model = model
    def info(self):
        print("color:", self.color)
        print("model:",self.model)
        print("Number of wheels:",self.number_of_weels)





nilofar = Car2("sefid","x4")
amirAli = Car2("meshki","206")
amin = Car2("sabx","111")
print(nilofar.number_of_weels)
print(amirAli.number_of_weels)
print(amin.number_of_weels)

print(nilofar.color)
print(amirAli.color)
print(amin.color)

nilofar.number_of_weels=5
print(nilofar.number_of_weels)
print(amirAli.number_of_weels)
