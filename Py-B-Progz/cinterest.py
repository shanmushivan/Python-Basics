
principle = float (input("Enter the Principle Amount: "))
rate = float (input("Enter the rate of interest: "))
time = float (input("Enter the time period: "))
CI = principle * (pow((1 + rate / 100), time))
print ("Compound interest is",CI)