# Author        : Peter Hall
# Date Created  : 20/03/2021
# Description   : Calculates an individual's fortnightly tax amount based on the ATO's Resident tax rates for 2020-21.

print("ATO INDIVIDUAL FORNIGHTLY TAX CALUATOR \n")

while True:
    try:
        income = round(float(input("Enter your taxable income for the fortnight: ")),2)
    except ValueError:
        print("Invalid entry. Please enter your fortnight taxble income. For example, 2100.55")
        continue
    else:
        if income >= 0: # Check for positive number
            break

yearlyIncome = income * 26

# Calculate tax
if 0 <= yearlyIncome <= 18200:
    tax = 0

elif 18201 <= yearlyIncome <= 45000:
    tax = (yearlyIncome - 18200) * 0.19

elif 45001 <= yearlyIncome <= 120000:
    tax = (yearlyIncome - 45000) * 0.325 + 5092

elif 120001 <= yearlyIncome <= 180000:
    tax = (yearlyIncome - 120000) * 0.37 + 29467

else:
    tax = (yearlyIncome - 180000) * 0.45 + 51667

tax = round((tax/26),2)
net = round((income - tax),2)
print("Tax     : $", tax);
print("Net Pay : $", net)
k  = input("Press any key to exit")