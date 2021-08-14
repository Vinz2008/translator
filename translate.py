from googletrans import Translator
import PySimpleGUI as sg
translator = Translator()
sg.theme('SystemDefault') 
layout = [[sg.Text('Translator'), sg.Text(size=(15,1))],
	  [sg.Input(key='-INPUT-')],
          [sg.Button("Exit")]],

window = sg.Window('Translator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
window.close()
