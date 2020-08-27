command = ""
started = False
while True:
    command = input("> ").lower()       #converts input, avoids repeated code
    if command == "help":
        print("start - to start the car \n stop - to stop the car \n quit - exit game")
    elif command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Starting car... Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand.")