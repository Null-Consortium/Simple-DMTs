import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema as extrema

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst 

#______________________________________________________________________________________________
#========            888           88        88888888      888888           88888          ===========
#========           88 88          88     888            88      88        88              ===========
#========          88   88         88     888            88      88        88888           ===========
#========         888888888        88     888    8888    88      88          8888          ===========
#========        888     888       88       88888888       888888         888888           ===========
#_____________________________________________________________________________________________
# see " Tests" for images collected whilst producing some of Navi's current/to-be features 
#IMPORTANT: In the demo the algos only be applied to past data until configuration for realtime data is complete

#fig, ax = plt.subplots() 

class In_Market:
    """Get Statistics of market fluctuations"""
    def __init__(self,sheet=r"C:\Users\AAske\Downloads\Historical Market Data - NASDAQ_GOOG (1).csv"):
        self.dataset = pd.read_csv(sheet)
        # .iloc (lets us get column data)
        # .iloc

    def date(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,0:1]):
            for i in self.dataset.iloc[:,0:1].values[n]:
                L.append(i)
            n+=1
        return L
    
    def previous_close(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,1:2]):
            for i in self.dataset.iloc[:,1:2].values[n]:
                L.append(i)
            n+=1
        return L
    def volume(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,2:3].values):
            for i in self.dataset.iloc[:,2:3].values[n]:
                L.append(i)
            n+=1
        return L
    def high(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,3:4].values):
            for i in self.dataset.iloc[:,3:4].values[n]:
                L.append(i)
            n+=1
        return L      
    def low(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,4:5].values):
            for i in self.dataset.iloc[:,4:5].values[n]:
                L.append(i)
            n+=1
        return L
class Patterns: # return only loc extremas that satifiy condition list, (NAVI will supply the x varible "ticks")
    """Chart Patterns typically associated with market trends"""
    def __init__(self,duration,cutoff):
        """upload initial parameters for each company to start geting stats and condtions from database"""
        self.duration = duration
        self.close = In_Market().previous_close()
        self.cutoff=cutoff

    
    def HS_Above(previous_prices,start,end,cutoff=0.05,show =False):
        """Return True if there is a head shoulder pattern above and/or below neckline
        through previous (duration days) prices """ 
        previous_prices = np.array(previous_prices)[start:end]
        Head_Shoulder_Pattern = [False]
        loc = []
        price_at_extremes = []
        date = [] #replace this with the actual date 
        for i in range(len(previous_prices)):
            date.append(i)
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) 
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        p = previous_prices
        Find = True
        try:
            min1 = local_min[0]
            max1 = local_max[0]
            min2 = local_min[0]
            max2 = local_max[0]
            min3 = local_min[0]
            max3 = local_max[0]
            min4 = local_min[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False,False,False]
        displacment = 0
        iteration = 7
        while Find:
            if min1 and min2 and min3 and min4 != local_min[-1] and max1 and max2 and max3 != local_max[-1]:
                if p[max1]>p[min1]*cutoff+p[min1] and max1>min1:
                    conditions[0] = True
                else:
                    try:import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema as extrema

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst 

#______________________________________________________________________________________________
#========            888           88        88888888      888888           88888          ===========
#========           88 88          88     888            88      88        88              ===========
#========          88   88         88     888            88      88        88888           ===========
#========         888888888        88     888    8888    88      88          8888          ===========
#========        888     888       88       88888888       888888         888888           ===========
#_____________________________________________________________________________________________
# some code is marked with hashtag for testing/future updating purposes 

#fig, ax = plt.subplots() 

class In_Market:
    """Get Statistics of market fluctuations"""
    def __init__(self,sheet=r"C:\Users\AAske\OneDrive\Desktop\Archetecture\Excel Sheets\TSLA2021_2022.csv"): #make this based on user input
        self.dataset = pd.read_csv(sheet)

    def date(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,0:1]):
            for i in self.dataset.iloc[:,0:1].values[n]:
                L.append(i)
            n+=1
        return L
    
    def previous_close(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,1:2]):
            for i in self.dataset.iloc[:,1:2].values[n]:
                L.append(i)
            n+=1
        return L
    def volume(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,2:3].values):
            for i in self.dataset.iloc[:,2:3].values[n]:
                L.append(i)
            n+=1
        return L
    def high(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,3:4].values):
            for i in self.dataset.iloc[:,3:4].values[n]:
                L.append(i)
            n+=1
        return L      
    def low(self):
        L = []
        n = 0
        while n != len(self.dataset.iloc[:,4:5].values):
            for i in self.dataset.iloc[:,4:5].values[n]:
                L.append(i)
            n+=1
        return L
