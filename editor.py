command = None

def display_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line",
          "Special commands: !help !done", sep="\n")

keywords = {"!done", "plain", "bold", "italic", "header", "link", "inline-code",
            # "ordered-list", "unordered-list",
            "new-line"}

def add_new_text(new_text: str, current_text: str):
    if current_text:
        if new_text.startswith("#") and not current_text.endswith("\n"):
            new_text = "\n" + new_text
        # elif not current_text.endswith(" ") and not current_text.endswith("\n"):
        #     new_text = " " + new_text
        return current_text + new_text # if not new_text.startswith("#") else current_text + "\n" + new_text
    return new_text

def header_formatter():
    while True:
        try:
            # if not a number ValueError will rise
            level = int(input("Level: "))

            if level < 1 or level > 6:
                raise ValueError
            text = input("Text: ")
            return f"{level * '#'} {text}\n"
        except ValueError:
            print("The level should be within the range of 1 to 6")

def link_formatter():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def newline_formatter():
    return "\n"

def bold_formatter():
    return f"**{input('Text: ')}**"

def italic_formatter():
    return f"*{input('Text: ')}*"

def plain_text_formatter():
    return f"{input('Text: ')}"

def inline_code_formatter():
    return f"`{input('Text: ')}`"

formatters = {
    "header": header_formatter,
    "link": link_formatter,
    "new-line": newline_formatter,
    "bold": bold_formatter,
    "italic": italic_formatter,
    "plain": plain_text_formatter,
    "inline-code": inline_code_formatter,
}

formatted_text = ""

while command != "!done":
    command = input("Choose a formatter: ")

    if command == "!done":
        continue
    elif command == "!help":
        display_help()
    elif command not in keywords:
        print("Unknown formatting type or command")
    else:
        new_formated_text = formatters[command]()
        formatted_text = add_new_text(new_formated_text, formatted_text)
        print(formatted_text)