from unreliable_car import UnreliableCar

def test_unreliable_car():
    my_car = UnreliableCar("Old Clunker", 100, 50)
    total_distance = 0
    for _ in range(10):
        driven = my_car.drive(10)
        total_distance += driven
        print(f"Attempted 10km, drove {driven}km.")
    print(f"Total distance driven: {total_distance}")
    print(my_car)

if __name__ == "__main__":
    test_unreliable_car()