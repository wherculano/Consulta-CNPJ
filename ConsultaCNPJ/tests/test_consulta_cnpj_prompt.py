from ConsultaCNPJ.consulta_cnpj_prompt import CnpjPrompt


def test_cnpj():
    numero = '00 000.000-0000/00'
    cnpj = CnpjPrompt(numero)
    assert cnpj is not None


def test_consulta():
    numero = '00 000.000-0000/00'
    cnpj = CnpjPrompt(numero)
    result = cnpj.consulta()
    assert result is None
