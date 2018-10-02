import time
import sys
import random
import sensors

def optimal_direction():
    distance_table = sensors.pan_check_distance()
    print("front distance", distance_table['front'])
    front_dist = distance_table['front']
    print("left distance", distance_table['left'])
    left_dist = distance_table['left']
    print("right distance", distance_table['right'])
    right_dist = distance_table['right']

    if left_dist < 20 and right_dist < 20:
        optimal_direction = 'reverse'
    else:
        dist_diff = left_dist - right_dist
        if dist_diff > 0:
            optimal_direction = 'left'
        elif dist_diff < 0:
            optimal_direction = 'right'
        else:
            print("It's all the same to me.. my gut says")
            x = random.randrange(0, 2)
            if x == 0:
                optimal_direction = 'left'
            elif x == 1:
                optimal_direction = 'right'
            else:
                print("Something went wrong in random number generation.")
    #Return Optimal Direction
    print(optimal_direction, "is optimal")

    return optimal_direction
