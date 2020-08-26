weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":         #converts str to uppercase then passes through function
    conv_weight = weight // 2.205
    print(f"You are: {conv_weight} kg.")
else:
    conv_weight = weight * 2.205
    print(f"You are: {conv_weight} lbs.")