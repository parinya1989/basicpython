scores = {
    'john': 1200,
    'pobpy': 2000,
    'janny': 4200
}

print(scores)
print(scores['pobpy'])

# เพิ่มสมาชิกใหม่เข้า dictionary
scores['roger'] = 3200

print(scores)

# การสร้าง dic ว่าง
points = {}

# เพิ่มค่าเข้า dic ว่าง
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)

# การ loop อ่านสมาชิกของ dic ออกมา
for key, value in scores.items():
    print(key, value)
