import requests
import json

URL = 'https://www.receitaws.com.br/v1/cnpj/'


class CnpjPrompt:
    def __init__(self, cnpj):
        self.cnpj = ''.join([n for n in cnpj if n.isnumeric()])

    def consulta(self):
        req = requests.get(URL+self.cnpj)
        if req.status_code == 200:
            content = req.text
            result = json.loads(content)
            try:
                rotulos = ['Razão Social:', 'Nome Fantasia:', 'Telefone:', 'e-mail:', 'CEP:', 'Endereco:',
                           'Numero:', 'Complemento:', 'Bairro:', 'Municipip:', 'Estado:', 'Porte:', 'Abertura:',
                           'Atividade Principal:', 'Atividades Secundarias:', 'Quadro Social Administrativo']

                dados = [result['nome'], result['fantasia'], result['telefone'], result['email'],
                         result['cep'].replace('.', ''), result['logradouro'], result['numero'], result['complemento'],
                         result['bairro'], result['municipio'], result['uf'], result['porte'], result['abertura'],
                         result['atividade_principal'][0]['text'], result['atividades_secundarias'][0]['text'],
                         result['qsa']]

                def _retorno():
                    for key, value in zip(rotulos, dados):
                        if key != 'Quadro Social Administrativo':
                            print(key, value)
                            print('-' * 50)
                        else:
                            for chave, nome in enumerate(value):
                                print(key, nome['nome'])
                return _retorno()
            except KeyError:
                return 'ERRO: {}'.format(result['message'])


if __name__ == '__main__':
    numero = input('CNPJ: ')
    c = CnpjPrompt(numero)
    c.consulta()
