command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")


        else:
            started = True
        print("Car started....")

    elif command == command == "stop":
        if not started:
            print("Car already stopped")

        else:
            started = True
        print("Car stopped.")
    elif command == "help":
        print("""
        start - to start car
        stop - to stop car
        quit - to quit game
        
        """)
    elif command == "quit":
        break
    else:
        print("sorry I don't understand")
