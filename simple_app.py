import PySimpleGUI as psg


psg.set_options(font=("Arial Bold", 16))
layout = [
    [psg.Text('Enter a num: '), psg.Input(key='-FIRST-')],
    [psg.Text('Enter a num: '), psg.Input(key='-SECOND-')],
    [psg.Text('Result  :  '), psg.Text(key='-OUT-')],
    [psg.Button('Add'), psg.Button('Sub'), psg.Exit()]
]

window = psg.Window('Calculator', layout, size=(715, 180), disable_minimize=True, disable_close=True)

while True:
    event, values = window.read()
    result = ''
    print(event, values)
    if event == 'Add':
        result = int(values['-FIRST-']) + int(values['-SECOND-'])
    if event == 'Sub':
        result = int(values['-FIRST-']) - int(values['-SECOND-'])
    window['-OUT-'].update(result)
    if event == psg.WIN_CLOSED or event == 'Exit':
        break

window.close()