input_path = "Input/grades.csv"
output_path = "Output/output21.txt"
dic = {}

with open(input_path,) as f:
    sss = f.read().split()

for i in sss:
    l = i.split(",")
    dic.update({l[0]:l[1]})
del dic["Name"]
    

ismlar = list(dic.keys())
baholar = list(map(int,dic.values()))

index = baholar.index(max(baholar))


with open(output_path, "w") as f:
    f.write(f"Eng yuqori balni: {ismlar[index]} olgan")