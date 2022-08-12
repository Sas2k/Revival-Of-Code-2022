total = 0
ribbon_total = 0
with open("input.txt", "r", encoding="utf-8") as dimension:
    dimensions = dimension.read().splitlines()
    for dimension in dimensions:
        dimension = dimension.split("x")
        dimension = [int(i) for i in dimension]
        length = dimension[0]
        width = dimension[1]
        height = dimension[2]
        d1 = length * width
        d2 = width * height
        d3 = height * length
        smallest = min(d1, d2, d3)
        total += (d1*2) + (d2*2) + (d3*2) + smallest
    for ribbon in dimensions:
        ribbon = ribbon.split("x")
        ribbon = [int(i) for i in ribbon]
        r1 = ribbon[0]
        r2 = ribbon[1]
        r3 = ribbon[2]
        ribbon_total += 2*(min(r1+r2, r2+r3, r3+r1)) + (r1 * r2 * r3)

print(f"Total Of Wrapping Paper(feet): {total}")
print(f"Total of Ribbon(feet)[length]: {ribbon_total}")