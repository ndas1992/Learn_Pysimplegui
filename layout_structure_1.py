import PySimpleGUI as psg

psg.set_options(font=("Arial Bold", 16))
layout = [
    [psg.Text('Name', size=(15,1)), psg.Input(key = '-NM-',expand_x=True)],
    [psg.Text('Address', size=(15,1)), psg.Input(expand_x=True, key='-AD-')],
    [psg.Text('Email ID', size=(15,1)), psg.Input(expand_x=True, key='-EID-')],
    [psg.Text('You Entered '), psg.Text(key='-OUT-')],
    [psg.OK(), psg.Exit()]
]

window = psg.Window('Form', layout, size=(715,250))
while True:
    event, values = window.read()
    print(event, values)
    out = values['-NM-'] + ' ' + values['-AD-'] + ' ' + values['-EID-']
    window['-OUT-'].update(out)
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    
window.close()