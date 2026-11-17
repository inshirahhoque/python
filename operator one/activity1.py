# ==========================================
# farm harvest calculator
# ==========================================

# --- assignment operator (=) --- 
# store the harvest in kg from each of the 5 fields 
field1 = 120
field2 = 85
field3 = 150
field4 = 95 
field5 = 110 

# --- arithmetic operators (=, -, *, /) --- 
# calculate total calculate total and avrage harvest 
total   = field1 + field2 + field3 + field4 + field5 
average = total / 5  

print("total harvest     :", total, "kg")
print("average per field :", average, "kg")

# price per kg is 15 rupees - calculate total earnings 
price_per_kg = 15
earnings = total * price_per_kg 
print("total earnings       : rs.", earnings)

# --- floor division (//) and modulus (%) --- 
# pack the harvest into bags of 25 kg each 
bags     = total // 25
leftover = total % 25 

print("full bags packed   :", bags)
print("leftover grain     :", leftover, "kg") 

# --- comparison operators (>, <, ==< >=)--- 
# compare this year's harvest with last year 
last_year = 500
print("better that last year?  :", total > last_year)
print("same as last year?        :", total == last_year)
print("at least as good?        :", total >= last_year)

# --- assignment operators (+=, -=) ---
# a bonus field adds 30 kg to the total 
total += 30 
print("after bonus crop :", total, "kg")

# subtract 15 kg saved as seeds for next season
total -= 15
print("after seed reserve  :", total, "kg")

# final bag count after all adjustments 
bags = total // 25 

print("final bags packed  :", bags)





