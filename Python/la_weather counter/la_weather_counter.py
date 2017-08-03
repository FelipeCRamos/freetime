# Test
__author__ = "FelipeCRamos"
print("Please, be welcome to la_weather_counter!")

def counter(list, list_element):
    global final_result
    counter = 0
    for element in list_element:
       print(element[:-1],':',list.count(element), 'times ~ %.2f%%' %(list.count(element)/len(list)*100))

file = open('la_weather.csv', 'r')
lines = []
weathers = []
elements_all = []
for line in file:
    lines.append(line.split(','))

lines.pop(0)
# print(lines)
for i in range(len(lines)):
    if(lines[i][1] not in weathers):
        weathers.append(lines[i][1])
    elements_all.append(lines[i][1])

# print(weathers)
print('')
print(counter(elements_all, weathers))
print("\nExiting...")
