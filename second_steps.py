# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }
print(sat_database)

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database["GOES"] = 2000
sat_database["worldview"] = 0.31

print("I have the following satellites in my database:")
print(sat_database)

# 2) print out all satellite names contained in the dictionary [2P]
print(sat_database.keys())

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

answer = input ("Please name the satellite of which you want to know the resolution.")
    
if answer == "METEOSAT":
    print ("METEOSAT has a resolution of 3000 Meters.")
elif answer == "LANDSAT":
    print ("LANDSAT has a resolution of 30 Meters.")
elif answer == "MODIS":
    print ("MODIS has a resolution of 500 Meters.")
elif answer == "GOES":
    print ("GOES has a resolution of 2000 Meters.")
elif answer == "worldview":
    print ("worldview has a resolution of 0.31 Meters.")
else:
    print ("I can't find the satellite, you are searching for. Please check your spelling and note the case sensitivity. Also note that no spaces are allowed.")
        

# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

#I checked the task with all Satellites. The Conditional Case works just fine.
# Also I checked if an error message occurs if you missspell or enter Satellite names, that are not named in the Conditional Case.


# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 
# I already did in Task 3. 