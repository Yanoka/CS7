#FALLING DISTANCE
GRAVITY = 9.8
def main():
    print ('Time\t Distance')

    for time in range(1,11):
        distance = falling_distance(time)
        print(time,'sec' '\t', format(distance,'2.2f'), 'g')

def falling_distance(time):
    distance = (GRAVITY*time**2)/2
    return distance

main()

