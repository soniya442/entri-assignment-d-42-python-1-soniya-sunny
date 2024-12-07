print("soniya")
print("ST12345")
print("soniya@example.com")
# Exercise 2
print("Soniya\nST12345\nsoniya@example.com")
# Exercise 3
num1=14
num2=7
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}/{num2}={num1/num2}")

# Exercise 4
i =1
while i< 6:
    print(i)
    i=i+1

# Exercise 5
print("\"SDK\"stands for\"software development kit\" , "
      "whereas\"IDE\"stands for \"integrated development environment\".")
# Exercise 6
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")  # Octal ASCII code
print("\x65")  # Hexadecimal ASCII code
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")
# Exercise 7
num = 23
textnum = "57"
decimal = 98.3
print(type(num))
print(type(textnum))
print(type(decimal))
total_sum = num + int(textnum) + decimal
print("Sum:", total_sum)
print("Data type of sum:", type(total_sum))
# Exercise 8
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

# Calculating total minutes in a year
total_minutes = days_in_year * hours_in_day * minutes_in_hour
print(f"There are {total_minutes} minutes in a year.")
# Exercise 9
name ="soniya"
print(f"Hi {name}, welcome to Python programming :)")
# Exercise 10
# Save as PoundsToDollars.py
pounds = float(333)
conversion_rate = 1.3  # Example conversion rate
dollars = pounds * conversion_rate
print(f"£{pounds} are ${dollars:.2f}")









