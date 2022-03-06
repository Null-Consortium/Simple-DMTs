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
    ['&Select', ['&Stocks ', ['&SHOW']],]
    ]
navi_layout = [
    [sg.Menu(menu_def,pad=(200, 1),text_color='black',background_color='white', tearoff=False,key='-MENUBAR-')],
    [sg.Text("",key='-STATUS-'),sg.Push(),sg.Text("",key='-COMP-'),sg.Push(),sg.Text(datetime.datetime.now().strftime('%Y-%m-%d'))],
    [sg.Graph((640, 480), (0, 0), (640, 480), key='-GRAPH-'),sg.Push(),],
    [sg.Text("Current Price:",size=(20,1),text_color='black',background_color='white',key='-PRICE-'),
    sg.Text("Date/Time:",size=(20,1),text_color='black',background_color='white',key= '-DATE-',),
    sg.Push(),sg.Checkbox("EMA",key='-EMA-',default=False)],
    [sg.Text("RSI: ",size=(20,1),text_color='black',background_color='white',key='-RSI-'),sg.Push(),sg.Button("View",button_color='skyblue',key="-VEIW-")],
]

window = sg.Window("NAVI",navi_layout,location=(0, 0),finalize=True,)
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
double_tops = []
double_bottoms = []
HS_belows = []
HS_aboves = []
ema_line = []
point=0
# global vars for shifting patterns
HSb_start = 0
HSa_start = 0
DT_start = 0
DB_start = 0
def plotting_price(ticker_symbol=None,run=False,display_expo=False):
    global point
    global HSb_start
    global HSa_start
    global DT_start
    global DB_start
    global double_tops
    global double_bottoms
    global HS_aboves
    global HS_belows
    figure_plots = []
    if run == True and ticker_symbol != None:
        SAMPLE_DATA = bull.In_Market().previous_close()[point]
        SAMPLE_DATES = bull.In_Market().date()[point]
        window['-PRICE-'].update(f"Current Price: {SAMPLE_DATA}") 
        window['-DATE-'].update(f"Date: {SAMPLE_DATES}")
        ax.set_ylabel("Price (USD)")
        ax.set_xlabel("Ticks")
        queue.append(SAMPLE_DATA) 
        if len(queue) <= 2:
            price.append(SAMPLE_DATA) 
            date.append(datetime.datetime.now().strftime("%I:%M:%S%p"))
            ticks = [i for i in range(len(price))] 
            point += 1
        elif queue[-1] == queue[-2]:  
            point += 1  
        else:
            # record the changes in stock price
            price.append(SAMPLE_DATA) 
            date.append(datetime.datetime.now().strftime("%I:%M:%S%p"))
            ticks = [ i for i in range(len(price))] #show acutal dates 
            plt.plot(ticks,price,color="blue")                  
            figure_plots.append((ticks,price,'blue'))
            if display_expo == True and bull.Indicators(price,0,len(ticks)).Exponetial_MAvg() != 'NaN':
                exp = bull.Indicators(price,0,len(ticks)).Exponetial_MAvg()
                plt.plot(ticks[:len(exp)],exp,color="orange")
                figure_plots.append((ticks[:len(exp)],exp,'orange'))          
            if bull.Patterns.HS_Above(price,HSa_start,len(ticks)) != False:
                ha0=bull.Patterns.HS_Above(price,HSa_start,len(ticks))[0]
                ha1=bull.Patterns.HS_Above(price,HSa_start,len(ticks))[1]
                figure_plots.append((ha0,ha1,'pink'))
                HSa_start = len(ticks)          
            if bull.Patterns.HS_Below(price,HSb_start,len(ticks)) != False:
                hb0=bull.Patterns.HS_Below(price,HSb_start,len(ticks))[0]
                hb1=bull.Patterns.HS_Below(price,HSb_start,len(ticks))[1]
                double_bottoms.append((hb0,hb1,'purple'))
                HSb_start = len(ticks)          
            if bull.Patterns.Double_T(price,DT_start,len(ticks)) != False:
                steps =bull.Patterns.Double_T(price,DT_start,len(ticks))[0]
                dT3=bull.Patterns.Double_T(price,DT_start,len(ticks))[1]
                double_tops.append((steps,dT3,'red'))
                DT_start = len(ticks)
            if bull.Patterns.Double_B(price,DB_start,len(ticks)) != False:
                steps=bull.Patterns.Double_B(price,DB_start,len(ticks))[0]
                db3=bull.Patterns.Double_B(price,DB_start,len(ticks))[1]
                double_bottoms.append((steps,db3,"green"))
                DB_start = len(ticks)          
        #ensure patterns stay shown 
        if len(double_bottoms) > 0:
            for i in double_bottoms:
                plt.plot(i[0],i[1],color=i[2])
        if len(double_tops) > 0:
            for i in double_tops:
                plt.plot(i[0],i[1],color=i[2])
        if len(HS_belows) > 0:
            for i in HS_belows:
                plt.plot(i[0],i[1],color=i[2])
        if len(HS_aboves) > 0:
            for i in HS_aboves:
                plt.plot(i[0],i[1],color=i[2])  
        ax.set_ylabel("Price (USD)")
        ax.set_xlabel("Ticks")
        y_upper = SAMPLE_DATA+100
        y_lower = SAMPLE_DATA-100
        plt.xlim(0,x_range)
        plt.ylim(y_lower,y_upper)
        window["-RSI-"].update(f"RSI: {bull.Indicators(bull.In_Market().previous_close(),0,len(ticks)).RSI_Index()}")
        fig.autofmt_xdate()
        fig.canvas.draw()
        ax.cla()
        ax.grid()
        point+=1
    return figure_plots
