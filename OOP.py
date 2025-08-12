# class member:
#     def __init__(self):
#         print("new member has been added")

# member_one =member()
# member_two = member()
# member_three =member()
# print(member_one.__class__)

# class member:
#     def __init__(self, first_name , middle_name , last_name ,gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
 
#     def full_name(self):
#         return f"{self.fname} {self.mname} {self.lname}"
    
#     def name_with_tittle(self):
#         if self .gender == "Male":
#             return f"hello Mr {self .fname}"
#         elif self.gender =="female":
#          return f"hello Mrs {self .fname}"
#         else:
#             return f"{self.fname}"
        
#     def get_all_info(self):
#         return f"{self.name_with_tittle()}, your full name is : {self.full_name()}"
    

# member_one =member("osama", "Mohammed" , "Ibrahim" , "Male")
# member_two = member("logy" , "lujina" , "rose" , "female")
# member_three =member("Mostafa", "Konafa" , "Moaz" , "Male")

# # print(member_two .fname , member_one .mname , member_three . lname)
 
# print(member_one .full_name())
# print(member_two.name_with_tittle())
# print(member_one.get_all_info())