#Grah aur unke vichaar

#Importing the OS variables
import os
# Clearing the screen
os.system('clear')

print ("This will print the planets and their constellations.")
print ("The name of planets are : ")
print ("Surya, Mangal, Guru, Budh, Shukra, Shani, Rahu, Ketu")

# Defining the rashi
rashi = {
    1 : "Mesh",
    2 : "Vrishabh",
    3 : "Mithun",
    4 : "Kark",
    5 : "Singh",
    6 : "Kanya",
    7 : "Tula",
    8 : "Vrishchik",
    9 : "Dhanu",
    10 : "Makar",
    11 : "Kumbh",
    12 : "Meen"
}

# Defining grah and their rashi
grah_rashi = {
    "Surya" : "Singh",
    "Chandra" : "Kark",
    "Mangal" : "Mesh, Vrishchik",
    "Shukra" : "Vrishabh, Tula",
    "Guru" : "Dhanu, Meen",
    "Budh" : "Mithun, Kanya",
    "Shani" : "Makar, Kumbh",
    "Rahu" : "Kanya",
    "Ketu" : "Meen"
}

# Defining Ucch 
uchch = {
    "Surya" : "Mesh",
    "Chandra" : "Vrishabh",
    "Mangal" : "Makar",
    "Guru" : "Kark",
    "Budh" : "Kanya",
    "Shukra" : "Meen",
    "Shani" : "Tula",
    "Rahu" : "Mithun",
    "Ketu" : "Dhanu"
}

# Defining neech
neech = {
    "Surya" : "Tula",
    "Chandra" : "Vrishchik",
    "Mangal" : "Kark",
    "Guru" : "Makar",
    "Budh" : "Meen",
    "Shukra" : "Kanya",
    "Shani" : "Mesh",
    "Rahu" : "Dhanu",
    "Ketu" : "Meen"
}

# Defining nakshatra
nakshtra = {
    "Surya" : "Kritikka, Uttarafalguni, Uttarashadha",
    "Chandra" : "Rohini, Hasta, Shravana",
    "Mangal" : "Mrigashira, Chitra, Dhanishta",
    "Guru" : "Punarvasu, Vishakha, Purvabhadrapad",
    "Budh" : "Aashlesha, Jayeshtha, Revati",
    "Shukra" : "Bharani, Purvafalguni, Purvashadha",
    "Rahu" : "Ardra, Swati, Shatbhisha",
    "Ketu" : "Ashwini, Magha, Mool"
}

x=str(input("Enter the graha name to get the information : "))
print("Rashi \t:---> ", grah_rashi[x])
print("Nakshtra :---> ", nakshtra[x])
print("Uchch \t:---> ", uchch[x])
print("Neech \t:---> ", neech[x])
