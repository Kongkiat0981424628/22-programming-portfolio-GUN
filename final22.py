"""

โปรแกรมคำนวณเกรดจากคะแนน(A/B/C/D)
I : score = คะแนนสอบ (0–100)
P : score >= 80 เกรด A / 70-79 เกรด B / 60-69 เกรด C  / 50-59 เกรด D / 0-50 เกรด F
o : ช่วงคะแนนที่ได้ เกรดที่ได้
ตัวแปรที่ใช้ score int / float เก็บคะแนน grade string เกรด

"""
print("โปรแกรมคำนวณเกรดจากคะแนน(A/B/C/D)")
print("I : score = คะแนนสอบ (0–100)")
print("P : score >= 80 เกรด A / 70-79 เกรด B / 60-69 เกรด C  / 50-59 เกรด D / 0-50 เกรด F")
print("o : ช่วงคะแนนที่ได้ เกรดที่ได้")
print("ตัวแปรที่ใช้ score int / float เก็บคะแนน grade string เกรด")
# รับค่าคะแนนจากผู้ใช้
score = float(input("กรอกคะแนนของคุณ: "))

# ตรวจสอบและคำนวณเกรด
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

# แสดงผลลัพธ์
print("คะแนนของคุณคือ:", score)
print("เกรดที่ได้คือ:", grade)

