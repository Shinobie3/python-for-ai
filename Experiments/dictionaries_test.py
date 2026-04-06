# person = { "name" : "Max", "age" : 15 , "occupation" : "student"}
# person["age"] = 15
# person["email"] = "masi@gmail.com"
# #del person["email"]
# #person.clear()
# person.update({"name" : "Malise", "age" : 13})
# print(f"{person.get("name")} is {person.get("age")} years old and currently works as a {person['occupation']}")
# if "email" in person:
#     print("Email found!")
#     print(f"Her email is: {person.get("email")}")

# print(person.keys())
# print(person.values())

# if person.get("name") == "Malise":
#     print("Malise I've found ya hehe")

passengers = {"Mr.Brown" : {"age" : 57, "ticket_valid" : False}, "Mr.Shakespeare" : {"age" : 176, "ticket_valid" : True}}
if passengers["Mr.Brown"]["ticket_valid"] == True:
    print("Welcome onboard, Mr.Brown!")
else:
    print("Sorry Mr.Brown but you need to buy a ticket first!")