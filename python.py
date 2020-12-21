if __name__ == '__main__':
    a = int(input())
    b = int(input())

print('{0}\n {1}\n {2}\n'.format(a+b, a*2-b, a*a))


#####################################################

print('{0}\n {1}\n'.format(a//b, a/b))

#####################################################

if __name__ == '__main__':
    n = int(input())
i = 0

while i < n:
    print(i**2)
    i += 1
#####################################################

def is_leap(year):
    leap = False

    return year % 4 == 0 and ( year % 400 == 0 or year % 100 != 0)

    return leap

year = int(input())


######################################################

if __name__ == '__main__':
    n = int(input())

i = 1

for i in range(1, n+1):
    print(i, end="")
