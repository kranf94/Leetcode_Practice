class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_num= [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman_list= ["M","CM","D","CD","C","XC","L","XL" ,"X","IX","V","IV","I"]
        
        list = ''
        for i in range (0,len(roman_num)) :
            while num >= roman_num[i]:
               num -= roman_num[i]
               list += roman_list[i]
        return list
        