def run():
  year = int(input("Enter your birth year: "))
  zodiac_list = ("Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig")
  zodiac = (year - 1900) % 12
  print(f"Your Chinese zoidac sign is {zodiac_list[zodiac]}")

