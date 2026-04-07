filename = "../task-4/example.txt"

with open(filename, "w") as file:
    file.write("Hello! This is a sample text.\n")
    file.write("We are learning how to write to a file using Python.\n")

print(f"Content written to {filename}")