def classify_bmi(bmi_value):
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value < 25:
        return "normal"
    elif bmi_value < 30:
        return "overweight"
    else:
        return "obese"

print(classify_bmi(25.6))