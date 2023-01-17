"""
Complete the script.
"""

print('Hello!')
name = input("What is your name?: ")

print()
print("Hello " + name + "! Let me tell you about the stats of my basketball team!")
print()

player = input("Pick a player from the following: Cora, Paisley, or Elle: ")
print()

if player == "Cora":
    print("Cora had 59 points this season.")
elif player =="Paisley":
    print("Paisley had 49 points this season.")
elif player == "Elle":
    print("Elle had 70 points this season.")

print()
print("Now let's discuss the stats of your basketball team.")

#Part 1 - get points scored from the user.

player_1_points = int(input('How many points did your first player score this season?: '))
player_2_points = int(input("How many points did your second player score this season?: "))
player_3_points = int(input("How many points did your third player score this season?: "))

type(player_1_points)
type(player_2_points)
type(player_3_points)

player_1_points = float(player_1_points)
player_2_points = float(player_2_points)
player_3_points = float(player_3_points)

#Part 2 - finding the sum, average, product, smallest, largest and range of my data.

#Finding the least amount of points scored
least_amount_of_points = min(player_1_points, player_2_points, player_3_points)

print()
print("The lowest scoring player scored", least_amount_of_points, "points.")

#Finding the most amount of points scored
most_amount_of_points =max(player_1_points,player_2_points,player_3_points)

print("The highest scoring player scored", most_amount_of_points, "points.")

#Finding the sum of points scored
sum_of_points = total = player_1_points + player_2_points + player_3_points
print("Together, your players scored a total of", sum_of_points, "points.")

#Finding the average points scored
average_points = (player_1_points + player_2_points + player_3_points)/3
average_points = round(average_points, 1)
print("The average points of your three players is", average_points, "points.")

#Finding the product of points scored
product_of_points = player_1_points * player_2_points * player_3_points
print ("The product of your players' points is", product_of_points, "points.")

#Finding the range of points scored
range_of_points = (most_amount_of_points - least_amount_of_points)
print("The range of your players' points is", range_of_points, "points.")
print()

#Part 3 Decision-making
if player_1_points < average_points:
    print("Your first player is below the average. They need an extra practice!")
if player_1_points == average_points:
    print("Your first player is average. Let them decide if they want to attend extra practice.")
if player_1_points > average_points:
    print("Your first player is above the average. They get to skip extra practice!")
print()

if player_2_points < average_points:
    print("Your second player is below the average. They need an extra practice!")
if player_2_points == average_points:
    print("Your second player is average. Let them decide if they want to attend extra practice.")
if player_2_points > average_points:
    print( "You're second player is above the average. They get to skip extra practice!")
print()

if player_3_points < average_points:
    print("Your third player is below the average. They need an extra practice!")
if player_3_points == average_points:
    print("Your third player is average. Let them decide if they want to attend extra practice.")
if player_3_points > average_points:
    print("Your third player is above the average. They get to skip extra practice!")


 

