from flask import Flask, render_template, redirect
from twitter import *
from tkinter import *
import mysql.connector as mariadb
app = Flask(__name__)

mariadb_connection = mariadb.connect(user='root', password='123456', database='tweets')
cursor = mariadb_connection.cursor()
def showTweets(x, num):
     # display a number of new tweets and usernames 
     for i in range(0, num):
          line1 = (x[i]['user']['screen_name']) 
          line2 = (x[i]['text'])
          cursor.execute("INSERT INTO tweet (user,text) VALUES (%s,%s)", (line1,line2))
          w = Label(master, text=line1 + "\n" + line2 + "\n\n") 
          w.pack()

def getTweets():
     x = t.statuses.home_timeline(screen_name="putscreennamehere") 
     return x

     def tweet(): 
         global entryWidget
        
         if entryWidget.get().strip() == "":
             print("Empty") 
         else:
             t.statuses.update(status=entryWidget.get().strip())
             entryWidget.delete(0,END)
             print("working")

t = Twitter( auth=OAuth('929748215058042883-eVIkYLyUIe6Uzm3gKiaXMTCSrQMUMNd', 'TaXvz7PhV9cOcrolPtcy4aBhXrpuXc0jjdG0Urouvz4Zo', 'aipWkJx95L2yxLw1Ud7tJggaY', '8e9LBVAuLDrULNanjxs5UQj4DMRnQyngd5ERxWIoALZlJos3vu'))
numberOfTweets =20

master = Tk()
showTweets(getTweets(), numberOfTweets)

master.title("Tkinter Entry Widget")
master["padx"] = 40
master["pady"] = 20
# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(master)
#Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Make a new Tweet:"
entryLabel.pack(side=LEFT)
# Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()




@app.route('/')
def index():
     return "hi"

@app.route('/home')
def home():
    tweets = cursor.execute("SELECT * FROM tweet")
        return render_template('home.html',tweets= tweets)

if __name__ == '__main__':
    master.mainloop()
    app.run(debug=True)
