from PySimpleGUI import PySimpleGUI as sg

#LAYOUT

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario:'),sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha:  '),sg.Input(key='senha', size=(20, 1), password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')],
]
#JANELA
janela = sg.Window ('Login', layout)

# ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuario'] == 'kaue' and valores ['senha'] == '12345678':
            print('Seja bem vindo!')