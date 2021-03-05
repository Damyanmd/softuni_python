def calc_combination(names, n, combs=[]):
    if len(combs) == n:
        print(', '.join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calc_combination(names[i+1:], n, combs)
        combs.pop()

name = input().split(', ')
n = int(input())
calc_combination(name, n)