
def main():
    string = input("Paste in your AutoHotkey string with %s")

    print(f"Entered String: {string}")
    print(f"Corrected for AHK use: {ahk(string)}")


def ahk(str):
    new_str = ""
    for ch in str:
        if ch == '%':
            new_str = new_str + '`' + ch
        else:
            new_str = new_str + ch
    return new_str


if __name__ == '__main__':
    main()
