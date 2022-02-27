# Display graph based on data in excel sheet 
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import PySimpleGUI as sg
from matplotlib import use as use_agg
from tkinter import *
import BullsEye as bull
sg.theme('Black')
use_agg("TkAgg")
fig, ax = plt.subplots()
 
menu_def = [

    ['&File', ['&Open', '&Save', 'E&xit']],
    ['&Select', ['&Stocks ', ['&GOOG']],]
    ]
layout = [
    [sg.Menu(menu_def,pad=(200, 1),text_color='black',background_color='white', tearoff=False,key='-MENUBAR-')],
    [sg.Text("",key='-STATUS-'),sg.Push(),sg.Text("",key='-COMP-'),sg.Push(),sg.Text(datetime.datetime.now().strftime('%Y-%m-%d'))],
    [sg.Graph((640, 480), (0, 0), (640, 480), key='-GRAPH-'),sg.Push(),],
    [sg.Text("Current Price:",size=(20,1),text_color='black',background_color='white',key='-PRICE-'),
    sg.Text("Date/Time:",size=(20,1),text_color='black',background_color='white',key= '-DATE-',),
    sg.Push(),sg.Checkbox("EMA",key='-EMA-',default=False)],[sg.Push(),sg.Button("View",button_color='skyblue',key="-VEIW-")],

]

window = sg.Window("NAVI",layout,location=(0, 0),finalize=True,)
# Link matplotlib to PySimpleGUI Graph
canvas = FigureCanvasTkAgg(fig, window['-GRAPH-'].Widget)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(row=0, column=0)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)



session = True
index = 0
n=1
x_range = 10
start = (None,False) 
queue = []
price=[]
date = []
point=0
   
def visualize(plots):
    """display plots in an interactive window"""
    embedeedmatplot_layout = [
    [sg.Push(),sg.T('KEY:  RED=Market_Pattern,   ORANGE=Exponential_Moving_Average,   BLUE=Stock_Price'),sg.Push()],
    [sg.Column(layout=[[sg.Canvas(key='fig_cv',size=(400 * 2, 400))]],background_color='#DAE0E6',pad=(0, 0))],
    [sg.B('Plot'), sg.B('Exit'),sg.Push(),sg.Canvas(key='controls_cv')]]
    fig2,ax2 = plt.subplots()
    embedeedmatplot_window = sg.Window('Viewing Data',embedeedmatplot_layout)
    while True:
        event, values = embedeedmatplot_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'): 
             # always,  always give a way out!
            break
         # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
        DPI = fig2.get_dpi()
        # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
        fig2.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
        # -----------------------------
        ax2.cla()
        for i in plots:
            if i != (None,None,None):
                plt.plot(i[0],i[1],color =i[2])
        
        draw_figure_w_toolbar(embedeedmatplot_window['fig_cv'].TKCanvas, fig2, embedeedmatplot_window['controls_cv'].TKCanvas)
        

    
    plt.figure(2).clear()

