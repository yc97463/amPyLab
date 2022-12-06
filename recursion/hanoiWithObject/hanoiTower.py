from stack_module import Stack


def init_hanoi_tower(n):
    a = Stack("a")
    b = Stack("b")
    c = Stack("c")
    for i in range(n-1, -1, -1):
        item = str(i)
        a.push(item)
    return a, b, c


def solve_hanoi_tower(n, a, b, c):
    if n == 1:
        item = a.pop()
        c.push(item)
        inst1 = "item = "+a.name+".pop()"
        inst2 = c.name+"push(item)"
        print(inst1)
        print(inst2)
    else:
        solve_hanoi_tower(n-1, a, c, b)
        solve_hanoi_tower(1, a, b, c)
        solve_hanoi_tower(n-1, b, a, c)


n = 3
a, b, c = init_hanoi_tower(n)
print("a = ", a.items)
print("b = ", b.items)
print("c = ", c.items)
solve_hanoi_tower(n, a, b, c)
print("a = ", a.items)
print("b = ", b.items)
print("c = ", c.items)
