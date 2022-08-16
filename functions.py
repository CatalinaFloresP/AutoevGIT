import json

def general_function(value):
    with open("farmers-protest-tweets-2021-03-5.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    list = []

    value = jsonObject[value]
    list.append(value)

    list.sort()
    for i in range(0,10):
        print(list[i])
