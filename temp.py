while True:
    with open("temp.txt", "r") as file:
        #open
        data = file.read()
        data = data.replace(" ", "")

