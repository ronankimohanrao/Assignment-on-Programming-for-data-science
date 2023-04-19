# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:32:04 2023

@author: SURESH
"""
import random
"""1 = body
 2 = head
 3 = antenna
 4 = eye
 5 = mouth
 6 = leg
 *collect body first before all body parts
 *head before antenna
 *eyes or mouth
 # 1 body, 1 head, 2 antenna, 2 eyes, 1 mouth, 6 legs """

def beetle_game(): 
    
    totalbodyparts = 13
    totalpartscollected = 1
    bodycount = 1
    antennacount = 1
    eyescount = 1
    mouthcount = 1
    legscount = 1       
    while(totalpartscollected<=totalbodyparts): 
        dice_roll = random.randint(1, 6)
        if((dice_roll == 1) and (totalpartscollected == 1)):
            print("body collected")
            bodycount = bodycount+1
            totalpartscollected = totalpartscollected+1
        elif((dice_roll == 2) and (totalpartscollected == 2)):    
            print("head collected")
            bodycount = bodycount+1 
            totalpartscollected = totalpartscollected+1
        else:
            if(dice_roll == 3 and antennacount <= 2 and bodycount==3):
                print("antenna collected")
                antennacount = antennacount+1
                totalpartscollected = totalpartscollected+1
            else:
                if(dice_roll == 4 and eyescount <= 2 and bodycount==3):
                    print("eye collected")
                    eyescount = eyescount+1
                    totalpartscollected = totalpartscollected+1
                else:
                    if((dice_roll == 5) and (mouthcount == 1) and bodycount==3):
                        print("mouth collected")
                        mouthcount = mouthcount+1
                        totalpartscollected = totalpartscollected+1
                    else:
                        if((dice_roll == 6) and legscount<=6 and bodycount==3):
                            print("leg collected")
                            legscount = legscount+1
                            totalpartscollected = totalpartscollected+1
                        else:
                            print("roll the dice again")
            
                
            
    return

beetle_game()
    
            
              
    

"""def beetle_game():
    
    
    else:
         if(dice == 5):
             print("mouth collected")
             total_parts_collected = total_parts_collected+1
         else:
             print("leg collected")
             total_parts_collected = total_parts_collected+1
             
             
    
    total_body_parts = 13
    total_parts_collected = 1
    count_rolls = 0
    body_count = 1
    antenna_count = 1
    eyes_count = 1
    mouth_count = 1
    legs_count = 1
    while(total_parts_collected <= total_body_parts):
        dice = random.randint(1,6)
        print(dice)
        count_rolls = count_rolls + 1
        
        
        if((dice == 1) and (total_parts_collected == 1)):
            print("body collected")
            body_count = body_count+1
            total_parts_collected = total_parts_collected+1
        elif((dice == 2) and (total_parts_collected == 2)):    
            print("head collected")
            body_count == body_count+1
            total_parts_collected = total_parts_collected+1
        else:
            if(dice == 3 and antenna_count <= 2 and body_count == 3):
                print("antenna collected")
                antenna_count = antenna_count+1
                total_parts_collected = total_parts_collected+1
            elif(dice == 4 and eyes_count <= 2 and body_count == 3):
                print("eye collected")
                eyes_count = eyes_count+1
                total_parts_collected = total_parts_collected+1
            elif((dice == 5) and (mouth_count == 1) and (body_count == 3)):
                print("mouth collected")
                mouth_count = mouth_count+1
                total_parts_collected = total_parts_collected+1
            elif((dice == 6)  and (body_count == 3)):
                print("leg collected")
                legs_count = legs_count+1
                total_parts_collected = total_parts_collected+1
                
                
                else:
                    if(dice == 5):
                        print("mouth collected")
                        total_parts_collected = total_parts_collected+1
                    else:
                        print("leg collected")
                        total_parts_collected = total_parts_collected+1
            
    return

beetle_game()"""

    