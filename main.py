from termcolor import colored as c
from os import system as s

def logo():
  print(c("██████╗ ███╗   ███╗██╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ", "red"))
  print(c("██╔══██╗████╗ ████║██║    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗", "yellow"))
  print(c("██████╔╝██╔████╔██║██║    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝", "green"))
  print(c("██╔══██╗██║╚██╔╝██║██║    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗", "cyan"))
  print(c("██████╔╝██║ ╚═╝ ██║██║    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║", "blue"))
  print(c("╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝", "magenta"))

logo()
weightLbs = int(input("Input Weight in lbs: "))
weightKg = weightLbs/2.205

heightFeet = int(input("\nInput Height in ft: "))
heightIn = int(input("Input Height in in: "))

inches = heightFeet*12 + heightIn
heightMeters = inches/39.37

BMI = weightKg/heightMeters**2
BMI = round(BMI, 2)
s("clear")

logo()
if BMI < 18.5:
  print("Your BMI is: "+str(BMI)+c(" (Underweight)", "blue"))

elif BMI > 18.5 and BMI < 24.9:
  print("Your BMI is: "+str(BMI)+c(" (Normal)", "green"))

elif BMI > 25 and BMI < 29.9:
  print("Your BMI is: "+str(BMI)+c(" (Overweight)", "yellow"))

elif BMI > 30 and BMI < 34.9:
  print("Your BMI is: "+str(BMI)+c(" (Obese)", "red"))

elif BMI > 35 and BMI < 39.9:
  print("Your BMI is: "+str(BMI)+c(" (Severely Obese)", "blue"))

elif BMI >= 40:
  print("Your BMI is: "+str(BMI)+c(" (Morbidly Obese)", "magenta"))
