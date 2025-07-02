input_path = "Input/grades.csv"
output_path = "Output/high_scores.csv"
dic = {}

with open(input_path,) as f:
    sss = f.read().split()

for i in sss:
    l = i.split(",")
    if l[0] != "Name":
        dic.update({l[0]:l[1]})




with open(output_path, "w") as f:
    for key, value in dic.items():
        if value == 5:
            f.write(f"{key},{value}")