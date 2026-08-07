def bmi(weight_kg, height_m):
    result = weight_kg / (height_m ** 2)
    return round(result, 1)

print(bmi(81, 1.78))