def plotting_price(ticker_symbol=None,run=False,
display_expo=False,display=False):
    figure_plots = []
    if run == True and ticker_symbol != None:
        SAMPLE_DATA = bull.In_Market().previous_close()[point]
        SAMPLE_DATES = bull.In_Market().date()[point]
        window['-COMP-'].update(ticker_symbol)
        window['-PRICE-'].update(f"Current Price: {SAMPLE_DATA}") 
        window['-DATE-'].update(f"Date: {SAMPLE_DATES}")
        ax.set_ylabel("Price (USD)")
        ax.set_xlabel("Ticks")
        queue.append(SAMPLE_DATA) 
        if len(queue) <= 2:
            price.append(SAMPLE_DATA) 
            date.append(datetime.datetime.now().strftime("%I:%M:%S%p"))
            ticks = [i for i in range(len(price))] 
        elif queue[-1] == queue[-2]:  
            pass  
        else:
            # record the changes in stock price
            price.append(SAMPLE_DATA) 
            date.append(datetime.datetime.now().strftime("%I:%M:%S%p"))
            ticks = [ i for i in range(len(price))] #show acutal dates
            figure_plots.append((ticks,price,'blue'))
            if display_expo == True and bull.Indicators(price,0,len(ticks)).Exponetial_MAvg() != 'NaN':
                exp = bull.Indicators(price,0,len(ticks)).Exponetial_MAvg()
                plt.plot(ticks[:len(exp)],exp,color="orange")
                figure_plots.append((ticks[:len(exp)],exp,'orange'))
            else:
                figure_plots.append((None,None,None))
            
            if bull.Patterns.HS_Above(price,0,len(ticks)) != False:
                ha0=bull.Patterns.HS_Above(price,0,len(ticks),show=True)[0]
                ha1=bull.Patterns.HS_Above(price,0,len(ticks),show=True)[1]
                plt.plot(ha0,ha1,color="red")
                figure_plots.append((ha0,ha1,'red'))
            else:
                figure_plots.append((None,None,None)) 

            if bull.Patterns.HS_Below(price,0,len(ticks)) != False:
                hb0=bull.Patterns.HS_Below(price,0,len(ticks),show=True)[0]
                hb1=bull.Patterns.HS_Below(price,0,len(ticks),show=True)[1]
                plt.plot(hb0,hb1,color="red")
                figure_plots.append((hb0,hb1,'red'))
            else:
                figure_plots.append((None,None,None))
        
            if bull.Patterns.Double_T(price,0,len(ticks),show=True) != False:
                dT2=bull.Patterns.Double_T(price,0,len(ticks),show=True)[2]
                dT3=bull.Patterns.Double_T(price,0,len(ticks),show=True)[3]
                plt.plot(dT2,dT3,color="red")
                figure_plots.append((dT2,dT3,'red'))

            else:
                figure_plots.append((None,None,None))
                        

            if bull.Patterns.Double_B(price,0,len(ticks),show=True) != False:
                db2=bull.Patterns.Double_B(price,0,len(ticks),show=True)[2]
                db3=bull.Patterns.Double_B(price,0,len(ticks),show=True)[3]
                plt.plot(db2,db3,color="red")
                figure_plots.append((db2,db3,'red'))

            else:
                figure_plots.append((None,None,None))
            if display == True:
                visualize(figure_plots)
                # relain plot initial plot here  
                plt.figure(2).clear()
                main()
            ax.set_ylabel("Price (USD)")
            ax.set_xlabel("Ticks")
            y_upper = SAMPLE_DATA+30
            y_lower = SAMPLE_DATA-30
            plt.xlim(0,x_range)
            plt.ylim(y_lower,y_upper)
            fig.autofmt_xdate()
            plt.plot(ticks,price,color="blue")
            fig.canvas.draw()
            figure_plots = []
    
    



def Graph_events(event):
    tick = None
    show = False
    if event != '__TIMEOUT__' and event != None:
        options = ['GOOG','TSLA','ACAD']
        condtions = []
        for i in range(3):   # <--  configure for number of tickers in database
            condtions.append(False)
            if event == options[i]:
                condtions[i] = True
                show = condtions[i]
                tick = options[i]
                return tick,show
    else:
        return None
def main():
    global price
    global x_range
    global queue
    global n
    global index
    global point
    global start
    while session == True:
        ax.cla()
        if len(price) >= x_range:
            x_range += 10*n
            n+=1
        status ="Viewing Past Data"
        if status == "Market Closed":
            window["-STATUS-"].update(f"{status}",text_color='Red')
        elif status == "After Hours":
            window["-STATUS-"].update(f"{status}",text_color='Yellow')
        elif status == "Pre-Market":
            window["-STATUS-"].update(f"{status}",text_color='Yellow')
        else:
            window["-STATUS-"].update(f"{status}",text_color='Green')
        event, values = window.read(timeout=10)

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if Graph_events(event) != None:
            if Graph_events(event)[0] != start:
                queue = []
                price = []
                start = Graph_events(event)
                index += 1
                if index == 4:
                    index=0
        if values["-EMA-"] == True:
            if event == "-VEIW-":
                plotting_price(start[0],start[1],display_expo=True,display=True)
                
            else:
                plotting_price(start[0],start[1],display_expo=True)
        else:
            if event == "-VEIW-" :
                plotting_price(start[0],start[1],display=True)
            else:
                plotting_price(start[0],start[1])

            
        point += 1
    window.close()

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        pass
        