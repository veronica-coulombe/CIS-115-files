print("You're traveling the Solar System in your Space Ship.")

print("You have 4 options to choose where you land.")

print("Moon, Mars, Venus, or Pluto.")

where = input("Where is the Space Ship going? ")

#Moon
if where == "Moon":
    weight = float(input("How much does the spaceship weigh in kilos? "))
    rocksCollected = (input("Did you pick up any rocks to study? y/n "))
    if rocksCollected == "y":
        rocks = float(input("How many kilos of rocks did you collect? "))
        if weight:
            totalWeight = weight + rocks
            total = totalWeight * .166
            print(f'The weight of the ship on the Moon plus the rocks is {total:.2f}.')
    elif rocksCollected == "n":
        print("The weight of the ship on the Moon is", weight * .166)
    else:
        print("You have to choose y or n.")
        
#Mars   
elif where == "Mars":
    weight = float(input("How much does the spaceship weigh in kilos? "))
    rocksCollected = (input("Did you pick up any rocks to study? y/n "))
    if rocksCollected == "y":
        rocks = float(input("How many kilos of rocks did you collect? "))
        if weight:
            totalWeight = weight + rocks
            total = totalWeight * .377
            print(f'The weight of the ship on Mars plus the rocks is {total:.2f}.')
    elif rocksCollected == "n":
        print("The weight of the ship on Mars is", weight * .377)
    else:
        print("You have to choose y or n.")

#Venus       
elif where == "Venus":
    weight = float(input("How much does the spaceship weigh in kilos? "))
    minutes = int(input("How long has the ship been on Venus? "))
    if minutes > 127:
        print("Your spaceship has lasted the longest on Venus than any other spaceship so far!")
    else:
        print("The number of minutes to beat is 127.")
    if weight:
        print("The weight of the ship on Venus is", weight * .907)

#Pluto            
elif where == "Pluto":
    weight = float(input("How much does the spaceship weigh in kilos? "))
    print("The weight of the ship on Pluto is", weight * .067)

else:
    if where != "Moon" "Mars" "Venus" "Pluto":
        print("That's not a place the spaceship can land to be weighed.")
