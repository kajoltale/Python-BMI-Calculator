import json

def getBMICategoryHelsthRisk(bmi, count):
    if 0 <= bmi <= 18.4:
        bmiCategory = "Underweight"
        healthRisk = "Malnutrition risk"
    elif 18.5 <= bmi <= 24.9:
        bmiCategory = "Normal weight"
        healthRisk = "Low risk"
    elif 25 <= bmi <= 29.9:
        bmiCategory = "Overweight"
        healthRisk = "Enhanced risk"
        count = count + 1
    elif 30 <= bmi <= 34.9:
        bmiCategory = "Moderately obese"
        healthRisk = "Medium risk"
    elif 35 <= bmi <= 39.9:
        bmiCategory = "Severely obese"
        healthRisk = "High risk"
    else:
        bmiCategory = "Very severely obese"
        healthRisk = "Very high risk"

    return bmiCategory,healthRisk, count

#This function calculates BMI
def calculateBmi(input):
    readJson = open(input)
    data = json.load(readJson)
    count = 0
    for row in data:
        heightM = row['HeightCm']/100
        bmi = row['WeightKg']/(heightM * heightM)

        bmiCategory, healthRisk, count = getBMICategoryHelsthRisk(bmi, count)

        #Add 3 new columns
        temp = {"BMI": bmi, "BMI Category": bmiCategory, "Health risk": healthRisk}
        row.update(temp)

    readJson.close()

    return data, count