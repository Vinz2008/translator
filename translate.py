from googletrans import Translator
import PySimpleGUI as sg
translator = Translator()
sg.theme('SystemDefault') 
layout = [[sg.Text('Translator'), sg.Text(size=(15,1))],
	  [sg.Input(key='-INPUT-')],
	  [sg.Button("Translate")],
	  [sg.Text("", key = "-OUTPUT-")],
          [sg.Button("Exit")]],

window = sg.Window('Translator', layout)

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':
        	break
	elif event ==  "Translate":
		input = values["-INPUT-"]
		translation = translator.translate(input)
		window["-OUTPUT-"](translation)

window.close()
