import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
#from sklearn.model_selection import train_test_split
#from sklearn import metrics
#from sklearn import tree
import os
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from graph import build_graph
from sklearn.linear_model import LinearRegression
from Rating import addRate
from tree import addR
from GON import one
#from datetime import timedelta
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)
FLASK_DEBUG=1
@app.route('/')
def upload_file():
   #user_reviews = pd.read_csv("googleplaystore_user_reviews.csv")
   #playstore_data = pd.read_csv("googleplaystore.csv")
   
   #l=playstore_data.describe()
   return render_template('home.html')




@app.route('/rating')
def rating_file():
   PEOPLE_FOLDER = os.path.join('static', 'people_photo')
   app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'goforit.png')
   
   return render_template('rating.html',user_image=full_filename)



@app.route('/home')
def home_file():
 
  user_reviews = pd.read_csv("C:/py/user_reviews.csv")
  playstore_data = pd.read_csv("C:/py/appdata1.csv")
  playstore_data.drop_duplicates(inplace=True)
  playstore_data_full = playstore_data[playstore_data.Rating == 5]

  PEOPLE_FOLDER = os.path.join('static', 'people_photo')
  app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
  full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'newplot.png')
  a=playstore_data_full.head()  
  c=a.values.tolist()
  
  user_reviews.describe()
  return render_template('upload.html',hey=c,user_image=full_filename)




@app.route('/detail')
def detail_file():
    user_reviews = pd.read_csv("C:/py/user_reviews.csv")
    #f=user_reviews.columns
    f=user_reviews.describe()
    g=f.values.tolist()
    
    list=['count','mean','std','min','25%','50%','75%','max'] 
    PEOPLE_FOLDER = os.path.join('static', 'people_photo')
    app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'polarityhai.png')
   
    return render_template('detail.html',ur=g,l=list,user_image=full_filename)




@app.route('/answer')
def index():
	return render_template('answer.html')

@app.route('/process', methods=['POST'])
def process():
   data = pd.read_csv("C:\\py\\user_reviews.csv")
   data = data.dropna()
   X=data['Sentiment_Subjectivity'].values.reshape(-1,1)
   y=data['Sentiment_Polarity'].values.reshape(-1,1)
   reg=LinearRegression()
   reg.fit(X,y)
   
   #predictions=reg.predict(X)
   name = request.form['name']
   if (float(name) >=-1) and (float(name) <= 1):
      rate=float(name)*reg.coef_[0][0]+reg.intercept_[0]
      newName = rate
      return jsonify({'name' : newName})
   else:
      return jsonify({'error' : 'Invalid data!'})

# Dynamic Graph

@app.route('/graph')
def plot_png():
  playstore_data = pd.read_csv("googleplaystore.csv")
  list_1 = ['Category', 'Installs', 'Type',
        'Content Rating']
  #fig = create_figure()
  fig = plt.figure(figsize=(14,18))
  fig.subplots_adjust(hspace=0.4, wspace=0.4)
  i = 1
  for names in list_1:
    ax1 = fig.add_subplot(2, 2, i)
    df2 = playstore_data[names].value_counts()
    df2 = df2.reset_index()
    bar_plot(x = df2[names],y = df2['index'],y_label = 'Freq',title = 'Bar Chart On {}'.format(names),color='red',ax=ax1,x_label=names)
    i += 1
    output = io.BytesIO()


  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')

def bar_plot(x,y,y_label,x_label,title,color,ax):
    # plt.figure(figsize=(10,5))
    bar = sns.barplot(x = x,y=y,ax=ax,orient='h')
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    for i, v in enumerate(x.values):
        ax.text(v + 3, i + .25, str(v), color='black', fontweight='bold')
    return bar
    #fig = plt.figure(figsize=(14,18))



@app.route('/graph2')
def plot_pngg():
   PEOPLE_FOLDER = os.path.join('static', 'people_photo')
   app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'info.png')
   return render_template('graph1.html',user_image=full_filename)





@app.route('/graph3')
def file():
   PEOPLE_FOLDER = os.path.join('static', 'people_photo')
   app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'chart.png')
   return render_template('graph2.html',user_image=full_filename)
@app.route('/freeapps')
def fil():
   PEOPLE_FOLDER = os.path.join('static', 'people_photo')
   app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'd.png')
   return render_template('freeapps.html',user_image=full_filename)




@app.route('/go')  
def CRUD_page():
   return render_template('go.html')     


@app.route('/rating/add', methods=['POST'])
def addRating():
   app_name= request.form['app_name']
   reviewss = request.form['reviewss']
   size = request.form['size']
   install = request.form['install']
   type_app = request.form['type_app']
   price = request.form['price']
   rating = request.form['rating']
   cat = request.form['cat']
   content_r = request.form['content_r']
   genre = request.form['genre']
  
   print(app_name,' ',reviewss,' ',size,' ',install,' ',type_app,' ',price,' ',rating,' ',cat,' ',content_r,' ',genre)
   status = addRate(app_name, reviewss,size,install,type_app,price,rating,cat,content_r,genre)
   
   return status 


@app.route('/gameofnumbers')
def show():	
   status = one()
   PEOPLE_FOLDER = os.path.join('static', 'people_photo')
   app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'down.png')
   return render_template('dlist.html',u=status,user_image=full_filename)





@app.route('/sentiments')
def kk():
   data = pd.read_csv("C:\\py\\user_reviews.csv")
   copy = data
   copy.drop([ 'Sentiment_Subjectivity' , 'Sentiment_Polarity'],axis=1,inplace=True)

   #sns.heatmap(copy.isna())
   copy=copy.dropna()
   
   scores = copy.Sentiment.map({"Positive":1,"Negative":-1,"Neutral":0})
   copy.Sentiment = scores
   
   #print("THE TOP 5 APPS POSITIVE SENTIMENTS ARE ARE:\n")
   copy_pos = copy.groupby('App').sum().reset_index()
   l=copy_pos.sort_values(by='Sentiment',ascending=False)
   
   #print("THE TOP 5 APPS GENERATING NEGATIVE SENTIMENTS ARE:\n")
   k=copy_pos.sort_values(by='Sentiment',ascending=True)
   PEOPLE_FOLDER = os.path.join('static', 'people_photo')
   app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'sentsG.png')

   return render_template('sentiments.html',k1=l,k2=k,img=full_filename)

   

   #WORKING UPDATE.
@app.route('/go2')  
def CRUD_pagee():
   return render_template('goo.html')

@app.route('/rating/add2',methods=['POST'])
def addRet():
 eventId = request.form['eventId'] 
 userId = request.form['userId']
 rating = request.form['rating']
 print(userId,' ',eventId,' ',rating)
 statuss = addR(userId, eventId, rating)
 
 return statuss




