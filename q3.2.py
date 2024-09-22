# start

max_stars: int = int(input('enter a number:'))
stars: int = 1
spaces: int = max_stars // 2

for _ in range(1, (max_stars - stars) // 2):
    print(' ', end=' ')
print()
for _ in range(1, stars + 1):
    print('*', end=' ')
print()
spaces -= 1

# stop


#start

max_stars: int = int(input('enter a number:'))
stars: int = 1

while stars <= max_stars:
    for _ in range(1, stars + 1):
        print('*', end=' ')
    print()
    stars += 2

# stop


#start

max_stars: int = int(input('enter a number:'))
stars: int = 1
spaces: int = 3

for stars in range(1, max_stars + 2, 2):
    for _ in range(1, spaces + 1):
        print(' ',end=' ')
        for _ in range(1, stars + 1):
            print('*',end=' ')
        print()
        spaces -=1

#stop
