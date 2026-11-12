name= input("enter your real name")
gadget=input("enter your favorite gadget")

agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

print("name" , name, "-> type:", type(name))
print("gadget:", gadget, "-> type:",type(gadget))
print("agent number:",agent_number, "-> type", type(agent_number))
print("speed rating:", speed_rating, "-> type", type(speed_rating))
print("mission count:",mission_count,"-> type",type(mission_count))
print("height (m):",height_m,"-> type",type(height_m))
print("is active:", is_active,"-> type", type(is_active))

agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print("agent number as text:", agent_number_text, "-> type:", type (agent_number_text))
print("mission count as text:", mission_count_text, "-> type:", type(mission_count_text))