class Patterns: # return only loc extremas that satifiy condition list, (NAVI will supply the x varible "ticks")
    """Chart Patterns typically associated with market trends"""
    def __init__(self,duration,cutoff):
        """upload initial parameters for each company to start geting stats and condtions from database"""
        self.duration = duration
        self.close = In_Market().previous_close()
        self.cutoff=cutoff

    
    def HS_Above(previous_prices,start,end,cutoff=0.05,show =False):
        """Return True if there is a head shoulder pattern above and/or below neckline
        through previous (duration days) prices """ #note: we'll be looking at daily price changes until configure for realtime data
        previous_prices = np.array(previous_prices)[start:end]
        Head_Shoulder_Pattern = [False]
        loc = []
        price_at_extremes = []
        date = [] #replace this with the actual date 
        for i in range(len(previous_prices)):
            date.append(i)
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) 
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        p = previous_prices
        Find = True
        try:
            min1 = local_min[0]
            max1 = local_max[0]
            min2 = local_min[0]
            max2 = local_max[0]
            min3 = local_min[0]
            max3 = local_max[0]
            min4 = local_min[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False,False,False]
        displacment = 0
        iteration = 7
        while Find:
            if min1 and min2 and min3 and min4 != local_min[-1] and max1 and max2 and max3 != local_max[-1]:
                if p[max1]>p[min1]*cutoff+p[min1] and max1>min1:
                    conditions[0] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7       
                            continue                        
                        else:
                            displacment += 1
                            max1 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min1] < p[min2]< p[max1] and min2>max1:
                    conditions[1] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            min2 = local_min[displacment]
                    except IndexError:
                        break
                if p[max2] > p[max1] and max2>min2:
                    conditions[2] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1 
                            max2 =local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min3]<p[min2]<p[max2] and min3>max2:
                    conditions[3] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1 
                            min3 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                # ==============experimentl ==================
                peak1_d =  np.sqrt((p[min2]-p[max1])**2+(max1-min2)**2) 
                peak3_d = np.sqrt((p[max3]-p[min3])**2+(max3-min3)**2)   
                dif_per = abs(peak3_d-peak1_d)/peak1_d  
                # dif_per < % distance variation between peaks
                #=============================================
                if p[max3]>=p[max1] and p[min2]>p[min3] and max3>min3: 
                    conditions[4] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1
                            max3 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min4] <p[min3]+p[min3]*0.05 and min4>max3:
                    conditions[5] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1
                            min4 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                
                if all(conditions) == True:
                    #print("Head and Shoulder Pattern (Above)")
                    Head_Shoulder_Pattern[0] = True
                    break
            else:
                break
        
        #print(f"HS_Above:  {conditions}")
        location = [[],[]]
        if all(conditions) == True:
            location[0].append(min1)
            location[0].append(max1)
            location[0].append(min2)
            location[0].append(max2)
            location[0].append(min3)
            location[0].append(max3)
            location[0].append(min4)
            location[1].append(p[min1])
            location[1].append(p[max1])
            location[1].append(p[min2])
            location[1].append(p[max2])
            location[1].append(p[min3])
            location[1].append(p[max3])
            location[1].append(p[min4])
            # ====================================================
        if show == True and all(conditions) == True:
            #plt.plot(date,previous_prices)
            plt.scatter(loc,price_at_extremes,color="black",linewidths=0.2)
            plt.plot(location[0],location[1],color="red")
            #plt.show()
            return location[0], location[1]
        elif all(conditions):
            return location[0], location[1]
        else:
            return False


    def HS_Below(previous_prices,start,end,cutoff=0.05,show =False):
        """Return True if there is a head shoulder pattern below a neckline
        through previous (duration days) prices """ #note: we'll be looking at daily price changes until configure for realtime data
        previous_prices = np.array(previous_prices)[start:end]
        Head_Shoulder_Pattern = [False]
        loc = []
        price_at_extremes = []
        date = [] #replace this with the actual date 
        for i in range(len(previous_prices)):
            date.append(i)
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) 
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        p = previous_prices
        Find = True
        try:
            max1 = local_max[0]
            min1 = local_min[0]
            max2 = local_max[0]
            min2 = local_min[0]
            max3 = local_max[0]
            min3 = local_min[0]
            max4 = local_max[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False,False,False]
        displacment = 0
        iteration = 7
        while Find == True:
            if min1 and min2 and min3 != local_min[-1] and max1 and max2 and max3 and max4 != local_max[-1]:
                if p[min1]<p[max1]-p[max1]*cutoff and max1<min1:
                    conditions[0] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7       
                            continue
                            
                        else:
                            displacment += 1
                            min1 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                if p[max1] < p[max2] and  min1<max2:
                    conditions[1] = True

                elif p[max2] < p[max1] and min1<max2:
                    conditions[1] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            max2 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min1]-p[min1]*cutoff > p[min2] and max2<min2:
                    conditions[2] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            min2 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                if p[max3] >p[max2] and min2<max3:
                    conditions[3] = True
                elif p[max3] < p[max2] and min2>max3:
                    conditions[3] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            max3 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min2] < p[min1] <p[min3] and min3>max3:
                    conditions[4] = True
                elif p[min2] <p[min3] <p[min1]  and min3>max3:
                    conditions[4] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            min3=local_min[displacment]
                            continue
                    except IndexError:
                        break
                if p[max4] > p[min1] and max4>min3:
                    conditions[5] = True
                elif p[max4] > p[min3] and max4>min3:
                    conditions[5] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            max4 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if all(conditions) == True:
                    #print("Head and Shoulder Pattern (Below)")
                    Head_Shoulder_Pattern[0] = True
                    break
            else:
                break
        
        #print(f"HS beloow{conditions}")
        location = [[],[]]
        if all(conditions) == True:
            location[0].append(max1)
            location[0].append(min1)
            location[0].append(max2)
            location[0].append(min2)
            location[0].append(max3)
            location[0].append(min3)
            location[0].append(max4)
            location[1].append(p[max1])
            location[1].append(p[min1])
            location[1].append(p[max2])
            location[1].append(p[min2])
            location[1].append(p[max3])
            location[1].append(p[min3])
            location[1].append(p[max4])
        if show == True and all(conditions) == True:
            #plt.plot(date,previous_prices)
            #plt.scatter(location[0],location[1],color="black",linewidths=0.2)
            plt.plot(location[0],location[1],color="pink")
            return location[0],location[1]
        elif all(conditions) == True:
            return location[0],location[1]
        else:
            return False

    def Double_T(previous_prices,start,end=None,cutoff=0.05,show=False):
        """Within an subset of previuos prices, 
        take a set of five local extremes - three minimums, two maximums - such that the price at
        those points satifies the condition of a double pattern"""
        previous_prices = np.array(previous_prices)[start:end]
        DoubleB = [False]
        loc = []
        price_at_extremes = []
        date = [] #replace this with the actual date 
        for i in range(len(previous_prices)):
            date.append(i)
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) 
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        p = previous_prices
        variation_allowance = 0.2
        Find = True
        try:
            i = local_min[0]
            k = local_max[0]
            l = local_min[0]
            m = local_max[0]
            n = local_min[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False]
        displacment = 0
        iteration = 5
        while Find == True:
            if i and l and n != local_min[-1] and k and m != local_max[-1]:
                if (p[k]/p[i])-1 >= cutoff and k > i: 
                    conditions[0]=True 
                    
                else:
                    try:
                        if displacment >= iteration:
                            #shift all previuos points by one outside loop by seting each outer step to last inloop step
                            #shift displacement length to greatest indexed local extreme + 5
                            #reset all in loop steps because it will only increment to eqaul new displacement 
                            i = local_min[displacment]
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            k = local_max[0+displacment]
                            continue
                    except IndexError:
                        break
                
                if p[m] >=p[k]-p[k]*0.1 and p[m] <= p[k]+p[k]*0.1 and p[m]>p[i] and m>k :
                    conditions[1] = True
                    iteration = displacment
                else:
                    try:
                        if displacment >= iteration:
                            i = local_min[displacment]
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            m = local_max[0+displacment]
                            continue
                    except IndexError:
                        break
                # ==============experimentl ==================
                #peak1_d =  np.sqrt((p[l]-p[k])**2+(l-k)**2) 
                #peak2_d = np.sqrt((p[m]-p[l])**2+(m-l)**2)   
                #dif_per = abs(peak2_d-peak1_d)/peak1_d   
                # if dif_per <= variation_allowance and m > l > k:
                #    conditions[2] = True
                #===========================================  
                i_allowance = p[i]-p[i]*0.5
                if p[l] >= i_allowance and p[l] < p[k] and m > l > k:
                        conditions[2] = True
                        iteration = displacment

                else:
                    try:
                        if displacment >= iteration:
                            i = local_min[displacment]
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            l = local_min[+displacment]
                            continue
                    except IndexError:
                        break
            
                if p[n] <= p[l] and p[m] >= p[n]*cutoff+p[n] and n>m:
                    conditions[3]=True
                    iteration = displacment
                   
                else:
                    try: 
                        if displacment >= iteration:
                            i = local_min[displacment] 
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else:
                            displacment+=1
                            n = local_min[displacment]
                    except IndexError:
                        break
                if all(conditions):
                    DoubleB[0]=True  
                    break                    
            else:
                break
        print(f"DT: {conditions}")
        location = [[],[]]
        if conditions[0]:
            location[0].append(i)
            location[0].append(k)
            location[1].append(p[i])
            location[1].append(p[k])
        if conditions[1]:
            location[0].append(l)
            location[1].append(p[l])
        if conditions[2]:
            location[0].append(m)
            location[1].append(p[m])
        if conditions[3]:
            location[0].append(n)
            location[1].append(p[n])

        if show == True and all(conditions):
            if len(loc) >= 5:
                #plt.plot(date,previous_prices)
                #plt.scatter(loc[:len(location[0])],price_at_extremes[:len(location[1])],color="black",linewidths=0.2)
                plt.plot(location[0],location[1],color="red")
                #plt.show()
                return loc, price_at_extremes, location[0], location[1]
        elif all(conditions):
            return location[0], location[1]
        else:
            return False
        #print(f"{0} or {10} is/are not a valid local extreme index")
    
    def Double_B(previous_prices,start,end,cutoff=0.05,show=False):
        """Within an subset of previuos prices, 
        take a set of five local extremes - three maximums, two minimums - such that the price at
        those points satifies the condition of a double pattern"""
        previous_prices = np.array(previous_prices)[start:end]
        DoubleB = [False]
        loc = []
        price_at_extremes = []
        date = [] #replace this with the actual date
        for i in range(len(previous_prices)):
            date.append(i)
        
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) #shitft to fit line
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        
        p = previous_prices
        variation_allowance = 0.1
        Find = True
        steps =[0,0,0,0,0]
        try:
            i = local_max[0]
            k = local_min[0]
            l = local_max[0]
            m = local_min[0]
            n = local_max[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False]
        displacment = 0
        iteration = 5
        while Find == True:
            if i and l and n != local_max[-1] and k and m != local_min[-1]:
                if p[k]<=p[i]-p[i]*cutoff and k > i: 
                    conditions[0]=True     
                else:
                    try:
                        if displacment >= iteration:
                            #shift all previuos points by one outside loop by seting each outer step to last inloop step
                            #shift displacement length to greatest indexed local extreme + 5
                            #reset all in loop steps because it will only increment to eqaul new displacement 
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]        
                            iteration += 5        
                            continue
                        else: 
                            displacment+=1
                            k = local_min[displacment]
                            continue
                    except IndexError:
                        break
                
                if p[m] >=p[k]-p[k]*0.1 and p[m] <= p[k]+p[k]*0.1 and p[m]<p[i] and m>k:
                    conditions[1] = True
                else:
                    try:
                        if displacment >= iteration:
                            #shift all previuos points by one outside loop by seting each outer step to last inloop step
                            #shift displacement length to greatest indexed local extreme + 5
                            #reset all in loop steps because it will only increment to eqaul new displacement 
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]         
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            m = local_min[displacment]
                            continue
                    except IndexError:
                        break
                 
                if p[l] >= p[i]+p[i]*0.1 and i<k<l<m:
                        conditions[2] = True
                else:
                    try:
                        if displacment >= iteration:
                            #shift all previuos points by one outside loop by seting each outer step to last inloop step
                            #shift displacement length to greatest indexed local extreme + 5
                            #reset all in loop steps because it will only increment to eqaul new displacement 
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]         
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            l = local_max[displacment]
                            continue
                    except IndexError:
                        break
                
                # define distance between each peak assuming a second peak accures
                if p[n] >= p[l]+p[l]*0.01  and n>m:
                    conditions[3]=True
                else:
                    try: 
                        if displacment >= iteration:
                            #shift all previuos points by one outside loop by seting each outer step to last inloop step
                            #shift displacement length to greatest indexed local extreme + 5
                            #reset all in loop steps because it will only increment to eqaul new displacement 
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]          
                            iteration += 5          
                            continue
                        else:
                            displacment+=1
                            n=local_max[displacment]
                            continue

                    except IndexError:
                        break
                if all(conditions):
                    DoubleB[0]=True  
                    break                   
            else:
                break
        print(f"DB:  {conditions}")
        location = [[],[]]
        if conditions[0]:
            location[0].append(i)
            location[0].append(k)
            location[1].append(p[i])
            location[1].append(p[k])
        if conditions[2]:
            location[0].append(l)
            location[1].append(p[l])
        if conditions[1]:   
            location[0].append(m)
            location[1].append(p[m])
        if conditions[3]:
            location[0].append(n)
            location[1].append(p[n])
        if show == True and all(conditions):
            if len(loc) > 5:
                plt.plot(date,previous_prices)
                plt.scatter(location[0],location[1],color="black",linewidths=0.2)
                plt.plot(location[0],location[1],color="red")
                return loc, price_at_extremes, location[0],location[1]
        elif all(conditions):
            return location[0],location[1]
        else:
            return False

