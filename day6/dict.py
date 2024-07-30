studentMarks = {}

marks = {"Amber": 85, "Salah": 65, "Syed": 95, "Syed": 80, "Syed": 70, "Char": 75}
print(marks)

print(marks["Salah"])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Amber": 95, "Salah": 85})
print(marks.get("Salah2"))
print(marks["Salah2"])