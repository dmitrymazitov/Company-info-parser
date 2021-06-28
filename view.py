import tkinter as tk
from tkinter import ttk

PAD = 300

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title('ПРОВЕРКА ЮРЛИЦ')
        
        self.controller = controller
        
        self.valueVar = tk.StringVar()

        self._makeFrameMain()
        self._makeFrameTop()
        self._makeCanvas()
        self._makeScrollBar()
        self._scrolledFrame()
        self._makeFrameDown()
        self._innerCanvasFrame()
        self._makeEntry()
        self._makeButton()        

    def main(self):
        self.geometry("600x650")
        self.mainloop()

    def _makeFrameMain(self):
        self.frameMain = ttk.Frame(self)
        self.frameMain.pack(fill=tk.BOTH, expand=1)
        self.frameMain.columnconfigure(0, weight=1)
        self.frameMain.rowconfigure(0, weight=1)
    
    def _makeFrameTop(self):
        self.frameTop = ttk.Frame(self.frameMain)
        self.frameTop.grid(row=0, column=0, sticky="news")
        self.frameTop.columnconfigure(0, weight=1)
        self.frameTop.rowconfigure(0, weight=1)
    
    def _makeCanvas(self):
        self.canvasTop = tk.Canvas(self.frameTop, background='grey', bd=0, highlightthickness='0')
        self.canvasTop.grid(row=0, column=0, sticky="news")
        self.canvasTop.bind("<Configure>", self.frameResize)
    
    def _makeScrollBar(self):
        self.scrollbar = ttk.Scrollbar(self.frameTop, orient='vertical', command=self.canvasTop.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        
    def _scrolledFrame(self):
        self.secondFrame = ttk.Frame(self.canvasTop)
        self.secondFrame.bind('<Configure>', lambda e: self.canvasTop.configure(scrollregion=self.canvasTop.bbox('all'))) 
        
        self.resize_scrollFrame = self.canvasTop.create_window((0,0), window=self.secondFrame, anchor="nw")
        self.canvasTop.configure(yscrollcommand=self.scrollbar.set)
    
    def _innerCanvasFrame(self):
        self.innerFrame = ttk.Frame(self.secondFrame)
        self.innerFrame.pack(side='top', fill='both', expand=1)
        self.innerFrame.columnconfigure(0, weight=1)
              
    def makeLabel(self, result):
        for number, s in enumerate(result):
            self.compFrame = tk.Frame(self.innerFrame, highlightbackground='grey', highlightthickness=1)
            self.compFrame.grid(row=number, column=0, sticky='nwes')
            self.compFrame.columnconfigure(0, weight=1)

            for num, xs in enumerate(s):
                self.ss = tk.Entry(self.compFrame, bd=0)
                self.ss.grid(row=num, column=0, sticky='nwes')
                self.ss.insert(0, xs)
                self.ss.config(state='readonly')

    def _makeFrameDown(self):
        self.frameDown = ttk.Frame(self.frameMain)
        self.frameDown.grid(row=1, column=0, sticky="news")

    def _makeEntry(self):
        self.entry = ttk.Entry(self.frameDown)
        self.entry.grid(row=0, columnspan=5, column=1, padx=20, sticky=tk.E)
    
    def _makeButton(self):
        self.btnSearch = ttk.Button(self.frameDown, text='Search', command=lambda button='Search': self.controller.onButtonClick(button))
        self.btnSearch.grid(row=0, column=6, sticky=tk.E)
        self.btnClean = ttk.Button(self.frameDown, text='Clean', command=lambda button='Clean': self.controller.onButtonClick(button))
        self.btnClean.grid(row=0, column=7, sticky=tk.E)

    def frameResize(self, event):
        self.canvasTop.itemconfigure(self.resize_scrollFrame, width = event.width)

    def getEntryValue(self):
        return self.entry.get()

    def cleanEntry(self):
        return self.entry.delete(0, last=tk.END)
        
    def cleanFrame(self):
        self.innerFrame.destroy()
        self.innerFrame = ttk.Frame(self.secondFrame)
        self.innerFrame.pack(side='top', fill='both', expand=1)
        self.innerFrame.columnconfigure(0, weight=1)

    