class Indicators:
    """Formuals and Mesurments for estemating market momentum"""
    def __init__(self,close,start,end):
        self.start=start
        self.end = end
        self.close = close #In_Market().previous_close()
        self.volume = In_Market().volume()[self.start:self.end]
        self.RSI = []   #upload this to database
        pass
    def Unusual_Volume(self,sensivity=20,show=False):
        """see if each volume is more than a % of it previouse average"""
        volume = self.volume[self.start:self.end]
        x=[]
        for i in range(len(volume)):
            x.append(i)
        total_volume = sum(volume)
        proportion = []
        for i in volume:
            proportion.append(round(i/total_volume,7))
        
        pt_change = []
        unusual_volume =[]
        time_at_uv = []
        for i in range(len(proportion)-1):
            delta = proportion[i+1]-proportion[i]
            pt_change.append(round(delta,4))
        for i in range(len(pt_change)):
            if abs(pt_change[i]) > abs(sum(pt_change)/len(pt_change))*sensivity or abs(pt_change[i]) < abs(sum(pt_change)/len(pt_change))*sensivity < abs(sum(pt_change)/len(pt_change))*(1/sensivity):
                unusual_volume.append(volume[i+1])
                time_at_uv.append(x[i+1])
        if show == True:
            #ax.set_ylim(0,max(volume))
            plt.plot(x,volume)
            plt.scatter(time_at_uv,unusual_volume,color="purple")

        return unusual_volume[-1] #returns latets point with unusally volume for Navi


        

    def RSI_Index(self):
        """Return Relative Strength Index values within an interval
        of past price points"""
        if len(self.close) >= 15:
            prices = self.close[self.start:self.end]
            date = []
            for i in range(len(prices)):
                date.append(i)
            up_moves = []
            down_moves = []
            for i in range(1,len(prices)):
                if prices[i] - prices[i-1] > 0:
                    up_moves.append(prices[i])
                elif prices[i] - prices[i-1] <0:
                    down_moves.append(prices[i])
                else:
                    pass
            price_change_up =[]
            price_change_down = []
            for i in range(1,len(up_moves)):
                price_change_up.append(up_moves[i]-up_moves[i-1])
            for i in range(1,len(down_moves)):
                price_change_down.append(down_moves[i]-down_moves[i-1])
            
            if len(up_moves) != 0 and len(down_moves)!=0 and sum(price_change_down) != 0 and len(price_change_up) != 0:
                avgU = sum(price_change_up)/len(price_change_up)
                avgD = sum(price_change_down)/len(price_change_down)
                rs = abs(avgU/avgD)  #relative strength
                rsi = 100 - 100/(1+rs)
                return round(rsi,2)
            else:
                return 'NaN'
        else:
            return 'NaN'
        # write condtions of bullish/bearish market divergence

    def Exponetial_MAvg(self): #this smooths out the market into general trend and can help in the modifiyng of indicators 
        """Return exponetinal moving average in the data"""
        # start by computing the moving avg
        if self.end-self.start >= 15:
            prices = self.close
            #print(prices[0],previuos[-1])
            period =  self.end-self.start
            smoothing = 4.7 
            weight = smoothing/(period+1)
            EMA = [] 
            if len(prices) >0:
                EMA.append(sum(prices)/len(prices)) #initial  EMA 
                n = 1
                while prices[n-1] != prices[period-1]:
                    ema_n = prices[n]*(weight)+EMA[n-1]*(1-weight)
                    EMA.append(ema_n)
                    n+=1
                plt.plot()
                return EMA
            else:
                return 'NaN'
        else:
            return 'NaN'
        #========================UPGRADE to MACD===========================
        #MACD = []
        #n = 1
        #while EMA[n-1] != EMA[-1]:
        #    macd_n = (prices[n] - EMA[n])*weight+EMA[n-1]*(1-weight)
        #    MACD.append(macd_n)
        #    n+=1
        #==============================================
        
        

