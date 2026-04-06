fruit_name = " PAPAGAYA PROLIFIA "
fruit_name = fruit_name.strip(" ")
fruit_price = "20$"
euro_price = fruit_price.replace("$", "€")
print(f"The {fruit_name.title()} costs about {fruit_price} or {euro_price}")
print(fruit_name.count("L"))
