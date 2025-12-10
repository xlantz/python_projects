import math

#F to C = (5/9)(F-32)
def FToC(temp):
    Celcius = (5/9)*(temp-32)
    print(f"It's {round(Celcius,2)} degrees C.")
    
#C to F = (C*(9/5)+32)
def CToF(temp):
    Faren = (temp*(9/5)+32)
    print(f"It's {round(Faren,2)} degrees F.")


temp = float(input("Please enter in a degree: \n"))
degree = input("Please enter if it's Farenheight (F) or Celcius (C): \n").upper()

if degree == "F":
    FToC(temp)
elif degree == "C":
    CToF(temp)