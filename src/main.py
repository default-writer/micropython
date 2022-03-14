def is_constructable(a, debug = False):
    from math import sqrt
    result = []
    side = int(sqrt(a))
    side_2 = int(sqrt(a/2))
    r = a - side*side
    r_2 = a - side_2*side_2
    if r == 0:
        if debug: 
            print (f"{side}*{side} + {0}*{0} == {a}")
        return True
    if r == 1:
        if debug: 
            print (f"{side}*{side} + {1}*{1} == {a}")
        return True
    if r_2 == a/2:
        if debug: 
            print (f"{side_2}*{side_2} + {side_2}*{side_2} == {a}")
        return True
    for x in range(side_2 + 1, side + 1, 1):
        s = 2*x*x
        if s == a:
            if debug: 
                print (f"{x}*{x} + {x}*{x} == {a}")
            return True
        if s > a:
            for i in range(x, -1, -1):
                a_1 = x*x + i*i
                if a_1 == a:
                    if debug: 
                        print (f"{x}*{x} + {i}*{i} == {a}")
                    return True
                if a_1 < a:
                    break
    return False

s = []

for i in range(32768):
    if is_constructable(i):
        s.append(i)

l = len(s)

res = []
for i in range(32768):
    if i not in s:
        j = 0
        x = 0
        duplicate = False
        while j < len(res):
            x = res[j]
            if i % x == 0:
                duplicate = True
                break
            j += 1
        if not duplicate:
            res.append(i)

print(res)
