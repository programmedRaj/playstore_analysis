import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
def one():
    copy = data
    copy.drop(['App', 'Size', 'Reviews', 'Type', 'Price', 'Content_Rating', 'Genres', 'Last_Updated', 'Android_Ver'],axis=1,inplace=True)
    
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    category_list = list(copy['Category'].unique())
    
    category_install = []
    install_count = a = first = second = third = four = five = 0
    
    for i in category_list:
        x = copy[copy['Category'] == i]
        
        if(len(x) != 0):
            install = sum(x.Installs)/len(x)
            install_count = install_count + install
            category_install.append(install)
        else:
            install = sum(x.Installs) 
            install_count = install_count + install
            category_install.append(install)
            
    category_copy = category_install.copy()       
    
    for i in category_install:
        i = float((category_install[a]/install_count)*100)
        category_install[a] = i
        a = a + 1
        
#sorting
    data_category_install = pd.DataFrame({'category': category_list, 'install':category_install})
    #new_index = (data_category_install['install'].sort_values(ascending = False)).index.values
    #sorted_data = data_category_install.reindex(new_index)


    
#####TWO#####
    installs = list(copy['Installs'])
    
    for i in installs:
        
        if (i >= 10000) and (i <= 50000):
            first = first + 1
            
        if (i >= 50000) and (i <= 150000):
            second = second + 1        
        
        if (i >= 150000) and (i <= 500000):
            third = third + 1

        if (i >= 500000) and (i <= 5000000):
            four = four + 1
            
        if (i >= 5000000):
            five = five + 1
    
    #counted_data = [first, second, third, four, five]
    #range_data = ['Between 10,000 and 50,000', 'Between 50,000 and 150,000', 'Between 150,000 and 5,00,000', 'Between 5,00,000 and 50,00,000','More than 5000000']
    
   
#####TWO#####
#####THREE#####
    min = max = category_copy[0]
    avg = []
    
    for i in category_copy:
        if i < min:
            min = i
        if i > max:
            max = i
        if i >= 250000:
            avg.append(i)
            
    print("The apps which belongs to ", end = ' ')
    l=[]
    for i in avg:
        
        k=category_list[avg.index(i)]+','
        l.append(k)
  #AVG 250k+
    new=""
    for x in l: 
        new += x
    KK=new
    K=category_list[category_copy.index(min)] #LEAST
    J=category_list[category_copy.index(max)] #MOST
    return K,KK,J
global data
data = pd.read_csv("C:\\py\\appdata1.csv")

