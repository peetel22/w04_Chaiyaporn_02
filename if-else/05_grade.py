score = int(input("Enter your score : "))
'''
>90 A Very Good !!!
>80 B Good
>70 C Normal
>60 D Pass
<60 F Fool!!!
'''
if score >= 90:
    grade = "A"
    comment = "Very Good !!!"
elif score >=80:
    grade = "B"
    comment = "Good"
elif score >=70:
    grade = "C"
    comment = "Pass"
elif score <=60:
    grade = "F"
    comment = "Fool"
print(f"คะแนน : {score}")
print(f"ได้เกรด : {grade}")
print(f"ความคิดเห็น : {comment}")