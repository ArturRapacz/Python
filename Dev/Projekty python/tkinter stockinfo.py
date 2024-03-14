import tkinter as tk
import yfinance as yf
win = tk.Tk()

win.title("Stock info")


topWidget = tk.Frame(win)
label = tk.Label(topWidget, text = "Write stock ticker:")
label.pack(side = tk.LEFT)
entry = tk.Entry(topWidget)
entry.pack(side = tk.RIGHT)
topWidget.pack(side = tk.TOP)

scrollbar = tk.Scrollbar(win)
textBox = tk.Text(win, height = 8, width = 70, padx = 5, pady = 5, font="Helvetica 12")

scrollbar.pack(side = tk.RIGHT, fill=tk.Y)
textBox.pack(expand = True, fill = tk.BOTH)
scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollbar.set)

def downloadData(e):
    textBox.delete(1.0, tk.END)
    stock = str(e.widget.get())
    stock = stock.upper().strip()
    print("Data downloaded:", stock)

    if not stock:
        print("No stock ticker")
        return
    
    stockData = yf.Ticker(stock)
    

    for key in stockData.info.keys():
        try:
            v = str(key).capitalize() + ": " + stockData.info[key] + "\n\n"
            textBox.insert(tk.END, v)
            
        except:
            pass


    history = stockData.history(period = "1mo", interval = "1d")
    textBox.insert(tk.END, history)

entry.bind("<Return>", downloadData)




win.mainloop()