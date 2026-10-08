def run():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = round(weight / (height**2), 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you are normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are overweight.")
    else:
         print(f"Your BMI is {bmi}, you are obese.")
    