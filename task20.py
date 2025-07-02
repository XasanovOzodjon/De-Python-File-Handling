input_path = "Input/grades.csv"
output_path = "Output/output20.txt"
dic = {}

with open(input_path,) as f:
    sss = f.read().split()

for i in sss:
    l = i.split(",")
    dic.update({l[0]:l[1]})
del dic["Name"]
    
baholar = list(map(int,dic.values()))
with open(output_path, "w") as f:
    f.write(f"o'rtacha baho: {round(sum(baholar)/ len(baholar))}\n")