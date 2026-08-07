# Problem 1: calculate BMI
def bmi(weight_kg, height_m):
    result = weight_kg / (height_m ** 2)
    return round(result, 1)
 
 
# Problem 2: classify a BMI value
def classify_bmi(bmi_value):
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value < 25:
        return "normal"
    elif bmi_value < 30:
        return "overweight"
    else:
        return "obese"
 
 
# Problem 3: loop through patient records and classify each one
patients = [
    {"name": "A", "weight": 70, "height": 1.75},
    {"name": "B", "weight": 95, "height": 1.70},
    {"name": "C", "weight": 55, "height": 1.60},
]
 
for patient in patients:
    patient_bmi = bmi(patient["weight"], patient["height"])
    category = classify_bmi(patient_bmi)
    print(patient["name"], patient_bmi, category)

obese_names = [patient["name"] 

for patient in patients:
    if classify_bmi(bmi(patient["weight"], patient["height"])) == "obese"]
print(obese_names) 