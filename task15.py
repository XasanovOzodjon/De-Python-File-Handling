input_path = "Input/students.txt"
output_path = "Output/output15.txt"

with open(input_path,) as f:
    students = f.read().title().split()
    

with open(output_path, "w") as f:
    for i in students:
        f.write(f"{i} = {len(i)}ta xarf\n")