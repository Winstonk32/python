# Define the number of rows
rows = 5

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for columns
    for j in range(i):
        print(i, end=" ")  # Print the same number with a space
    print()  # Move to the next line after each row
