input_path = "Input/grades.csv"
output_path = "Output/output22.txt"
dic = {}

with open(input_path,) as f:
    sss = f.read().split()

for i in sss:
    l = i.split(",")
    if l[0] != "Name":
        dic.update({l[0]:l[1]})

    
alochilar = []
for key, value in dic.items():
    if value == 5:
        alochilar.append(key)


with open(output_path, "w") as f:
    f.write(f"5 olgan o'quvchilar: {'.'.join(alochilar)}")