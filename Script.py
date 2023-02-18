user_input = input("Mile:")
Mile = user_input

if user_input.isdigit():
    KM = float(Mile) * 1.609344
    print(f"KM: {KM}")

else:
    print("Invalid Mile value, please insert a valid number")