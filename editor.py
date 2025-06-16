# write your code here
command = None

def display_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line",
          "Special commands: !help !done", sep="\n")

keywords = {"!done", "plain", "bold", "italic", "header", "link", "inline-code",
            "ordered-list", "unordered-list",
            "new-line"}

def add_new_text(new_text: str, current_text: str):
    if current_text:
        if new_text.startswith("#") and not current_text.endswith("\n"):
            new_text = "\n" + new_text

        return current_text + new_text
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

def list_formatter(ordered: bool = False):
    while True:
        rows = input("Number of rows: ")
        try:
            rows = int(rows)
            if rows < 1:
                raise ValueError

            result = ""

            for x in range(1, rows + 1):

                text = input(f"Row #{x}: ")

                if not ordered:
                    prefix = f"{x}. "
                else:
                    prefix = f"* "
                result += f"{prefix}{text}\n"

            return result
        except ValueError:
            print("The number of rows should be greater than zero")

def save_result_to_file(text_to_save: str):
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(text_to_save)



formatters = {
    "header": header_formatter,
    "link": link_formatter,
    "new-line": newline_formatter,
    "bold": bold_formatter,
    "italic": italic_formatter,
    "plain": plain_text_formatter,
    "inline-code": inline_code_formatter,
    "ordered-list": list_formatter,
}

formatted_text = ""

while command != "!done":
    command = input("Choose a formatter: ")

    if command == "!done":
        save_result_to_file(formatted_text)
        continue
    elif command == "!help":
        display_help()
    elif command not in keywords:
        print("Unknown formatting type or command")
    else:
        new_formated_text = formatters[command]() if command != "unordered-list" else list_formatter(True)
        formatted_text = add_new_text(new_formated_text, formatted_text)
        print(formatted_text)

