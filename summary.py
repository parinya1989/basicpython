# วนลูปผลรวม
print("----------------------------------------")
print("#Summation Program")
print("#Type 'exit' to end the program")
print("----------------------------------------")

# ตัวแปรเก็บผลรวม
sumdata = 0
count = 1

while True:
    data = input(f"Enter number {count}:")
    

    #ตรวจสอบป้อน Exit
    if data == "exit":
        break
    #หาผลรวม
    sumdata += int(data)
    count = count + 1

print(f"Sumdata value is {sumdata}")