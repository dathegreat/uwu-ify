import random

def uwu_ify(text):
    new_text = ""
    #loop through each letter and replace r's and l's with w's
    for letter in text:
        new_text += "w" if letter.lower() == "l" or letter.lower() == "r" else letter.lower()
        #randomly append uwu to end of sentences
        if letter == ".":
            if random.random() < 0.1:
                new_text += " uwu."
    return new_text

with open("text.txt", "w+t") as file:
    resume = input("Please open text.txt and fill it with what you want to convert. Hit enter when done\n>> ")

    to_convert = file.read()
    to_write = uwu_ify(to_convert)
    file.close()

with open("uwu_ify.txt", "w+t") as file:
    file.write(to_write)
    file.close()

with open("uwu_ify.txt", "r") as file:
    print(file.read())
    file.close()

