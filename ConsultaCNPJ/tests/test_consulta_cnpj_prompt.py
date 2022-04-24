from ConsultaCNPJ.consulta_cnpj_prompt import ConsultaCNPJ


def test_cnpj():
    numero = '00360305000104'
    cnpj = ConsultaCNPJ(numero)
    result = cnpj.consulta()
    assert type(result) == dict


def test_consulta():
    numero = '00360305000109'  # '00360305000104'
    cnpj = ConsultaCNPJ(numero)
    result = cnpj.consulta()
    print(result)
    assert "ERRO:" in result

# ToDo: Criar testes que não sejam de integração (não dependam da internet)
