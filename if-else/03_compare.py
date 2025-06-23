num_1 = 10
num_2 = 20

# print(f"{num_1 <= num_2}")

# name_1 = "apple"
# name_2 = "banana"

# print(f"{name_1 > name_2}")
fruits = ["apple","banana","papaya","orange"]
find_fruits = input(str("ใส่ชื่อรายการที่ค้นหา :"))
if find_fruits in fruits:
    print(f"มี {find_fruits} อยู่ในรายการ")
else:
    print(f"ไม่มี {find_fruits} อยู่ในรายการ")
    
