# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 04:49:17 2018

@author: 김연덕
"""

from module.oneTimePad import OTP
def main():
    rf=open("Word.txt","rt",encoding='utf-8')
    f=open("WordOTP.txt","wt",encoding='utf-8')
    for plain in rf.readlines():
        plain=plain.rstrip()
        Object=OTP(plain,255)
        cypher=Object.enCode()
        decypher=Object.deCode()
        otp=Object.printOtp()
        f.write("%s %s %s %s\n"%(plain,otp,cypher,decypher))
    print('done')
    f.close()
if __name__=="__main__":
    main()