import random
import numpy as np
import matplotlib.pyplot as plt

#Define scenario: 0 - seat MUST be put down after use, 1 - seat is left in after use position
#Define the percentage of use in which the seat is used in the down position
loop = 10000 #define how many 'toilet uses' simulated 

def main(i):
    
    #running scenario 1
    counter = 0
    seat_pos = 0
    
    for j in range(loop):
        
        if random.random() < percent_down:
            counter, seat_pos = seat_down(i, counter, seat_pos)
            j += 1
        else:
            counter, seat_pos = seat_up(i, counter, seat_pos)
            j += 1
            
        
 
        
    return counter


#function for when the seat MUST ALWAY be down after use
def seat_down(scenario, counter, seat_pos): # function for when the seat is needed in the down position
    if scenario == 0:
        counter = counter        
        
    else:
        if seat_pos == 0:
            counter = counter
        else:
            counter += 1
            seat_pos = 0           
            

    return counter, seat_pos

def seat_up(scenario, counter, seat_pos): # function for when the seat is needed in the up position
    if scenario == 0:
        counter += 2
        
        
    else:
        if seat_pos == 0:
            counter += 1
            seat_pos = 1
        else:
            counter = counter
                       
            

        
    return counter, seat_pos

percent = np.linspace(0.2,0.9,100)
ratio = []
for k in range(len(percent)):
    percent_down = percent[k]
    for i in range(2): 
        if i == 0:
            a = main(i)
            i += 1
        else:
            b = main(i)
            i += 1

    temp = a/b

    ratio.append(temp)    
    
plt.xlabel("Percentage of time seat is needed down")
plt.ylabel("How ")

plt.plot(percent,ratio)
        
        