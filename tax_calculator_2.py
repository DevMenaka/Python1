income_per_year = float(input("Enter Your Monthly Income Amount : "))

if income_per_year <= 1200000:
    print("Your Tax Amount Is Zero 0.0 Rupees /=")

else:

    if 1200000 < income_per_year <= 1700000:
        print(f"Your Tax Amount Is: {(income_per_year - 1200000) * (6 / 100)}/= Rupees")

    elif 1700000 < income_per_year <= 2200000:
         print(f"Your Tax Amount Is : {(income_per_year - 1700000) * (12 /100) + 500000 * 6 / 100}/= Rupees")

    elif 2200000 < income_per_year <= 2700000:
         print(f"Your Tax Amount Is : {(income_per_year - 2200000) * (18 / 100) + (500000 * 12 / 100) + (500000 * 6 / 100)}/= Rupees")

    elif 2700000 < income_per_year <= 3200000:
         print(f"Your Tax Amount Is : {(income_per_year - 2700000) * (24 / 100) + (500000 * 18 / 100) + (500000 * 12 / 100) + (500000 * 6 / 100)}/= Rupees")

    elif 3200000 < income_per_year <= 3700000:
         print(f"Your Tax Amount Is : {(income_per_year - 3200000) * (30/100) + (500000 * 24 / 100) + (500000 * 18 / 100) + (500000 * 12 / 100) + (500000 * 6 /100)}/= Rupees")

    elif 3700000 < income_per_year :
        print(f"Your Tax Amount Is : {(income_per_year - 3700000) * (36 / 100) + (500000 * 30 / 100) + (500000 * 24 / 100) + (500000 * 18 / 100) + (500000 * 12 / 100) + (500000 * 6 /100)}/= Rupees")

    else:
        print("Something Went Wrong")