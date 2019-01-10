from tkinter import *
import requests
import json

def mascaraCNPJ(event):
    if len(eCNPJ.get()) == 2:
        eCNPJ.insert(END,'.')
    if len(eCNPJ.get()) == 6:
        eCNPJ.insert(END,'.')
    if len(eCNPJ.get()) == 10:
        eCNPJ.insert(END,'/')
    if len(eCNPJ.get()) == 15:
        eCNPJ.insert(END,'-')
        
def limpar(event):
    eCNPJ.delete(0,END)
    txt.configure(state='normal')
    txt.delete(1.0,END)
    txt.configure(state='disabled')

     
def consulta (event):
    cnpj = eCNPJ.get().replace('.','').replace('/','').replace('-','').strip()
    url = 'https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj)
    req = requests.get(url)
    code = req.status_code
    if code == 200:
        try:
            html = req.text
            receita = json.loads(html)
            txt.configure(state='normal')#Habilita e edição de texto
            txt.delete(1.0,END)
            txt.insert(INSERT,'NOME: {}\n'.format(receita['nome']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nTELEFONE: {}\n'.format(receita['telefone']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nE-MAIL: {}\n'.format(receita['email']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nCEP: {}\n'.format(receita['cep'].replace('.','')))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nENDEREÇO: {}\n'.format(receita['logradouro']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nNÚMERO: {}\n'.format(receita['numero']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nCOMPLEMENTO: {}\n'.format(receita['complemento']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nBAIRRO: {}\n'.format(receita['bairro']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nCIDADE: {}\n'.format(receita['municipio']))
            txt.insert(INSERT,'-'*138)
            txt.insert(INSERT,'\nESTADO: {}\n'.format(receita['uf']))
            txt.insert(INSERT,'-'*138)
            try:
                txt.insert(INSERT,'\nATIVIDADE PRINCIPAL: {}\n'.format(receita['atividade_principal'][0]['text']))
                txt.insert(INSERT,'-'*138)
            except IndexError:
                pass
            try:                
                txt.insert(INSERT,'\nATIVEIDE SECUNDÁRIA: {}\n'.format(receita['atividades_secundarias'][0]['text']))
                txt.insert(INSERT,'-'*138)
            except IndexError:
                pass
            try:
                txt.insert(INSERT,'\nQuadro dos Sócios e Administradores (QSA)\n')
                txt.insert(INSERT,'    NOME: {}\n'.format(receita['qsa'][0]['nome']))
                txt.insert(INSERT,'    NOME: {}\n'.format(receita['qsa'][1]['nome']))
                txt.insert(INSERT,'-'*138)
            except IndexError:
                pass
            txt.configure(state='disabled')
        except KeyError:
            txt.insert(INSERT,'ERRO: {}'.format(receita['message']))
                                       


janela = Tk()
janela.geometry('580x550+100+50')
janela.title('CONSULTA CNPJ by Wagner Herculano')
janela['bg'] = 'light gray'
janela.resizable(width=False, height=False)

lbNome = Label(janela, text='CNPJ', font = 'Arial 14 bold',bg='light gray')
lbNome.place(x=8, y=20)
eCNPJ = Entry(font='Arial 12')
eCNPJ.place(x=65,y=23, width='190', height='23')
eCNPJ.bind('<Key>', mascaraCNPJ)
eCNPJ.bind('<Return>',consulta)
eCNPJ.bind('<Button-1>',limpar)

btnOK = Button(janela, width=20, text='OK', font='Arial 12 bold')
btnOK.place(x=270, y=23, width='50', height='24')
btnOK.bind('<Button-1>', consulta)

btnLimpar = Button(janela, width=90, text='LIMPAR', font='Arial 12 bold')
btnLimpar.place(x=330, y=23, width='90', height='24')
btnLimpar.bind('<Button-1>', limpar)

txt = Text(janela, height=30, width=80, font='Arial 10')
txt.place(x = 8, y = 50)
txt.configure(state='disabled')#Desabilita a edição de texto




