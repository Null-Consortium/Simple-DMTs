from os import remove
from re import L
from Conversions import *
from openpyxl import Workbook
import Items

    
class AlphaNum:
    """Create ways of getting certain values from Alphanumeric text"""

    def __init__(self,text): 
        
        self.data = Items.Get_Items(text)
        self.L = []
        

    def Get_NUMS(self):
        """Loop through symbols in text and get numeric values"""
        numbers = '1234567890'
        n = 0
        List_Nums = []
        while n in range(len(self.data)):
            accepted = []
            for chr in self.data[n]:
                if chr in list(numbers) and self.data[n] != '':
                    accepted.append(chr)
                else:
                    pass
            List_Nums.append(convert(accepted))
            for chr in accepted:
                 accepted.remove(chr)    
            n += 1
        self.L.append(List_Nums)
        return self.L[0]

  
    def Get_ALPHA(self):
        """Loop through symbols in text and get alphabet values"""
        alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        n = 0
        List_Alpha = []
        while n in range(len(self.data)):
            alphas = []
            for chr in self.data[n]:
                if chr in list(alphabet):
                    alphas.append(chr)
                else:
                    pass
            List_Alpha.append(convert(alphas))
            for chr in alphas:
                alphas.remove(chr)
            n += 1
        self.L.append(List_Alpha)
        return self.L[1]

    def Get_OTHERS(self):
        """Loop through symbols in text and get non-tradtional values"""
        numbers = '1234567890'
        alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        numeric = list(numbers)
        alpha = list(alphabet)
        n = 0
        while n in range(len(self.data)):
            others = []
            for chr in list(self.data[n]):
                if chr in numeric:
                    pass
                elif chr in alpha:
                    pass
                else:
                    others.append(chr)
            print(convert(others))
            for chr in others:
                others.remove(chr)
    def upload(self,Book=None,):
        wb = Workbook()
        ws1 = wb.active
        for i in range(len(self.L[0])):
            for j in range(len(self.L)): 
                _ = ws1.cell(column= j+1, row=i+1, value=self.L[j][i])
            #ws1.append([listA[row]])
        wb.save(r"{Book}.xlsx")
        
        
        
# ==== vestigial code ====
#class Cell_Hoping:
 #   """Allow for common excel functions to be applied to displaced cells"""
  #  def __init__(self,Book): 
   #     
    #    self.data = Items.Get_Items()
     #   self.Book = Book
      #  self.L = []

    #def repeat_txt_v(self,txt,count, step=0):
     #   """append data to worksheet in every cell vertically from column _"""
      #  text = []
        #n = 0
       # while n in range(count):
         #   text.append(txt)
          #  n += 1
        #print(text)
            
       
    
   # def repeat_text_h(self,txt,count, step=0):
    #    pass
