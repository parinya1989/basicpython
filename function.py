# การสร้างฟังก์ชั่นแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")

# สร้างฟังก์ชั่นแบบมีการ return value


def area(width, heigth):
    total = width * heigth
    return total


# เรียกใช้งานฟังก์ชั่น hello()
hello("Parin")

# เรียกใช้งานฟังก์ชั่น area
print(area(5, 8))
print("พื้นที่ทั้งหมดคือ", area(15, 8.5))


# ฟังก์แบบมีค่าเริ่มต้น
def shoe_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Lang: {lang}")


# เรียกใช้งาน show_info
shoe_info()
shoe_info('Parinya', 12000, 'PHP')
