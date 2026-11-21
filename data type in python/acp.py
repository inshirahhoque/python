# =============================================
# SCHOOL CLUB MEMBER BADGE 
# =============================================

# ---------- PART 1 : member details ----------
name = input("member name: ")
club = input("club name:  ") 

# ---------- PART 2 : data types ----------
member_number = 8
points = 9.5
is_active = true
print("memmber number:", member_number,"-> type:", type(member_number))
print("points:", points, "-> type:", type(points))
print("active:", is_active, "-> type:", type:", type(is_active))

# ---------- PART 3 : badge code ----------
badge_code = name[0:3] + club[-1:] + str(member_number)
print("badge code:", badge_code)

# ---------- PART 4 : final badge ----------
print("===== CLUB BADGE =====")
print("member: " + name)
print("club: " + club)
print("code: " + badge_code)
print("points: " + str(points) + " | active: " + str(is_active))

      