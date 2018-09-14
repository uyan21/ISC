# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 02:39:59 2018

@author: 김연덕
"""

from module.oneTimePad import OTP
def main():
    plain=input("입력: ")
    plainlen=len(plain.encode('utf-8'))
    while plainlen<4 or plainlen>100:
        print("%dByte 4Byte~100Byte 범위에서 입력하세요.\n"%int(plainlen))
        plain=input("입력: ")
        plainlen=len(plain.encode('utf-8'))
        
    f=open("Password.txt","at",encoding='utf-8')
    Object=OTP(plain,255)
    cypher=Object.enCode()
    decypher=Object.deCode()
    otp=Object.printOtp()
    f.write("%s %s %s %s\n"%(plain,otp,cypher,decypher))
    print('done')
    print("%dByte"%plainlen)
    f.close()
    del Object
if __name__=="__main__":
    main()