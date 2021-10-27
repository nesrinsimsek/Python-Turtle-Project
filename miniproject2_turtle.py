from manager import *


def q1(turtle):  # the function that provides movements for the first question.
    while is_facing_wall(turtle):  # turtle firstly turns left to start, moves 30 units and repeats these until there is a wall in front of it.
        pd(turtle)
        lt(turtle, 90)
        fd(turtle, 30)
        if is_facing_wall(turtle):
            rt(turtle, 90)
            if is_facing_wall(turtle):  # turtle turns back and keeps moving.
                lt(turtle, 90)
                lt(turtle, 180)
                fd(turtle, 30)
                lt(turtle, 90)
            while is_facing_wall(turtle):  # turtle checks left side while it is going down on the maze and while there are walls, keeps moving down.
                rt(turtle, 90)
                fd(turtle, 30)
                lt(turtle, 90)
            break   # if there is no wall at the left of the turtle while it is going down, -means turtle arrives exit- , it stops.
        rt(turtle, 90)  # if there is no wall in front of turtle while it is going up, it keeps checking right side.
    fd(turtle, 30)  # when turtle arrives exit it leaves the maze by moving 30 units.


def picking_treasures(turtle):  # the function picks the treasures.
    while not is_facing_wall(turtle):  # turtle moves while there is no wall in front of it.
        fd(turtle, 30)
        if is_over_treasure(turtle):  # turtle picks the treasure under of it.
            pick_treasure(turtle)
            if max_treasure_count == 1:  # if there is only 1 treasure turtle picks it and stops.
                break
    else:
        lt(turtle, 180)  # if there is a wall in front of turtle it turns 180 degrees.


def oneTour_for_a_column(turtle):  # turtle takes a tour to check the column if there are treasures to pick.
    for i in range(2):  # turtle completes the tour and picks all treasures at the column.
        picking_treasures(turtle)
    rt(turtle, 90)  # after tour is completed, turtle turns right at the bottom of the column to check if there is a wall.
    q1(turtle)  # turtle starts checking right hand side.


def oneTour_after_firstTour(turtle):  # turtle passes to the next column, completes the column and arrives first space between two columns.
    fd(turtle, 30)  # moves 30 units to pass to the next column.
    if is_over_treasure(turtle):  # picks treasures if there are.
        pick_treasure(turtle)
    lt(turtle, 90)  # turtle turns left to start the tour.
    oneTour_for_a_column(turtle)  # keeps taking tours on columns.


def q2(turtle, no_of_columns):  # if it is question two,
    for i in range(no_of_columns * 2):  # turtle checks and searches the exit. until it find, it continues.
        q1(turtle)


def q3(turtle, max_treasure_count):  # if it is question three,
    lt(turtle, 90)  # turtle firstly turns left to start.
    if max_treasure_count == 1:  # if only one treasure will be picked,
        picking_treasures(turtle)  # turtle picks it and stops by this function.
    elif max_treasure_count == 2:  # if two treasures will be picked,
        for i in range(2):
            picking_treasures(turtle)
    elif max_treasure_count >= 3:  # if more than maximum treasures are wanted to be picked,
        oneTour_for_a_column(turtle)  # all treasures are picked, turtle searches the exit and leaves the maze.


def q4(turtle, max_treasure_count, no_of_columns):  # if it is question four,
    lt(turtle, 90)  # turtle firstly turns left to start.
    if max_treasure_count == 1:  # if only one treasure will be picked,
        picking_treasures(turtle)  # turtle picks it and stops by this function.
    elif max_treasure_count >= 5:  # if all treasures or more than all are wanted to be picked,
        oneTour_for_a_column(turtle)  # turtle takes a tour at first column and picks treasures there.
        for i in range(no_of_columns - 1):  # for the time one less of number of columns,
            oneTour_after_firstTour(turtle)  # turtle takes other tours on columns and at the end it exits.


manager = WorldManager()
is_facing_wall = manager.is_facing_wall
is_over_treasure = manager.is_over_treasure
pick_treasure = manager.pick_treasure

if __name__ == '__main__':

    print(40 * "*" + " Welcome " + 40 * "*" + "\n")
    delay = 0.4

    while True:
        world = TurtleWorld()
        world.geometry("600x400")
        for i in range(1, 5):
            print(i, "-", "Question", i)
        print(0, "-", "Exit")
        choice = int(input("Choose Question Number: "))
        if choice == 1:
            manager.read_world("maze1.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q1(bob)
            wait_for_user()
        elif choice == 2:
            no_of_columns = int(input(
                "Enter the number of columns your maze will have: "))
            manager.read_world("maze2.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q2(bob, no_of_columns)
            wait_for_user()
        elif choice == 3:
            max_treasure_count = int(input(
                "Enter the maximum number of treasures the turtle can pick up: "))
            manager.read_world("maze3.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q3(bob, max_treasure_count)
            if max_treasure_count <= 2:
                print("# of treasures collected:" + str(max_treasure_count))
            else:
                print("# of treasures collected:" + "2")
            wait_for_user()
        elif choice == 4:
            no_of_columns = int(input(
                "Enter the number of columns your maze will have: "))
            max_treasure_count = int(input(
                "Enter the maximum number of treasures the turtle can pick up: "))
            manager.read_world("maze4.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q4(bob, max_treasure_count, no_of_columns)
            if max_treasure_count == 1:
                print("# of treasures collected:" + "1")
            else:
                print("# of treasures collected:" + "5")

            wait_for_user()
        elif choice == 0:
            exit()

