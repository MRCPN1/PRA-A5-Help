import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
import os
from datetime import datetime
from datetime import timedelta

os.system("cls") #Deze regel nog invullen! Hoe maak je het scherm leeg?
print("Working...")

data = pd.read_excel("Volleybal_Topdivisie_tussenstand.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
data = data.sort_values("datum")


#Informatievraag 1
totaloffence = data["overtredingen"].sum()
print(totaloffence)



#Informatievraag 2
averageViolations=data["overtredingen"].mean()
print(averageViolations)



#Informatievraag 3
zwartBoek =  data_sorted=data.sort_values("overtredingen", ascending=False) 
top5=data_sorted.head(5)
file3 = open("zwartboek.txt", "w", encoding="UTF-8")
file3.write(bamboo.prettify(top5, type="zwartboek"))
print(top5)



#Informatievraag 4
filter = (data["overtredingen"] <2)
data_filtered = data[filter]
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
filter = (data["datum"] > (datetime.now()) - timedelta(days=15))
data_filtered2 = data[filter]
os.system("cls")
top21 = data_filtered.head((data_filtered2["overtredingen"].count()))
file4 = open("eregalerij.txt", "w", encoding="UTF-8")
file4.write(bamboo.prettify(top21, type="eregalerij"))
print(top21)















print("Done!")
