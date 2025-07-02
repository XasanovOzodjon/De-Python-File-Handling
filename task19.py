input_path = "Input/grades.csv"
output_path = "Output/output19.txt"
dic = {}

with open(input_path,) as f:
    sss = f.read().split()

for i in sss:
    l = i.split(",")
    dic.update({l[0]:l[1]})
    
with open(output_path, "w") as f:
    for key,value in dic.items():
        f.write(f"ism: {key}, baho: {value}\n")