temperature = [36.2, 38, 37.5, 40.0, 45, 35.7]
for temp in temperature:
    if temp < 36:
        print(f"{temp}: Low Range")
    elif 36<= temp <= 40:
        print(f"{temp}: Decent Range")
    else:
        print("High Temp")