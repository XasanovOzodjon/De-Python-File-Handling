input_path = "Input/students.txt"
output_path = "Output/output16.txt"

with open(input_path,) as f:
    students = f.read().title().split()
    

with open(output_path, "w") as f:
    for i in students:
        if len(i) >= 5:
            f.write(f"{i} = {len(i)}ta xarf\n")