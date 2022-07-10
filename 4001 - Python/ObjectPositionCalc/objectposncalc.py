def main():

    print("This program will accept user input and output a simple calculation")

    initial_pos = float(input("Please enter the initial position of you object: "))
    initial_vel = float(input("Please enter the initial velocity: "))
    acceleration = float(input("What is the acceleration of the object? "))
    time = float(input("How long did the object take to complete the task? "))

    final_pos = (initial_pos) + (initial_vel*time) + (0.5 * (acceleration * (time ** 2)))

    print("The final position of the object is ", final_pos)

main()
