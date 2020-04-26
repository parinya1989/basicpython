number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Jana', 'Wasan']
mixed = [10, 25, True, 'Parinya']

#การเข้าถึงสมาชิกใน List
print(number[3])
print(name[2])
print(mixed[2],mixed[3])

#การนับจำนวนสมาชิกใน List
print("สมาชิกทั้งหมดของ number=", len(number))

#การสร้าง List แบบวว่าง (empty list)
data =[]

#การเพิ่มสมาชิกเข้าไปใน list ว่าง
data.append(10)
data.append(15)
data.append(20)

print(data)

#การอัพเดตสมาชิกใน list

data[1] = 12
print(data)

#ฟังก์ชั่นวนลูปอ่านสมาชิกทั้งหมด
for n in number:
    print(n)

#Loop หาผลรวม
sum = 0
for num in number:
    sum += num

print(sum)