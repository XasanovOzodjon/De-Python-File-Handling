input_path = "Input/students.txt"
output_path = "Output/output18.txt"

with open(input_path,) as f:
    students = f.read().title().split()

#foydalanuvchi ism kiritadai agar u fayda bo'lsa student mavjud deydi agar mavjud bulmasa uni faylga qo'shadi
name = input("Ism kiriting:")  
if name in students:
    print("Stududent mavjud")
else:
    students.append(name.title())

with open(output_path, "w") as f:
    f.write(f"{", ".join(students)} ")