def south_indian():
    print("\nSouth Indian Dishes")
    print("1. Idli")
    print("2. Dosa")
    print("3. Vada")
    print("4. Pongal")
    print("5. Upma")


def north_indian():
    print("\nNorth Indian Dishes")
    print("1. Butter Naan")
    print("2. Paneer Butter Masala")
    print("3. Chole Bhature")
    print("4. Dal Makhani")
    print("5. Jeera Rice")


def chinese():
    print("\nChinese Dishes")
    print("1. Fried Rice")
    print("2. Noodles")
    print("3. Manchurian")
    print("4. Spring Rolls")
    print("5. Momos")


def italian():
    print("\nItalian Dishes")
    print("1. Pizza")
    print("2. Pasta")
    print("3. Garlic Bread")
    print("4. Lasagna")
    print("5. Risotto")


def desserts():
    print("\nDesserts")
    print("1. Gulab Jamun")
    print("2. Ice Cream")
    print("3. Rasmalai")
    print("4. Brownie")
    print("5. Cake")


def menu(choice):
    match choice:
        case 1:
            south_indian()
        case 2:
            north_indian()
        case 3:
            chinese()
        case 4:
            italian()
        case 5:
            desserts()
        case _:
            print("Invalid choice entered")


def run_app():
    while True:
        print("\n========== FOOD MENU ==========")
        print("1. South Indian")
        print("2. North Indian")
        print("3. Chinese")
        print("4. Italian")
        print("5. Desserts")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 6:
            break

        menu(choice)

    print("Thank You! Visit Again.")


run_app()