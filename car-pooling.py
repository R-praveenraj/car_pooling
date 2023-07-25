def car_pooling(array, capacity):
    kilometer = {}
    for num_passengers, start_km, end_km in array:
        for i in range(start_km, end_km):
            kilometer[i] = kilometer.get(i, 0) + num_passengers
            if kilometer[i] > capacity:
                return False
    return True

twoD_array=[]
num_of_trips=int(input())
for i in range(num_of_trips):
    twoD_array.append(list(map(int,input().split())))
capacity=int(input())
print(car_pooling(twoD_array,capacity))