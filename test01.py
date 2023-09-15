#default parameter การกำหนดค่าให้ตัวแปร ต้องกำหนดจากตัวท้ายสุดแล้วไล่ไปเรื่อยๆ ห้ามกำหนดข้ามตัว
def funcA(x, y = 20, z = 10) :
    print(x + y + z)
    print('^_^')


funcA(10, 20)
funcA(5, 6, 7)
funcA(555)