def run():
    day = 0
    print("Is your birthday in this set?(y/n)")
    print(
        "Set 1: 1, 3, 5, 7, 9, 11, 13, 15, 17, "
        "19, 21, 23, 25, 27, 29, 31"
        )
    answer = input("Type y for yes, n for no. ")
    if answer == "y":
        day+= 1
    print("Is your birthday in this set?(y/n)")
    print(
        "Set 2: 2, 3, 6, 7, 10, 11, 14, 15, 18, 19, "
        "22, 23, 26, 27, 30, 31"
        )
    answer = input("Type y for yes, n for no. ")
    if answer == "y":
        day+= 2
    print("Is your birthday in this set?(y/n)")
    print(
        "Set 3: 4, 5, 6, 7, 12, 13, 14, 15, 20, 21, "
        "22, 23, 28, 29, 30, 31"
        )
    answer = input("Type y for yes, n for no. ")
    if answer == "y":
        day+= 4
    print("Is your birthday in this set?(y/n)")
    print(
    "Set 4: 8, 9, 10, 11, 12, 13, 14, 15, 24, 25, "
    "26, 27, 28, 29, 30, 31 "
    )
    answer = input("Type y for yes, n for no. ")
    if answer == "y":
        day+= 8
    print("Is your birthday in this set?(y/n)")
    print(
    "Set 5: 16, 17, 18, 19, 20, 21, 22, 23, 24, "
    "25, 26, 27, 28, 29, 30, 31"
    )
    answer = input("Type y for yes, n for no. ")
    if answer == "y":
        day+= 16
    print(f"Your birthday is {day}!")
    
    
        
    