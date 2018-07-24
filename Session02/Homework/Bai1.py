mass=int(input("Please enter your weight in kg: "))
height=int(input("Please enter your height in cm: "))
BMI=(mass/(height/100))/(height/100)
if BMI<16:
    print("You are severely underweight.")
elif 16<BMI<18.5:
    print("You are underweight.")
elif 18.5<BMI<25:
    print("You are normal.")
elif 25<BMI<30:
    print("You are overweight.")
else:
    print("You are obese.")
