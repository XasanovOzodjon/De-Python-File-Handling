input_path = "Input/numbers.txt"
output_path = "Output/output06.txt"

with open(input_path,) as f:
    numbers = list(map(int, f.read().split()))
    

with open(output_path, "w") as f:
    for i in numbers:
        if i % 2 == 1:
            f.write(f"{i}, ")