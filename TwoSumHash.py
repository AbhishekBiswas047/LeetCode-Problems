n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))

found = False

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print("Indices:", i, j)
            found = True
            break

    if found:
        break

if not found:
    print("No solution found")
