input_path = "Input/numbers.txt"
output_path = "Output/output05.txt"

with open(input_path,) as f:
    numbers = list(map(int, f.read().split()))
    
with open(output_path, "w") as f:
    f.write(f"{", ".join(list(map(str, numbers)))} sonlarning o'rtachasi: {sum(numbers)/ len(numbers)}")