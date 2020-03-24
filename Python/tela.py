import PySimpleGUI as sg

layout = [
    [sg.Text('Filename')],
    [sg.Input('', key='filename'),sg.FileBrowse()],
    [sg.Button('Ok'), sg.Button('Cancel')],
]

window = sg.Window('Test', layout)

while True:
    event, values=window.read()
    if event in ('Exit', None): break

    print(event, values)

    if event == 'Ok':
        print(values['filename'])
        print('teste')

window.close()