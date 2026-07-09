print("Area Calculator")

print("1. Rectangle")
print("2. Triangle")

choice = int(input("Select a menu: "))

if choice == 1:
    width = float(input("Width: "))
    length = float(input("Length: "))
    area = width * length
    print("Area =", area)

elif choice == 2:
    base = float(input("Base length: "))
    height = float(input("Height: "))
    area = 0.5 * base * height
    print("Area =", area)

else:
    print("Invalid menu selection")