class Fundementals:
    """chose between P/E ratio, EPS ratio, and D/E ratio, as a moderation variable"""
    def PE_Ratio():
        pass
    def Earnings_per_shar():
        pass
    def DE_Ratio():
        pass   

#===functions for testing pattern alogos===
def T1():
    """Test RSI Plots"""
    results = []
    n = 70
    while n != 120:
        if n != 'NaN':
            results.append(Indicators(In_Market().previous_close(),0,n).RSI_Index())
        print(n)
        n+=1
    ticks = [i for i in range(len(results))]
    const = [50 for i in range(len(results))]
    #ax.set_ylim(0,100)
    plt.plot(ticks,results,color = "Gray")
    plt.plot(ticks,const,color="Black")
    plt.show()
def T2():
    """Test Volume"""
    Indicators(In_Market().previous_close(),0,100).Unusual_Volume(show=True)

def T3():
    """open plt and pattern"""
    start = 0
    end = 20
    course = len(In_Market().previous_close())
    ticks = [i for i in range(len(In_Market().previous_close()))]

    plt.show()
    while end != course:
        if Patterns.Double_T(In_Market().previous_close(),start,end) != False:
            a = Patterns.Double_T(In_Market().previous_close(),start,end)[0]
            b = Patterns.Double_T(In_Market().previous_close(),start,end)[1]
            plt.plot(ticks,In_Market().previous_close(),0,len(In_Market().previous_close()))
            plt.plot(a,b,color="red") 
            plt.show()
            start = end
            print(start) #checking for change
        else:
            end +=1
            print(end)

