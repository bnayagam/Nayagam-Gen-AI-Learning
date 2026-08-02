import json
patient_data = {
    "name": "Patient A",
    "age": 45,
    "glucose_readings": [90,110,145]
}

with open ("patient.json", "w") as file:
    json.dump(patient_data, file, indent=10)

with open("patient.json", "r") as file:
    data = json.load(file)

print(f"name: {data['name']}")
print(f"age: {data['age']}")
print(f"glucose readings: {data['glucose_readings']}")