with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("output.txt", "a") as file:
    file.write("This is a new line return by Python\n")
    file.write("Second line\n")