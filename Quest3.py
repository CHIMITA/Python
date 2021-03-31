#도전문제 1 중첩 for문

for i in range(5):
    print("k", end='')
    for j in range(5):
        print("a", end='')
    print("k")

print("-" *20)

for j in range(6):
    print("K", end='')

print("")

for k in range(6):
    print("A", end='')
print('')

print("-" *20)

for i in range(5):
    if(i % 2 == 0):
        for j in range(6):
            print("K", end='')
    else:
        for k in range(6):
            print("A", end='')
        print('')

print("-" *20, end='')

for h in range(6):
    for b in range(h):
        print('*', end='')
    print('')
