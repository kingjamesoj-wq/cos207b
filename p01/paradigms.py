data = [3, 1, 4, 1, 5]
# 1. Imperative: say HOW, step by step, changing a variable
total = 0
for x in data:
 total = total + x * x
print("imperative :", total)
# 2. Functional: combine functions; no variable is changed
print("functional :", sum(map(lambda x: x * x, data)))
# 3. Declarative style: say WHAT you want
print("declarative:", sum(x * x for x in data))