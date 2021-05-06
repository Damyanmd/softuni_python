n_m = input()
n, m = n_m.split(' ')
n = int(n)
m = int(m)
n_set = set()
m_set = set()
unique_elements = set()
for i in range(n):
    n_set.add(input())
for i in range(m):
    m_set.add(input())
for number in n_set:
    if number in m_set:
        unique_elements.add(number)
print('\n'.join(unique_elements))