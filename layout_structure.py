import PySimpleGUI as psg

layout1 = [
    [psg.Text('Name'), psg.Input()],
    [psg.Text('Address'), psg.Input()],
    [psg.Text('Email ID'), psg.Input()],
    [psg.OK(), psg.Cancel()]
]

window1 = psg.Window('Form', layout1)
events, values = window1.read()
print(events, values)
window1.close()

psg.set_options(font=("Arial Bold", 16))
layout2 = [
    [psg.Text('Name', size=(15,1)), psg.Input(expand_x=True)],
    [psg.Text('Address', size=(15,1)), psg.Input(expand_x=True)],
    [psg.Text('Email ID', size=(15,1)), psg.Input(expand_x=True)],
    [psg.OK(), psg.Cancel()]
]

window2 = psg.Window('Form', layout2, size=(715,207))
events, values = window2.read()
print(events, values)
window2.close()