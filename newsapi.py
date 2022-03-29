import requests
import tkinter as tk

def getnews():
    api_key = "5462b85bcbab41d7920a3b971a59cbf1"
    url = "https://newsapi.org/v2/everything?"+api_key
    news = requests.get(url).json()

    articles = news['articles']

    my_articles = []
    my_news = ""

    for articles in articles:
        my_articles.append(articles["title"])

    for i in range(10):
        my_news = my_news + my_articles[i] + "\n"

print("my_news")          

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News API")

button = tk.Button(canvas, font=25, text= "Reload", command = "getnews")
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

getnews()

canvas.mainloop