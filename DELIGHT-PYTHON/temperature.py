def temperature_advisory(temp, unit='C', threshold=30):
    if unit == 'C':
        compare_temp = temp
        compare_threshold = threshold
    elif unit == 'F':
        compare_temp = temp
        compare_threshold = threshold
    else:
        raise ValueError("Invalid unit. Use 'C' or 'F'.")

    if compare_temp < compare_threshold:
        return "Cold advisory"
    else:
        return "Heat alert"