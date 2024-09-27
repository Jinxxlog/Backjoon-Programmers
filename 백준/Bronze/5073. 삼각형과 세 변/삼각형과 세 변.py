
while True:
    tri = sorted(map(int, input().split()))

    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break

    if tri[0] + tri[1] <= tri[2]:
        print("Invalid")
    elif tri[0] == tri[1] == tri[2]:
        print("Equilateral")
    elif tri[0] != tri[1] != tri[2]:
        print("Scalene")
    else:
        print("Isosceles")