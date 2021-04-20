import json
from bmi_calculator_fun import calculateBmi

class BmiCalculator():
    dataFile = 'Data/input.json'
    data, count = calculateBmi(dataFile)

    # Save new data in JSON file
    saveData = open(dataFile, "w")
    json.dump(data, saveData)
    saveData.close()

    print("Total number of overweight person = ", count)

