import random
import PySimpleGUI as sg


class PassGen:
    def __init__(self):
        # Definicao do Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Nome do Site ou Aplicativo:', size=(20, 1)), sg.Input(key='site', size=(30, 1))],
            [sg.Text('E-mail ou Usuario:', size=(20, 1)), sg.Input(key='login', size=(30, 1))],
            [sg.Text('Quantidade de Caracteres:'), sg.Combo(values=list(range(8, 31)), key='qtd_caracteres', default_value=8, size=(3, 1))],
            [sg.Text('Console do gerador:', size=(20, 1))],
            [sg.Output(size=(60, 6))],
            [sg.Button('Gerrar Senha')]
        ]

        # Definicao da Janela do gerador
        self.janela = sg.Window('Gerador de Senhas do Guto', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerrar Senha':
                nova_senha = self.Gerar_senha(valores)
                self.Salvar_Senha(nova_senha, valores)

    def Gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-=+,.<>/|?]}[{;:'
        chars = random.choices(char_list, k=int(valores['qtd_caracteres']))
        new_pass = ''.join(chars)
        return new_pass

    def Salvar_Senha(self, nova_senha, valores):
        if valores['site'] == '' or valores['login'] == '':
            print("Preencha todos os campos para gerar sua nova senha!")
        else:
            with open('Senhas.txt', 'a', newline='') as arquivo:
                arquivo.write(
                    f"\nSenha Salva para o Site: {valores['site']}, com o usuario: {valores['login']}, com a senha: {nova_senha}")
            print(nova_senha)
            print("Arquivo salvo com Sucesso em Senhas.txt")


gen = PassGen()
gen.Iniciar()
