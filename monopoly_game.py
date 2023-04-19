import random
def monopoly_game():  
    
    loc = 1
    cash = 100    
    own_property_1 = False
    keep_going = True
    
    while(keep_going):
        dice = random.randint(1, 6)
        loc = loc+dice
        if(loc == 1):
            cash = cash + 100
        elif(loc == 2):
            if(own_property_1 == False):
                cash = cash - 60
                print("property_1 purchased")
                own_property_1 = True
        elif(loc == 30):
            print("go to jail")
            loc = 10
        if(cash < 0):
            keep_going = False
            
    return        
            
monopoly_game()           
            
        