limit = 20

print("Pythagorean Triples (a, b, c) ≤ 20:")
for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        for c in range(b, limit + 1):
            if a**2 + b**2 == c**2:
                print(f"({a}, {b}, {c})")