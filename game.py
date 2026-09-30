cuarto = 'entrada'
ingredientes = 0
juego_activo = True

while juego_activo:
    if cuarto == 'entrada':
        print("Welcome to Foquita Gyu Restaurant. A very demanding customer has been waiting half an hour for his food, and the chef turned into a seal!")
        print("You need to find 2 ingredients in the kitchen and bring them to the dining room before he leaves.")
        print("1. Go to the dining room")
        print("2. Go to the kitchen")
        
        respuesta = input("Choose an option: ")
        
        if respuesta == "1":
            cuarto = "comedor"
        elif respuesta == "2":
            cuarto = "cocina"
        else:
            print("You picked a door that doesn't exist... and now you're in the bathroom? Go back to the entrance.")
    
    elif cuarto == "comedor":
        if ingredientes >= 2:
            print("Well done, you got your two ingredients. The customer tastes the dish and loves it!")
            juego_activo = False
        else:
            print("What a disgrace. You only have " + str(ingredientes) + " ingredients")
            cuarto = "entrada"
    elif cuarto == "cocina":
        print("You just found the seal chef. He's very cute and funny now.")
        print("1. Pantry")
        print("2. Fridge")
        print("3. Back to the entrance")
        
        respuesta = input("Choose an option: ")
        if respuesta == "1":
            cuarto = "despensa"
        elif respuesta == "2":
            cuarto = "refrigerador"
        elif respuesta == "3":
            cuarto = "entrada"
        else:
            print("Back in the bathroom again, oh boy")
            
    elif cuarto == "despensa":
        print("You are in the pantry. Solve a riddle to get an ingredient.")
        print("I come and go, go and come, leaving white what was black.")
        
        respuesta = input("Your answer is: ").lower()
        
        if respuesta == "eraser" or respuesta == "an eraser" or respuesta == "the eraser":
            print("Well done, you just got a fried egg")
            ingredientes += 1
            cuarto = "cocina"
        else:
            print("The chef is delighted, nobody has been able to solve his riddle")
            
    elif cuarto == "refrigerador":
        print("Welcome to the fridge, a place to smell and taste.")
        print("To get the ingredient here, you have to unscramble these two words")
        print("nrfhec seirf")
        
        respuesta = input("Your answer is: ").lower()
        
        if respuesta == "french fries" or respuesta == "fries":
            print("Excellent, you just got french fries")
            ingredientes += 1
            cuarto = "cocina"
        else:
            print("You got it wrong, try again")
        
    print("")
        