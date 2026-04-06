age = 13
has_ticket = True
pass_message = "Welcome onboard dear passenger!"
false_message = "You need a ticket first!"
adult_supervision_message = "You may not enter, you need adult supervision!"
if age >= 16 and has_ticket:
    print("*" * len(pass_message))
    print(pass_message)
    print("*" * len(pass_message))

elif age < 16 and has_ticket:
    print("*" * len(adult_supervision_message))
    print(adult_supervision_message)
    print("*" * len(adult_supervision_message))
else:
    print("*" * len(false_message))
    print(false_message)
    print("*" * len(false_message))
