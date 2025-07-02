input_path = "Input/numbers.txt"
output_path = "Output/output09.txt"
xonalar = {}

with open(input_path,) as f:
    numbers = list(map(int, f.read().split()))
    
for i in numbers:
    st = len(str(i))
    xonalar.update({st: []})

for i in numbers:
    st = len(str(i))
    xonalar[st].append(i)
    
with open(output_path,"w") as f:
    for key, valur in xonalar.items():
        f.write(f"{key} {valur}\n")