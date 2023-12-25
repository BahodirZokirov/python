# def common_ground(s1,s2):
#     lt = []
#     s2 = s2.split ()
#     s1 = s1.split ()
#     for i in s2:
#         for j in s1:
#
from time import sleep, perf_counter


import asyncio
# async def foo ():
#     print ('boshlandi')
#     await asyncio.sleep (1)
#     print ("tugadi")
#
#
# async def time():
#     await asyncio.gather(foo(), foo(), foo(), foo())
#
# asyncio.run(time())









# async def foo ():
#     print ("boshlandi")
#     await asyncio.sleep(2)
#     print ("tugadi")
#
#
# async def main ():
#     await asyncio.gather(foo(), foo(), foo(), foo())
#
# asyncio.run(main())


                            # Funksiya qaytaradigan mallumotlarni umumiy hajmini chiqaradigan dekorator tuzing


import sys
def sizer_func (original_function):
    def wrapper_function (*args):
        original = original_function(*args)
        return sys.getsizeof(original)
    return wrapper_function


def original_f (a):
    return a


a =[1, 2]
b =[1, 2, 3, 4]
c =[1, 2, 3, 4]
d =[2, 3, 1, 4, 66, 54, 45, 89]

k = sizer_func(original_f)
print (k(d))

# 80
# 96
# 96
# 128
#

print (sys.getsizeof(d))