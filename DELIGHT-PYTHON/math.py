import math

n_terms = 10

e_estimate = 0

print("Term\tValue\t\tCumulative e")
for n in range(n_terms):
    term_value = 1 / math.factorial(n)
    e_estimate += term_value
    print(f"{n}\t{term_value:.10f}\t{e_estimate:.10f}")
    
print(f"\nEstimated value of e after {n_terms} terms: {e_estimate:.10f}")