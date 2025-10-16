preciple_amount = float(input("Enter Principle Amount ? "))
how_menay_years = int(input("Enter How Menay Years ?"))
presentage      = float(input("Enter Presentage Per Years"))

if preciple_amount != 0 and how_menay_years !=0 and presentage !=0 :
   interest_for_no_of_years = preciple_amount * (presentage / 100) * how_menay_years
   print(f"Total Interest : {interest_for_no_of_years}")

else:
    print("Something Went Wrong")
