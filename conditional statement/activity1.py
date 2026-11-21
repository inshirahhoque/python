# part 1: ask for todays temperature
temperature = int(input("enter today's temperature in celsius: "))

# part 2: decide between a jacket and a t-shirt
if temperature < 20:
    outfit = "jacket"
    print("it is cold today.")
    print("wear a", outfit)
else:
    outfit = "t-shirt"
    print("it is warm today.")
    print("wear a", outfit)

#part 3: ask whether it is raining
is_raining = input("is it raining today? (yes/no): ")

# part 4: add an umbrella reminder only if its raining
if is_raining == "yes" :
    print("bring an umbrella!")

# part 5: ask for the wind speed 
wind_speed = int(input("enter the wind speed in km/h: "))

# part 6: decide whether a windbreaker is needed
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("it is windy today.")
    print("wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("it is calm today.")
    print("no windbreaker needed over your", outfit)
          
 # part 7: ask whether there are puddles on the ground
has_puddles = input("are there puddles on the ground? (yes/no): ")

# part 8: decide between boots and sneakers
if has_puddles == "yes":
    shoes = "boots"
    print("the ground is wet.")
    print("wear", shoes)
else:
    shoes = "sneakers"
    print("the ground is dry.")
    print("wear", shoes)

# part 9: this message always prints, no matter what was chosen above
print("")
print("weather check complete!")



                        
  

