input_path = "Input/numbers.txt"
output_path = "Output/output10.txt"

with open(input_path,) as f:
    numbers = list(map(int, f.read().split()))
    

numbers.sort()
with open(output_path, "w") as f:
    for i in numbers:
        f.write(f"{i}, ")