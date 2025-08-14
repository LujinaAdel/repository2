class person:
    def __init__(self, name, gender, age, job, position="Employee"):
        self.name = name
        self.gender = gender
        self.age = age
        self.job = job
        self.position = position

    def details(self):
        return f"your Name: {self.name}\nthe gender: {self.gender}\nthe age: {self.age}\nyour job: {self.job}\nyour position: {self.position}"

class Employees(person):
    def __init__(self, name, gender, age, job):
        super().__init__(name, gender, age, job, position="Employee")
        self.position = "Employee"

    def details(self):
        return super().details()
    
class team_leader(Employees):
    def __init__(self, name, gender, age, job, team_members):
        super().__init__(name, gender, age, job)
        self.team_members = team_members
        self.position = "Team leader"
    
    def details(self):
        member = member
        return f"{super().details()}\nTeam Members: {member}"
    

Ahmed = person("Ahmed Mohamed", "Male", 16, "Backend developer", "Employee")

nour = Employees("Nour Ibrahim", "Male", 16, "Backend Developer")
hana = Employees("Hana", "Female", 15, "Backend Developer")
moaz = Employees("Moaz Waleed", "Male", 16, "Backend Developer")

lujina = team_leader("Lujina Adel", "Female", 16, "Backend Developer", [Ahmed, nour, hana, moaz])

print ("hello ! please write your informations:")
print (input("Name :"))
print (input("gender :"))
print (input("age :"))
print (input("job :"))
print (input("position :"))

("#" * 40)
print("Person Details:")
print(Ahmed.details())

print("Employees Details:")
print(nour.details())
print(hana.details())
print(moaz.details())

print("Team Leader Details:")
print(lujina.details())