def T4():
    a = Patterns.HS_Below(In_Market().previous_close(),0,400)[0]
    b = Patterns.HS_Below(In_Market().previous_close(),0,400)[1]
    print(Patterns.HS_Below(In_Market().previous_close(),0,400))
    plt.plot(a,b,color="red")
    plt.scatter(a,b,color="black",linewidths=0.1)
    plt.show()

                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7       
                            continue
                            
                        else:
                            displacment += 1
                            max1 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min1] < p[min2]< p[max1] and min2>max1:
                    conditions[1] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            min2 = local_min[displacment]
                    except IndexError:
                        break
                if p[max2] > p[max1] and max2>min2:
                    conditions[2] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1 
                            max2 =local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min3]<p[min2]<p[max2] and min3>max2:
                    conditions[3] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1 
                            min3 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                # ==============experimentl ==================
                peak1_d =  np.sqrt((p[min2]-p[max1])**2+(max1-min2)**2) 
                peak3_d = np.sqrt((p[max3]-p[min3])**2+(max3-min3)**2)   
                dif_per = abs(peak3_d-peak1_d)/peak1_d  
                # dif_per < % distance variation between peaks
                #=============================================
                if p[max3]>=p[max1] and p[min2]>p[min3] and max3>min3: 
                    conditions[4] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1
                            max3 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min4] <p[min3]+p[min3]*0.05 and min4>max3:
                    conditions[5] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            min4 = local_min[displacment+3]
                            iteration += 7
                            continue
                        else:
                            displacment +=1
                            min4 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                
                if all(conditions) == True:
                    #print("Head and Shoulder Pattern (Above)")
                    Head_Shoulder_Pattern[0] = True
                    break
            else:
                break
        
        #print(f"HS_Above:  {conditions}")
        location = [[],[]]
        if all(conditions) == True:
            location[0].append(min1)
            location[0].append(max1)
            location[0].append(min2)
            location[0].append(max2)
            location[0].append(min3)
            location[0].append(max3)
            location[0].append(min4)
            location[1].append(p[min1])
            location[1].append(p[max1])
            location[1].append(p[min2])
            location[1].append(p[max2])
            location[1].append(p[min3])
            location[1].append(p[max3])
            location[1].append(p[min4])
            # ====================================================
        if show == True and all(conditions) == True:
            #plt.plot(date,previous_prices)
            #plt.scatter(loc,price_at_extremes,color="black",linewidths=0.2)
            #plt.plot(location[0],location[1],color="red")
            #plt.show()
            return location[0], location[1]
        
        return False


    def HS_Below(previous_prices,start,end,cutoff=0.05,show =False):
        """Return True if there is a head shoulder pattern below a neckline
        through previous (duration days) prices """ #note: we'll be looking at daily price changes until configure for realtime data
        previous_prices = np.array(previous_prices)[start:end]
        Head_Shoulder_Pattern = [False]
        loc = []
        price_at_extremes = []
        date = [] #replace this with the actual date 
        for i in range(len(previous_prices)):
            date.append(i)
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) 
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        p = previous_prices
        Find = True
        try:
            max1 = local_max[0]
            min1 = local_min[0]
            max2 = local_max[0]
            min2 = local_min[0]
            max3 = local_max[0]
            min3 = local_min[0]
            max4 = local_max[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False,False,False]
        displacment = 0
        iteration = 7
        while Find == True:
            if min1 and min2 and min3 != local_min[-1] and max1 and max2 and max3 and max4 != local_max[-1]:
                if p[min1]<p[max1]-p[max1]*cutoff and max1<min1:
                    conditions[0] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7       
                            continue
                            
                        else:
                            displacment += 1
                            min1 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                if p[max1] < p[max2] and  min1<max2:
                    conditions[1] = True

                elif p[max2] < p[max1] and min1<max2:
                    conditions[1] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            max2 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min1]-p[min1]*cutoff > p[min2] and max2<min2:
                    conditions[2] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            min2 = local_min[displacment]
                            continue
                    except IndexError:
                        break
                if p[max3] >p[max2] and min2<max3:
                    conditions[3] = True
                elif p[max3] < p[max2] and min2>max3:
                    conditions[3] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            max3 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if p[min2] < p[min1] <p[min3] and min3>max3:
                    conditions[4] = True
                elif p[min2] <p[min3] <p[min1]  and min3>max3:
                    conditions[4] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            min3=local_min[displacment]
                            continue
                    except IndexError:
                        break
                if p[max4] > p[min1] and max4>min3:
                    conditions[5] = True
                elif p[max4] > p[min3] and max4>min3:
                    conditions[5] = True
                else:
                    try:
                        if displacment >= iteration:
                            min1 = local_min[displacment]
                            max1 = local_max[displacment]
                            min2 = local_min[displacment+1]
                            max2 = local_max[displacment+1]
                            min3 = local_min[displacment+2]
                            max3 = local_max[displacment+2]
                            max4 = local_max[displacment+3]
                            iteration += 7
                            continue 
                        else:
                            displacment += 1
                            max4 = local_max[displacment]
                            continue
                    except IndexError:
                        break
                if all(conditions) == True:
                    #print("Head and Shoulder Pattern (Below)")
                    Head_Shoulder_Pattern[0] = True
                    break
            else:
                break
        
        #print(f"HS beloow{conditions}")
        location = [[],[]]
        if all(conditions) == True:
            location[0].append(max1)
            location[0].append(min1)
            location[0].append(max2)
            location[0].append(min2)
            location[0].append(max3)
            location[0].append(min3)
            location[0].append(max4)
            location[1].append(p[max1])
            location[1].append(p[min1])
            location[1].append(p[max2])
            location[1].append(p[min2])
            location[1].append(p[max3])
            location[1].append(p[min3])
            location[1].append(p[max4])
        if show == True and all(conditions) == True:
            #plt.plot(date,previous_prices) 
            #plt.scatter(loc,price_at_extremes,color="black",linewidths=0.2)
            #plt.plot(location[0],location[1],color="red")
            #plt.show()
            return location[0],location[1]
        return False

    def Double_T(previous_prices,start,end,cutoff=0.01,show=False):
        """Within an subset of previuos prices, 
        take a set of five local extremes - three minimums, two maximums - such that the price at
        those points satifies the condition of a double pattern"""
        previous_prices = np.array(previous_prices)[start:end]
        DoubleB = [False]
        loc = []
        price_at_extremes = []
        date = [] 
        for i in range(len(previous_prices)):
            date.append(i)
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) 
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        p = previous_prices
        variation_allowance = 0.1
        Find = True
        try:
            i = local_min[0]
            k = local_max[0]
            l = local_min[0]
            m = local_max[0]
            n = local_min[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False]
        displacment = 0
        iteration = 5
        while Find == True:
            if i and l and n != local_min[-1] and k and m != local_max[-1]:
                if (p[k]/p[i])-1 >= cutoff and k > i: 
                    conditions[0]=True     
                else:
                    try:
                        if displacment >= iteration:
                            #shift all previuos points by one outside loop by seting each outer step to last inloop step
                            #shift displacement length to greatest indexed local extreme + 5
                            #reset all in loop steps because it will only increment to eqaul new displacement 
                            i = local_min[displacment]
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            k = local_max[0+displacment]
                            continue
                    except IndexError:
                        break
                
                if p[m] >=p[k]-p[k]*0.1 and p[m] <= p[k]+p[k]*0.1 and p[m]>p[i] and m>k :
                    conditions[1] = True
                else:
                    try:
                        if displacment >= iteration:
                            i = local_min[displacment]
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            m = local_max[0+displacment]
                            continue
                    except IndexError:
                        break
                # ==============experimentl ==================
                #peak1_d =  np.sqrt((p[l]-p[k])**2+(l-k)**2) 
                #peak2_d = np.sqrt((p[m]-p[l])**2+(m-l)**2)   
                #dif_per = abs(peak2_d-peak1_d)/peak1_d   
                #===========================================  
                i_allowance = p[i]-p[i]*0.5
                if p[l] >= i_allowance and p[l] < p[k] and m > l > k:
                        conditions[2] = True
                else:
                    try:
                        if displacment >= iteration:
                            i = local_min[displacment]
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            l = local_min[+displacment]
                            continue
                    except IndexError:
                        break
                
      

                if p[n] <= p[l] and p[m] >= p[n]*cutoff+p[n] and n>m:
                    conditions[3]=True
                else:
                    try: 
                        if displacment >= iteration:
                            i = local_min[displacment]
                            k = local_max[displacment]
                            l = local_min[displacment+1]      
                            m = local_max[displacment+1]   
                            n = local_min[displacment+2]        
                            iteration += 5          
                            continue
                        else:
                            displacment+=1
                            n = local_min[displacment]
                    except IndexError:
                        break
                if all(conditions):
                    DoubleB[0]=True  
                    break                    
            else:
                break
        #print(f"DT: {conditions}")
        location = [[],[]]
        if conditions[0]:
            location[0].append(i)
            location[0].append(k)
            location[1].append(p[i])
            location[1].append(p[k])
        if conditions[1]:
            location[0].append(l)
            location[1].append(p[l])
        if conditions[2]:
            location[0].append(m)
            location[1].append(p[m])
        if conditions[3]:
            location[0].append(n)
            location[1].append(p[n])

        if show == True and all(conditions):
            if len(loc) >= 5:
                #plt.scatter(loc,price_at_extremes,color="black",linewidths=0.2)
                #plt.plot(location[0],location[1],color="red")
                #plt.show()
                return loc, price_at_extremes, location[0], location[1]
        else:
            return False
       
    
    def Double_B(previous_prices,start,end,cutoff=0.01,show=False):
        """Within an subset of previuos prices, 
        take a set of five local extremes - three maximums, two minimums - such that the price at
        those points satifies the condition of a double pattern"""
        previous_prices = np.array(previous_prices)[start:end]
        DoubleB = [False]
        loc = []
        price_at_extremes = []
        date = [] #replace this with the actual date
        for i in range(len(previous_prices)):
            date.append(i)
        
        local_max = extrema(previous_prices,np.greater)[0]
        local_min = extrema(previous_prices,np.less)[0]
        for i in local_max:
            loc.append(i) #shitft to fit line
        for i in local_min:
            loc.append(i)
        loc.sort()
        for i in loc:
            price_at_extremes.append(previous_prices[i])
        
        p = previous_prices
        variation_allowance = 0.1
        Find = True
        steps =[0,0,0,0,0]
        try:
            i = local_max[0]
            k = local_min[0]
            l = local_max[0]
            m = local_min[0]
            n = local_max[0]
        except IndexError:
            Find = False
        conditions = [False,False,False,False]
        displacment = 0
        iteration = 5
        while Find == True:
            if i and l and n != local_max[-1] and k and m != local_min[-1]:
                if p[k]<=p[i]-p[i]*cutoff and k > i: 
                    conditions[0]=True     
                else:
                    try:
                        if displacment >= iteration:
                            #shift all previuos points by one outside loop by seting each outer step to last inloop step
                            #shift displacement length to greatest indexed local extreme + 5
                            #reset all in loop steps because it will only increment to eqaul new displacement 
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]        
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            k = local_min[displacment]
                            continue
                    except IndexError:
                        break
                
                if p[m] >=p[k]-p[k]*0.1 and p[m] <= p[k]+p[k]*0.1 and p[m]<p[i] and m>k:
                    conditions[1] = True
                else:
                    try:
                        if displacment >= iteration:
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]         
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            m = local_min[0+displacment]
                            continue
                    except IndexError:
                        break
                 
                if p[l] >= p[i]-p[i]*0.5  and  p[i]+p[i]*0.5  and  p[l] > p[k] and i<k<l:
                        conditions[2] = True
                else:
                    try:
                        if displacment >= iteration:
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]         
                            iteration += 5          
                            continue
                        else: 
                            displacment+=1
                            l = local_max[displacment]
                            continue
                    except IndexError:
                        break
                
                # define distance between each peak assuming a second peak accures
                if p[n] >= p[i] and p[m] <= p[i]- p[i]*cutoff and n>m:
                    conditions[3]=True
                else:
                    try: 
                        if displacment >= iteration:
                          
                            i = local_max[displacment]
                            k = local_min[displacment]
                            l = local_max[displacment+1]      
                            m = local_min[displacment+1]   
                            n = local_max[displacment+2]          
                            iteration += 5          
                            continue
                        else:
                            displacment+=1
                            n=local_max[displacment]
                            continue

                    except IndexError:
                        break
                if all(conditions):
                    DoubleB[0]=True  
                    break                   
            else:
                break
        #print(f"DB:  {conditions}")
        location = [[],[]]
        if conditions[0]:
            location[0].append(i)
            location[0].append(k)
            location[1].append(p[i])
            location[1].append(p[k])
        if conditions[1]:   
            location[0].append(l)
            location[1].append(p[l])
        if conditions[2]:
            location[0].append(m)
            location[1].append(p[m])
        if conditions[3]:
            location[0].append(n)
            location[1].append(p[n])
        if show == True and all(conditions):
            if len(loc) > 5:
                #plt.scatter(loc,price_at_extremes,color="black",linewidths=0.2)
                #plt.plot(location[0],location[1],color="red")
                return loc, price_at_extremes, location[0],location[1]
            #plt.show()
        return False

