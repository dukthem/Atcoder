n, q = map(int, input().split())
s = input()

# Function to count occurrences of "ABC" in the string
def count_abc(s):
    count = 0
    i = 0
    while i < len(s) - 2:
        if s[i:i+3] == "ABC":
            count += 1
            i += 3  # Skip the next two characters since they form "ABC"
        else:
            i += 1
    return count

# Initial count of "ABC" in the original string
abc_count = count_abc(s)

for _ in range(q):
    a, c = input().split()
    x = int(a)
    x -= 1  # Convert to zero-based index

    # Only modify the string if there's a change
    if s[x] != c:
        # Check if we need to reduce count
        if x > 1 and s[x-2:x+1] == "AB" and c == "C":
            abc_count -= 1
        if x > 0 and s[x-1:x+2] == "BC" and c == "A":
            abc_count -= 1
        if s[x-1:x+2] == "AB" and c == "C":
            abc_count += 1
        if s[x:x+3] == "ABC" and c == "A":
            abc_count -= 1

        # Update string
        s = s[:x] + c + s[x+1:]

        # Check if we need to increase count
        if x < n - 2 and s[x:x+3] == "ABC":
            abc_count += 1
        
    print(abc_count)
