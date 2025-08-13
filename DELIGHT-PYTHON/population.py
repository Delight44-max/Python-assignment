current_population = 8_230_000_000  # 8.23 billion
growth_rate = 0.00841  # 0.841%

print("Year\tProjected Population")
for year in range(1, 101):
    current_population *= (1 + growth_rate)
    print(f"{year}\t{int(current_population):,}")