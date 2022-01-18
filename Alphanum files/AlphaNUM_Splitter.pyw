from os import execl
import PySimpleGUI as sg
import sys
from tkinter import *

from Extra_Sheet_Tools import AlphaNum

#fomart of window specs sg.Window(title="Hello World", layout=[[]], margins = (150,50)).read()

sg.theme('black')

#windows contents
layout = [[sg.Text('Select a text file with alpha-numeric')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open(), sg.Cancel("Quit")],
                    [sg.Text('',size=(1,2))],
                    [sg.Push(),sg.Text("GIVEN DATA"),sg.Push()],
                    [sg.Multiline(size=(65,5), key = '-Contents-',enable_events=True)],
                    [sg.Text("Results")],
                    [sg.Multiline(size=(25,12), key ='-NUMS-', enable_events = True),
                    sg.Push(),sg.Multiline(size=(25,12), key ='-ALPHAS-', enable_events = True)],
                    [sg.Text('',size=(1,2))],
                    [sg.Push(),sg.In(), sg.FileBrowse("Upload to Excel Sheet")],
                    [sg.Push(),sg.RButton('Submit')]
]

#create window 
window = sg.Window('AlphaNum',layout,icon=r"C:\Users\AAske\Downloads\scissors.ico")


#event loop to get data displayed
run = True
while run:
    event, values = window.read()
    fname = values[0]
    excel = layout[9][1]
    get_text = True
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    else:
        pass
    while get_text:
        if not fname:
            sg.popup('Text File Not Detected')
            #raise SystemExit("Cancelling: no filename supplied")
            break
        else:
            Test = AlphaNum(fname)
            with open(fname, 'r') as file:
                L = []
                items = file.readlines()
                for line in items:
                    L.append(line[:-1])
            window['-Contents-'].update(L)
            # display nums, alphas, and other symbols into the three respective blocks
            window['-NUMS-'].update(Test.Get_NUMS()) #numbers always go before letters
            window['-ALPHAS-'].update(Test.Get_ALPHA())
            break
    if not excel:
        upload = False
    else:
        upload = True
    while upload:
        if event == 'Submit':
            try:
                Test = AlphaNum(fname)
                Test.Get_NUMS()
                Test.Get_ALPHA()
                Test.upload(execl)
                sg.popup('File Uploaded')
                break
            except FileNotFoundError:
                break
        else:
            break

window.close()


    
    





# ---- Initial METHOD ----
#if len(sys.argv) == 1:
#    event, values = sg.Window('Alpha Numeric Parser',
#                    [[sg.Text('Select a text file with alpha-numeric')],
#                    [sg.In(), sg.FileBrowse()],
#                    [sg.Open(), sg.Cancel()],
#                    [sg.Text('',size=(1,10))]],
                    
#                    ).read(close=True)
                    
#    fname = values[0]
#else:
#    fname = sys.argv[1]

#while True:
#    if not fname:
#        sg.popup("Cancel", "No filename supplied")
#        raise SystemExit("Cancelling: no filename supplied")
#    else:
#        Test = AlphaNum(fname)
       ## window['-OUTPUT-'].update(values['-IN-'])
#        break