# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 02:14:18 2018

@author: 김연덕
"""

import random

class OTP:
    def __init__(self,plain,bit):
        self.plain=plain
        self.bit=bit
        self.__length=len(self.plain)
        self.__otp=[]
        self.cypher=""
        self.decypher=""
    
    def enCode(self):
        for i in range(self.__length):
            self.__otp.append(random.randint(0,self.bit))
        for i in range(self.__length):
            self.cypher+=chr(ord(self.plain[i])^self.__otp[i])
        return self.cypher
    
    def deCode(self):
        for i in range(self.__length):
           self.decypher+=chr(ord(self.cypher[i])^self.__otp[i])
        return self.decypher
   
    def printOtp(self):
       self.otp=self.__otp
       return self.otp
       
    def __del__(self):
        return 0
        
        

        
    
        