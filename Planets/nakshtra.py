# Defining the list of nakshtra

constellation = ["Ashwini", "Bharani" , "Kritika" , "Rohini" , "Mrigashira" , "Ardra" , "Punarvasu", "Pushya", "Ashlesha",
            "Magha" , "Purva Falguni" , "Uttara Falguni" , "Hasta" , "Chitra" , "Swati" , "Vishakha", "Anuradha", "Jyeshtha",
            "Mool", "Purva Ashadha" , "Uttara Ashadha" , "Shravan" , "Dhanishta" , "Shatbhisha" , "Purva Bhadrapad" , "Uttara Bhadrapada",
            "Revati"]

class nakshtra:
    def __init__(self, name, grah, yoni, gan, nadi):
        self.name = name
        self.yoni = yoni
        self.gana = gan
        self.nadi = nadi

n1 = nakshtra("Ashwini", "Ketu", "Ashwa", "Dev", "Aadi")
n2 = nakshtra("Bharani", "Shukra", "Gaja", "Manushya", "Madhya")
n3 = nakshtra("Kritika" , "Surya", "Medha", "Rakshas", "Anatya")
n4 = nakshtra("Rohini" , "Chandra", "Sarp", "Manushya", "Anatya")
n5 = nakshtra("Mrigshira", "Mangal", "Sarp", "Dev", "Madhya")
n6 = nakshtra("Ardra", "Rahu", "Shwan", "Manushya", "Aadi")
n7 = nakshtra("Punarvasu", "Guru", "Marjar" , "Dev", "Aadi")
n8 = nakshtra("Pushya", "Shani", "Medha", "Dev", "Madhya")
n9 = nakshtra("Ashlesha", "Budh" , "Marjar", "Rakshas", "Madhya")
n10 = nakshtra("")


