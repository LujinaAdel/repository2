from  k import person
class TeamLeader(person):
    def details(self):
        original_details = super().details()
        
        if self.age >= 20:
            if self.gender == "female":
                return f"Hello Mrs {self.name} ,{original_details}"
            else:
                return f"Hello M. {self.name} ,{original_details}"
        else:
            return original_details


if __name__ == "__main__":
    team_members = []  
    leader0 = TeamLeader ("Ahmed Mohamed ", "Male", 25, "Backend Developer" , team_members)
    print(leader0.details())
    leader = TeamLeader("Lujina Adel", "female", 20, "Backend Developer", team_members)
    print(leader.details())
    leader1 = TeamLeader("Moaz waleed", "Male", 25, "Backend Developer", team_members)
    print(leader1.details())
    leader2 = TeamLeader("Hana", "female", 15, "Backend Developer", team_members)
    print(leader2.details())

