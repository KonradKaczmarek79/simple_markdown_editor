command = None

def display_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line",
          "Special commands: !help !done", sep="\n")

keywords = {"!done", "plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"}

while command != "!done":
    command = input("Choose a formatter: ")

    if command == "!help":
        display_help()
    elif command not in keywords:
        print("Unknown formatting type or command")