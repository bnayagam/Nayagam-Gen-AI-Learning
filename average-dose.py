def average_dose(doses):
    if len(doses) == 0:
        return None
    return sum(doses) / len(doses)

print(f"{average_dose([500, 250, 750]):.2f}")
print(average_dose([]))