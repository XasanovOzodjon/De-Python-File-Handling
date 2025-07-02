input_path = "Input/students.txt"
output_path = "Output/output17.txt"

with open(input_path,) as f:
    students = f.read().title().split()
    

with open(output_path, "w") as f:
    for i in students:
        if i.startswith("A"):
            f.write(f"{i}, ")