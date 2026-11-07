hours = [12.5, 8.0, 15.0, 10.5, 9.0, 20.0, 11.5, 7.5]
total = 0
for h in hours:
 total += h
mean = total / len(hours)
squares = 0
for h in hours:
 squares += (h - mean) ** 2
variance = squares / (len(hours) - 1) # sample variance: divide by n - 1
sd = variance ** 0.5
print(f"n = {len(hours)}, mean = {mean:.3f}")
print(f"sample variance = {variance:.3f}, SD = {sd:.3f}")