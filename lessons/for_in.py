"""An example of for in syntax."""

names: list[str] = ["Isaac", "Kaki", "Erzi", "Marc"]

# Example of iterating through names usng a while loop
print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for..in loop is the same as the while loop above
print("for..in output:")
for name in names:
    print(name)