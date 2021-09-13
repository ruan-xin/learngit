import EswinAPI
from ctypes import *

fib=EswinAPI.CEswinUsbDevice()
print(fib.c())
print(fib.c1(1,2))
s=c_ubyte(1)
n3=c_char_p(1)
n4=c_uint(1)
print(fib.Spi_RegRead(n4,byref(s)))

fib=CDLL(r'C:\Users\e0005202\Desktop\通讯\two\EswinAPI\x64\Release\EswinAPI.dll')
fib.c()

