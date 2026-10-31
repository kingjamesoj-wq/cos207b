scores = [62, 75, 48, 90, 71] # list of int
course = "WSU-COS 207" # str
mean = sum(scores) / len(scores) # float
passed = mean >= 50 # bool
for value in (scores, course, mean, passed):
 print(f"{type(value).__name__:<6} {value}")
print(f"{course}: n = {len(scores)}, mean = {mean:.2f}")