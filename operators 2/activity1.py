print("=== smart school day planner ===")

day = input("what day is it today?")
weather = input("what is the weather like today?")
homework = input("do you have homework today?")

print(f"=== your plan for {day} ===")

if day in ("saturday", "sunday"):
    print("day type: weeknend - enjoy your free time!")
elif day == "monday": 
    print("day type   : first day of the week. pack your weekly planner.")
elif day == "friday": 
    print("day type  : last school day. return library books today.")
elif day in ("tuesday", "wednesday", "thurday"):
    print("day type    : regular school day. stay focused!")
else:
    print("day type    : day not reconized. please check the spelling.")

if weather == "rainy" or weather == "cloudy":
    print("weather tip : pack your umbrella - it may get wet outside.")

if not (homework == "yes"):
    print("homework   : not done yet. finish it before going out!") 

if weather ==  "sunny" and homework == "yes":
    print("after school: head to the park - great weather and homework is done!")

if weather == "rainy" and not (homework == "yes"):
   print("best plan  : stay in, finish homework, then watch your favorite show.")
elif weather == "sunny" and homework == "yes" and not day in ("saturday", "sunday"):
   print("best plan   : all set for a great school day - you are prepared!")
elif day in ("saturday",  "sunday") and weather == "sunny":
    print("best plan   : perfect weekend weather - head outside and have fun!")
else:
    print("best plan  : take it one step at a time - you have got this!")