def Graph_events(event):
    tick = None
    show = False
    if event != '__TIMEOUT__' and event != None:
        options = ['SHOW']
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
def visualize(plots):
    """display plots in an interactive window"""
    global double_tops
    global double_bottoms
    embedeedmatplot_layout = [
    [sg.Push(),sg.T('KEY:  RED=Market_Pattern,   ORANGE=Exponential_Moving_Average,   BLUE=Stock_Price'),sg.Push()],
    [sg.Column(layout=[[sg.Canvas(key='fig_cv',size=(400 * 2, 400))]],background_color='#DAE0E6',pad=(0, 0))],
    [sg.B('Plot'), sg.B('Exit'),sg.Push(),sg.Canvas(key='controls_cv')]]
    embedeedmatplot_window = sg.Window('Viewing Data',embedeedmatplot_layout,modal=True)
    while True:
        fig2,ax2 = plt.subplots()
        event, values = embedeedmatplot_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'): 
            break
        else:
            DPI = fig2.get_dpi()
            fig2.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            ax2.cla()
            ax2.grid()
            for i in plots:
                if i != (None,None,None):
                    plt.plot(i[0],i[1],color =i[2])
            if len(double_bottoms) > 0:
                for i in double_bottoms:
                    plt.plot(i[0],i[1],color=i[2]) 
            if len(double_tops) > 0:
                for i in double_tops:
                    plt.plot(i[0],i[1],color=i[2]) 
            if len(HS_belows) > 0:
                for i in HS_belows:
                    plt.plot(i[0],i[1],color=i[2])
            if len(HS_aboves) > 0:
                for i in HS_aboves:
                    plt.plot(i[0],i[1],color=i[2]) 
            draw_figure_w_toolbar(embedeedmatplot_window['fig_cv'].TKCanvas, fig2, embedeedmatplot_window['controls_cv'].TKCanvas)
    embedeedmatplot_window.close()    

def main():
    global price
    global x_range
    global queue
    global n
    global index
    global point
    global start
    while session == True:            
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
        else:
            if Graph_events(event) != None:
                if Graph_events(event)[0] != start:
                    print(start,Graph_events(event)[0])
                    queue = []
                    price = []
                    start = Graph_events(event)
                    index += 1
                    if index == 4:
                        index=0
            if values["-EMA-"] == True:
                if event == "-VEIW-":
                    visualize(plotting_price(start[0],start[1],display_expo=True))
                else:
                    plotting_price(start[0],start[1],display_expo=True)
                    
            else:
            
                if event == "-VEIW-" :
                    visualize(plotting_price(start[0],start[1]))
                else:
                    plotting_price(start[0],start[1])        
    window.close()

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        pass
