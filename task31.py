'''
Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ...,
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''


def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


lst = []
for i in range(1, 15):
    lst.append(fib(i - 1))

print(lst)
print(fib(8))
