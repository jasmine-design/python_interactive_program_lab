import random

class Nine_Coins:
    
    def __init__(self, decimal):
        self.decimal = decimal
 
    def decimal_to_binary(self):
        '''change decimal into binary'''
        binary_num = bin(self.decimal)[2:]  
        num = 9 - len(binary_num)
        for x in range(num):
            binary_num = '0'+ binary_num
        return binary_num
    
    def binary_to_coin(self):
        '''change binary into coin'''
        coin = Nine_Coins.decimal_to_binary(self)
        coin = coin.replace("0", "H")
        coin = coin.replace("1", "T")
        return coin
        
    def __str__(self):
        binary = Nine_Coins.decimal_to_binary(self)
        return "binary: {} and decimal: {}".format(binary, self.decimal)
    
    def __repr__(self):
        coin = Nine_Coins.binary_to_coin(self)
        return "Nine_Coins: {} ".format(coin) 
    
    def toss(self):
        self.decimal = random.randint(1, 512)