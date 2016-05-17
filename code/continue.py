numbersTaken = [2, 5, 12, 35, 57]

print("Here are the numbers still available:")

for n in range(1, 20):
    if n in numbersTaken:
        # Means keep going loop skip anything after it if condition matches
        continue
    print(n)
