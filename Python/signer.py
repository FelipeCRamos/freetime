# CODED BY FelipeCRamos
# FOR FREETIME

import os
# CODED BY: FELIPECRAMOS
# THIS IS THE SIGN PHRASE, JUST CHANGE IT
# DO NOT FORGET TO CHANGE THE ATTRIBUTES TOO ON LINE 17 -> %(attribute1, attribute2, ...)
# phrase = "/* %s - URI SOLUTION */\n/* LINK: https://www.urionlinejudge.com.br/judge/en/problems/view/%s */\n/* CODED BY: %s */\n\n"
# phrase = "# CODED BY %s\n# FOR FREETIME\n\n"
author = "FelipeCRamos"
def makeItHappen(ext, dir, phrase):
    count = 0
    for filename in os.listdir('.'):
        if filename.endswith(ext):
            count += 1
            print("~ Reading file: %s"%(filename))
            file = open(filename, 'r+')
            file.content = file.read()
            file.seek(0,0)
            # file.write(phrase %(filename[:-2], filename[0:4], author)+file.content)
            file.write(phrase %(author)+file.content)
            file.close()
    print("\nSucessful modified %i files.\nExiting...\n"%(count))
print("\n\tBe welcome to the Signer v1.0\n\nPlease, tell us the extention of the file and then the path of it.\n(use '.' to current path, ex: '.c' '/usr/felipecramos')")

# Main
extension = input("Extension: ")
path = input("Path: ")

print("You're about to sign every file that ends with '%s' that is on path '%s';"%(extension, path))
phrase = input("Please, give us the phrase you want to sign: (for more complex phrases, look to the .py file)\n")
print("\nSIGN:\n" + phrase + "\n")
sure = input("\nAre you sure? (y/n) ")
if(sure == 'y'):
    print("\nLet's roll\n")

    makeItHappen(extension, path, phrase)
else:
    print("\nExiting...\n")
