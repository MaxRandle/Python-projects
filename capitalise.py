def capital(string):
    string += " "
    letters = "abcdefghijklmnopqrstuvwxyz"
    characters = ""
    capital_string = ""
    for char in string:
        characters += char
        if char == " ":
            capital_string += characters[0].capitalize()
            capital_string += characters[1::]
            characters = ""
    return capital_string
            
