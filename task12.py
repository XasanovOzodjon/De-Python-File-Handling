input_path = "Input/students.txt"
output_path = "Output/output12.txt"

with open(input_path,) as f:
    students = f.read().split()
    
count = len(students)
with open(output_path, "w") as f:
    f.write(f"{", ".join(students)} = {count}ta ism")