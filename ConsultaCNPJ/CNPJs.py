from tkinter import *
import requests
import json


class Cnpj:
    def __init__(self, master):
        janela = master
        janela.geometry('580x550+100+50')
        janela.title('CONSULTA CNPJ by Wagner Herculano')
        janela['bg'] = 'light gray'
        janela.resizable(width=False, height=False)

        self.lbNome = Label(janela, text='CNPJ', font='Arial 14 bold', bg='light gray')
        self.lbNome.place(x=8, y=20)
        self.eCNPJ = Entry(font='Arial 12')
        self.eCNPJ.place(x=65, y=23, width='190', height='23')
        self.eCNPJ.bind('<Key>', self.mascara_cnpj)
        self.eCNPJ.bind('<Return>', self.consulta)
        self.eCNPJ.bind('<Button-1>', self.limpar)

        self.btnOK = Button(janela, width=20, text='OK', font='Arial 12 bold')
        self.btnOK.place(x=270, y=23, width='50', height='24')
        self.btnOK.bind('<Button-1>', self.consulta)

        self.btnLimpar = Button(janela, width=90, text='LIMPAR', font='Arial 12 bold')
        self.btnLimpar.place(x=330, y=23, width='90', height='24')
        self.btnLimpar.bind('<Button-1>', self.limpar)

        self.txt = Text(janela, height=30, width=80, font='Arial 10')
        self.txt.place(x=8, y=50)
        self.txt.configure(state='disabled')  # Desabilita a edição de texto

    def mascara_cnpj(self, event):
        if len(self.eCNPJ.get()) == 2:
            self.eCNPJ.insert(END, '.')
        if len(self.eCNPJ.get()) == 6:
            self.eCNPJ.insert(END, '.')
        if len(self.eCNPJ.get()) == 10:
            self.eCNPJ.insert(END, '/')
        if len(self.eCNPJ.get()) == 15:
            self.eCNPJ.insert(END, '-')

    def limpar(self, event):
        self.eCNPJ.delete(0, END)
        self.txt.configure(state='normal')
        self.txt.delete(1.0, END)
        self.txt.configure(state='disabled')

    def consulta(self, event):
        cnpj = self.eCNPJ.get().replace('.', '').replace('/', '').replace('-', '').strip()
        url = 'https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj)
        req = requests.get(url)
        code = req.status_code
        if code == 200:
            html = req.text
            receita = json.loads(html)
            try:
                self.txt.configure(state='normal')  # Habilita e edição de texto
                self.txt.delete(1.0, END)
                self.txt.insert(INSERT, 'NOME: {}\n'.format(receita['nome']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nTELEFONE: {}\n'.format(receita['telefone']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nE-MAIL: {}\n'.format(receita['email']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nCEP: {}\n'.format(receita['cep'].replace('.', '')))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nENDEREÇO: {}\n'.format(receita['logradouro']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nNÚMERO: {}\n'.format(receita['numero']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nCOMPLEMENTO: {}\n'.format(receita['complemento']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nBAIRRO: {}\n'.format(receita['bairro']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nCIDADE: {}\n'.format(receita['municipio']))
                self.txt.insert(INSERT, '-'*138)
                self.txt.insert(INSERT, '\nESTADO: {}\n'.format(receita['uf']))
                self.txt.insert(INSERT, '-'*138)
                try:
                    self.txt.insert(INSERT, '\nATIVIDADE PRINCIPAL: {}\n'.format(receita['atividade_principal'][0]['text']))
                    self.txt.insert(INSERT, '-'*138)
                except IndexError:
                    pass
                try:
                    self.txt.insert(INSERT, '\nATIVEIDE SECUNDÁRIA: {}\n'.format(receita['atividades_secundarias'][0]['text']))
                    self.txt.insert(INSERT, '-'*138)
                except IndexError:
                    pass
                try:
                    self.txt.insert(INSERT, '\nQuadro dos Sócios e Administradores (QSA)\n')
                    self.txt.insert(INSERT, '    NOME: {}\n'.format(receita['qsa'][0]['nome']))
                    self.txt.insert(INSERT, '    NOME: {}\n'.format(receita['qsa'][1]['nome']))
                    self.txt.insert(INSERT, '-'*138)
                except IndexError:
                    pass
                self.txt.configure(state='disabled')
            except KeyError:
                self.txt.insert(INSERT, 'ERRO: {}'.format(receita['message']))
                                       

if __name__ == '__main__':
    root = Tk()
    Cnpj(root)
    root.mainloop()
