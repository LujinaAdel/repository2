class Person:
    def __init__(self, name, gender, age, job, position="Employee"):
        self.name = name
        self.gender = gender
        self.age = age
        self.job = job
        self.position = position

    def details(self):
        return f"Name: {self.name}\nGender: {self.gender}\nAge: {self.age}\nJob: {self.job}\nPosition: {self.position}"


class Employees(Person):
    def __init__(self, name, gender, age, job):
        super().__init__(name, gender, age, job, position="Employee")


class TeamLeader(Employees):
    def __init__(self, name, gender, age, job, team_members):
        super().__init__(name, gender, age, job)
        self.team_members = team_members
        self.position = "Team Leader"

def details(self):
    return f"{super().details()}Team Members:{(self.team_members)}"


Ahmed = Person("Ahmed Mohamed", "Male", 16, "Backend Developer", "Employee")
nour = Employees("Nour Ibrahim", "Male", 16, "Backend Developer")
hana = Employees("Hana", "Female", 15, "Backend Developer")
moaz = Employees("Moaz Waleed", "Male", 16, "Backend Developer")

lujina = TeamLeader("Lujina Adel", "Female", 16, "Backend Developer", [Ahmed, nour, hana, moaz])

print("Person Details:")
print(Ahmed.details())

print("\nEmployees Details:")
print(nour.details())
print(hana.details())
print(moaz.details())

print("\nTeam Leader Details:")
print(lujina.details())
