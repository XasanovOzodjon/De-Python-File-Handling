input_path = "Input/numbers.txt"
output_path = "Output/output04.txt"

with open(input_path,) as f:
    numbers = list(map(int, f.read().split()))
    

with open(output_path, "w") as f:
    for i in numbers:
        if i % 2 == 0:
            f.write(f"{i}, ")