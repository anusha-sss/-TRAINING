
info = ""
while info.lower() != "quit":

    info = input("> ")
    if info == "help":
        print("start-to start the car")
        print("stop-to stop the car")
        print("quit-to quit the game")
    elif info == "start":
        print("Car started . . . ready to go")
    elif info == "stop":
        print("car stopped")
    elif info == "quit":
        break
    else:
        print("I don't understand")
