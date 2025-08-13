import math

target_values = [3.14, 3.141, 3.1415, 3.14159]
targets_reached = {val: None for val in target_values}

pi_estimate = 0
denominator = 1
sign = 1
terms_used = 0

print("Term\tπ Estimate")

while None in targets_reached.values():
    pi_estimate += sign * (4 / denominator)
    terms_used += 1
    print(f"{terms_used}\t{pi_estimate:.10f}")
    
    for val in target_values:
        if targets_reached[val] is None and round(pi_estimate, len(str(val).split('.')[-1])) == val:
            targets_reached[val] = terms_used

    denominator += 2
    sign *= -1  

print("\nTarget Accuracy Achieved:")
for val in target_values:
    print(f"{val} reached after {targets_reached[val]} terms")