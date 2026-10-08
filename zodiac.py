def run():
  year = int(input("Enter your birth year: "))
  zodiac_list = ("Monkey", "Rooster", "Dog", "Pig", "Rat",
  "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat")
  zodiac = (year - 1900) % 12
  print(f"Your Chinese zoidac sign is {zodiac_list[zodiac]}")

