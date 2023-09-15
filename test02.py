#return not values -การสิ้นสุดหรือการจบการทำงานของ Block Scope(ขอบเขตการทำงาน(แบบย่อหน้า)) การทำงานหหนึ่งๆ เมื่อมันถูกใช้งาน ทำงานจากซ้ายไปขวา บนลงล่าง
def func1( ) :
    print('AAA')
    print('BBB')
    return
    print('CCC')

def func2( x ) :
    return
    print(f'X is {x}')

func1( )
func2( 10 )