import os
import webbrowser
import pywhatkit as p
from datetime import datetime

def handling_browser(a):
    if "open" in a:
        b = a.split("open", 1)
        aman = b[1].strip()
        if "whatsapp" in a:
            webbrowser.open(f"https://web.{aman}.com/")
            print("Opening: whatsapp")
        elif "chrome" in a:
            os.startfile(f"C:/Program Files/Google/{aman}/Application/{aman}.exe")
            print(f"Opening: {aman}")
        elif aman:
            webbrowser.open(f"https://{aman}.com/")
            print(f"Opening: {aman}")

def multiply(a):
    
    for i in range(1,11):
            print(f"{a} * {i} = {a*i}") 
            save_to_history(f"{a} * {i} = {a*i}")

def play(a):
    if "play" in a:
        word = a.split("play",1)
        song = word[1].strip()
        if song:
            p.playonyt(song)
            print(f"Playing: {song}")

def search(a):
    if "search" in a:
        words = a.split("search",1)
        s = words[1].strip()
        if "song" in s:
            webbrowser.open(f"https://www.youtube.com/results?search_query= {s}")
            print(f"searching: {s}")
        elif s:
            webbrowser.open(f"https://www.google.com/search?q={s}")
            print(f"searching: {s}")

def save_to_history(a):
    with open("Memori.txt", "a") as f:   
        now = datetime.now()  
        timestamp = now.strftime("%d/%m/%Y %I:%M %p")
        f.write(f"{timestamp}: {a}\n")
    with open("Memori.txt", "r") as f:
        if "history" in a:
            hi = f.read()
            print(hi)
    if "clear history" in a:
        with open("Memori.txt", 'w') as f:
                f.write("")
                print("Your history clear..")

if __name__ == "__main__":
    while True:
        a = input("enter your input: ").lower()

        handling_browser(a)
        play(a)
        search(a)
        
        
        
