input_path = "Input/students.txt"
output_path = "Output/output13.txt"

with open(input_path,) as f:
    students = f.read().title().split()
    
students.sort()

with open(output_path, "w") as f:
    f.write(f"{", ".join(students)} ")