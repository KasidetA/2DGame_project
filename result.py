# Task 4
def calculate_weight_ratio(mp, rp):
    me = 5.97e24
    re = 6371
    massRatio = mp / me
    radiusRatio = re / rp
    return massRatio * radiusRatio * radiusRatio

ratios = []

while True:
    name = input("Name the planet ")
    mp = float(input(f"Enter mass for {name} ")) * 1e24
    rp = float(input(f"Enter mean radius for {name} "))

    weightRatio = calculate_weight_ratio(mp, rp)
    print(f"Weight ratio for {name} {weightRatio}")
    ratios.append(weightRatio)

    more = input("more y/n ").lower()
    if more == 'n':
        break

total = len(ratios)
average = sum(ratios) / total
print(f"A total of {total} calculations were made")
print(f"The average ratio was {average}")
print("Goodbye")
