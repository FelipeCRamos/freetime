# Made by FelipeCRamos
__author__ = "FelipeCRamos"

''' FUNCTIONS '''
def counter(list, list_element):
    global final_result
    counter = 0
    for element in list_element:
       print(element[:-1],':',list.count(element), 'times ~ %.2f%%' %(list.count(element)/len(list)*100))

def enterFile():
    filename = input("Please, enter the filename below:\n> ")
    main(filename)

def main(filename):
    try:
        file = open(filename, 'r')
        lines, weathers, elements_all = [], [], []
        for line in file:
            lines.append(line.split(','))
        lines.pop(0)
        for i in range(len(lines)):
            if(lines[i][1] not in weathers):
                weathers.append(lines[i][1])
            elements_all.append(lines[i][1])
        print('\n' + counter(elements_all, weathers))
        print("\nExiting...")

    except FileNotFoundError:
        print("\nThe file doesn't exist!\n\nPlease, try again.\n")
        enterFile()

''' PROGRAM ITSELF '''
print("Please, be welcome to la_weather_counter!")
enterFile()
