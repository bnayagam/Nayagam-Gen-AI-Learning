def classify_temperature(temp):
    if temp < 36.0:
        return "Low"
    elif 36.0 <= temp <= 39:
        return "Good Range"
    else:
        return "May be fever"


temperatures = [35, 36.8, 37.4, 39.1, 40]

for temp in temperatures:
    result = classify_temperature(temp)
    print (f"{temp} Degree Celsius: {result}")


