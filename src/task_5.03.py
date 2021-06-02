# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.

for i in range(200, 300):
    r, t = 0, 0
    for k in range(1, i):
        if i % k == 0:
            r += k
    for j in range(1, r):
        if r % j == 0:
            t += j
    if i == t and i < r:
        print(i, r)