class Indicators:
    """Formuals and Mesurments for estemating market momentum"""
    def __init__(self,close,start,end):
        self.start=start
        self.end = end
        self.close = close #In_Market().previous_close()
        self.volume = In_Market().volume()[self.start:self.end]
        self.RSI = []   #upload this to database
        pass
    def Unusual_Volume(self,sensivity=20,show=False):
        """see if each volume is more than a % of it previouse average"""
        volume = self.volume[self.start:self.end]
        x=[]
        for i in range(len(volume)):
            x.append(i)
        total_volume = sum(volume)
        proportion = []
        for i in volume:
            proportion.append(round(i/total_volume,7))
        
        pt_change = []
        unusual_volume =[]
        time_at_uv = []
        for i in range(len(proportion)-1):
            delta = proportion[i+1]-proportion[i]
            pt_change.append(round(delta,4))
        for i in range(len(pt_change)):
            if abs(pt_change[i]) > abs(sum(pt_change)/len(pt_change))*sensivity or abs(pt_change[i]) < abs(sum(pt_change)/len(pt_change))*sensivity < abs(sum(pt_change)/len(pt_change))*(1/sensivity):
                unusual_volume.append(volume[i+1])
                time_at_uv.append(x[i+1])
        if show == True:
            #ax.set_ylim(0,max(volume))
            plt.plot(x,volume)
            plt.scatter(time_at_uv,unusual_volume,color="purple")
            #plt.show()

        return unusual_volume[-1] #will return last point with unusaul volume to Navi


        

    def RSI_Index(self):
        """Return Relative Strength Index values within an interval
        of past price points"""
        if len(self.close) >= 15:
            prices = self.close[self.start:self.end]
            date = []
            for i in range(len(prices)):
                date.append(i)
            up_moves = []
            down_moves = []
            for i in range(1,len(prices)):
                if prices[i] - prices[i-1] > 0:
                    up_moves.append(prices[i])
                elif prices[i] - prices[i-1] <0:
                    down_moves.append(prices[i])
                else:
                    pass
            price_change_up =[]
            price_change_down = []
            for i in range(1,len(up_moves)):
                price_change_up.append(up_moves[i]-up_moves[i-1])
            for i in range(1,len(down_moves)):
                price_change_down.append(down_moves[i]-down_moves[i-1])
            
            if len(up_moves) != 0 and len(down_moves)!=0 and sum(price_change_down) != 0 and len(price_change_up) != 0:
                avgU = sum(price_change_up)/len(price_change_up)
                avgD = sum(price_change_down)/len(price_change_down)
                rs = abs(avgU/avgD)  #relative strength
                rsi = 100 - 100/(1+rs)
                return round(rsi,2)
            else:
                return 'NaN'
        else:
            return 'NaN'
        # write condtions of bullish/bearish market divergence

    def Exponetial_MAvg(self): #this smooths out the market into general trend and can help in the modifiyng of indicators 
        """Return exponetinal moving average in the data"""
        # start by computing the moving avg
        if self.end-self.start >= 15:
            prices = self.close
            #print(prices[0],previuos[-1])
            period =  self.end-self.start
            smoothing = 4.7 
            weight = smoothing/(period+1)
            EMA = [] 
            if len(prices) >0:
                EMA.append(sum(prices)/len(prices)) #initial  EMA 
                n = 1
                while prices[n-1] != prices[period-1]:
                    ema_n = prices[n]*(weight)+EMA[n-1]*(1-weight)
                    EMA.append(ema_n)
                    n+=1
                return EMA
            else:
                return 'NaN'
        else:
            return 'NaN'
        #========================UPGRADE to MACD===========================
        #MACD = []
        #n = 1
        #while EMA[n-1] != EMA[-1]:
        #    macd_n = (prices[n] - EMA[n])*weight+EMA[n-1]*(1-weight)
        #    MACD.append(macd_n)
        #    n+=1
        #==============================================
        
        

class Fundementals:
    """chose between P/E ratio, EPS ratio, and D/E ratio, as a moderation variable"""
    def PE_Ratio():
        pass
    def Earnings_per_shar():
        pass
    def DE_Ratio():
        pass   

