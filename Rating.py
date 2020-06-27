import pandas as pd 

def addRate(app_name, reviewss,size,install,type_app,price,rating,cat,content_r,genre):
# Creating the first Dataframe using dictionary 
    isThere = False

    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('C:/py/appdata1.csv')

    try:
        app_namee = app_name
        reviewsss = reviewss
        sizee = int(size)
        installl = int(install)
        type_appp = type_app
        pricee = int(price)
        catt = cat
        content_rr = content_r
        ratingInt = float(rating)
        genree = genre
        print(app_namee,catt,ratingInt,reviewsss,sizee,installl,type_appp,pricee,content_rr,genree)




        if(type_appp=='Free' and pricee>0):
            invalid = 'invalid'
            return invalid

        
        for index,row in df1.iterrows(): 
           
            if (row['App']== str(app_namee) and row['Category'] == str(catt)):
                row['Rating'] = rating
                row['Reviews'] = reviewss
                row['Size'] = size
                row['Installs'] = install
                row['Type'] = type_app
                row['Price'] = price
                row['Content_Rating'] = content_r
                row['Genres'] = genre
                k=['raj','s','hah']
                row['Android_Ver'] = k[0]
                row['Current _Ver'] = k[1]
                row['Last_Updated'] = k[2]
                isThere = True
        # Creating the Second Dataframe using dictionary 
        
        if isThere != True: 

            df2 = pd.DataFrame({'App':[app_namee],'Category':[catt],'Rating':[ratingInt],'Reviews':[reviewsss],'Size':[sizee],'Installs':[installl],
            'Type':[type_appp],'Price':[pricee],'Content_Rating':[content_rr],'Genres':[genree]}) 

            dff = df1.append(df2, ignore_index = True)
            dff.to_csv(r"C:/py/appdata1.csv", index = False)

            add = 'added'
            return add

        else:
            df1.to_csv(r'C:/py/appdata1.csv', index = False) 
            update = 'Already Exists!!'
            return update



    except ValueError:
        error = 'error'
        return error

    
