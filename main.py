# import ทั้งหมดในฟังก์ชั่นใน Module
# import numbers

# inport มาบางฟังก์ชั่น
# from numbers import factorial

#import ทุกฟังก์ชั่น
# from numbers import*

# import และเปลี่ยนชื่อฟังชั่น (นามแฝง)
from numbers import factorial as fa, fibonacci as fi

# เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))


print(fa(5))
print(fi(100))
