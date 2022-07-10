def main():

    print("This program will calculate an objects positions based off your inputs!")

    do_calc = True
    while( do_calc ):
        while( True ):
            try:
                initial_pos = float(input("Please enter the intial position: "))
                if( initial_pos < 0 ):
                    print("Negative numbers are not allowed")
                    continue
            except ValueError:
                print("Please enter only numerical values")
            else:
                break
                
        while( True ):
            try:
                initial_vel = float(input("Please enter the intial velocity: "))
                if( initial_vel < 0 ):
                    print("Negative numbers are not allowed")
                    continue
            except ValueError:
                print("Please enter only numerical values")
            else:
                break

        while( True ):
            try: 
                acceleration = float(input("What is the acceleration of the object? "))
                if( acceleration < 0 ):
                    print("Negative numbers are not allowed")
                    continue
            except ValueError:
                print("Please enter only numerical values")
            else:
                break

        while( True ):
            try:
                time = float(input("Please enter the time it took for the object to stop: "))
                if( time < 0 ):
                    print("Negative numbers are not allowed")
                    continue
            except ValueError:
                print("Please enter only numerical values")
            else:
                break

        final_pos = (initial_pos) + (initial_vel * time) + (0.5 * (acceleration * (time ** 2)))

        print("The final position of the object is ", final_pos)

        another_calc = input("Do you want to perform another calculation? (y/n): ")
        if( another_calc != "y" ):
            print("Thank you for using the calculator!")
            do_calc = False

main()

    
