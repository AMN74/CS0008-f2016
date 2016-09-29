# print("\t\t\t\tUSC\t \tDistance\t")
# print("Distance ______________:")
# print("Gas ___________________:")
# print("Consumption ___________:")
# print("Gas Consumption Rating :")


x = (input("Would you like to use USC or Metric?")) #Asks the user if their values are in USC or metric
y = float(input("What is the distance driven?")) #Asks the user how far they drove
z = float(input("How much gas is used?")) # Asks the user how much gas was used for the distance traveled

a = y * 1.60934  # miles --> Kilometers
b = z * 3.78541  # gal --> liters

c = y * .621371  # kilometers --> miles
d = z * .264172  # liters --> gallons

cm = (b / a) * 100 # This is the cm value if the user inputs values in USC
cm2 = (z / y) * 100 # This is the cm value if the user inputs values in metric

#The following is a conditional statement. This will run if the user inputs a 1 value indicating that their values are in USC
if x == "USC":
    print("\t\t\t\t\t\t\t\tUSC\t \t\tDistance\t")
    print("Distance ______________:     ", format(y, ',.3f'), "miles\t", format(a, ',.3f'), "Km")
    print("Gas ___________________:     ", format(z, ',.3f'), "gallons\t", format(b, ',.3f'), "liters")
    print("Consumption ___________:     ", format(y / z, ',.3f'), "mpg\t\t", format(cm, ',.3f'), " 1/100km")
#This is another conditional statement. This will run if the user inputs a 2 value indicating that their values are in metric.
elif x == "Metric":
    print("\t\t\t\t\t\t\t\tUSC\t \t\tDistance\t")
    print("Distance ______________:     ", format(c, ',.3f'), "miles\t", format(y, ',.3f'), "Km")
    print("Gas ___________________:     ", format(d, ',.3f'), "gallons\t", format(z, ',.3f'), "liters")
    print("Consumption ___________:     ", format(c / d, ',.3f'), "mpg",format(cm2, ',.3f'), " 1/100km")
#This is what will run if the user inputs an unrecognizable value
else:
    print("ERROR:Input either USC or Metric")
#The following condititonal statements indicate what should be outputed for the given input value

if cm > 20:
    print("Gas Consumption Rating : Extremely Poor")
if 15 < cm <= 20:
    print("Gas Consumption Rating : Poor")
if 10 < cm <= 15:
    print("Gas Consumption Rating : Average")
if 8 < cm <= 10:
    print("Gas Consumption Rating : Good")
if cm <= 8:
    print("Gas Consumption Rating : Excellent")



