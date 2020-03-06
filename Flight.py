# Lists that contain the locations and the prices of said locations
# List that contain the departure locations and the prices of said departure locations
# List that contain the accomodation locations and the prices of said accomadation locations per night

Locations = [["Sydney", 326], ["Tonga", 378], ["Shanghai", 1436], ["London", 2376]]
Departures = [["Christchurch", 75], ["Wellington", 50], ["Auckland", 0]]
Accomadation = [["Sydney", 120], ["Tonga", 40], ["Shanghai", 60], ["London", 80]]

# The total price in which the amount that the user will have to pay.
# Consists of Location they are flying to, there departure location, and their accomodation prices

Total_Price = 0


print("Welcome to the flight calculator, please answer the questions below acurately")

# Using my own style of loop with the puprose of printing only the names of the locations
# by using the value and the listno variable i can change the name of the city that is printed

value = 0
listno = 1
ask = True
while ask == True:
    if value == len(Locations):
        ask = False
    else:
        print(listno, ":", Locations[value][0])
        value+=1
        listno+=1

# Input by the user stored in a variable.  The stored information is the number of the country that they selected

destination = int(input("Where will you be travelling to? (Please answer with the nunmber of the country)"))
destination-=1
Total_Price+= (Locations[destination][1])


# Same type of loop with different variable names

departure_value = 0
departure_no = 1
loop = True
while loop == True:
    if departure_value == len(Departures):
        loop = False
    else:
        print(departure_no, ":", Departures[departure_value][0])
        departure_value+=1
        departure_no+=1

departure = int(input("Where are you departing from? (Please answer with the number of the city)"))
departure-=1
Total_Price+= (Departures[departure][1])


# This part of the code gets the price of the accomodation and multiplies it by how many nights they are staying
# This price then gets added to the total price which already consists of the cost of the flights

stay = int(input("How many nights are you staying?"))
Total_Stay = stay*(Accomadation[destination][1])
Total_Price+= Total_Stay

# Final message that tells the user how much the flights and accomodation will cost

print("The total price you will be paying for the selected options is:", Total_Price, "NZD")