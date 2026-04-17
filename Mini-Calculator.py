import tkinter as tk
root = tk.Tk()
root.title("Mini-Calculator.py")
display = tk.Label(root, text="", font=("Cascadia Code", 16, "bold"))
display.grid(row=0, column=0, columnspan=9)
text = ""
def calculator(com):
    global text
    if com == "=": text = str(eval(text))
    elif com == "C": text = ""
    elif com == "⌫": text = text[:-1]
    elif com == "±":
        if text[0] == "-": text = text[:0] + text[1:]
        else: text = "-"+"("+text+")"
    else: text = text+com
    display.config(text=text); text = text[:16] 
names = [("7",1,1), ("8",1,2), ("9",1,3), ("4",2,1), ("5",2,2), ("6",2,3), ("1",3,1), ("2",3,2), ("3",3,3), ("0",4,2), ("C",1,0,), ("=",4,1,), ("⌫",4,3), ("+",4,4), ("-",3,4), ("/",2,4), ("*",1,4), ("**",2,0), (".",4,0), ("±",3,0), ("(",5,1), (")",5,2)]
for (com,row,col) in names:
    btn = tk.Button(root, text=com, width=2, height=1, font=("Cascadia Code", 24, "bold"), command=lambda r=row, c=col, com=com: calculator(com))
    btn.grid(row=row, column=col)
root.bind('<Return>', lambda fff: calculator('=')); root.mainloop()