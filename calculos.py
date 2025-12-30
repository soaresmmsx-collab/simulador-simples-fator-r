from tabelas_simples import TABELA_SIMPLES

ENCARGOS_CLT_PERCENTUAL = 0.70
VALE_REFEICAO = 600

def calcular_folha(cargos):
    total_salarios = sum(c["salario"] * c["quantidade"] for c in cargos)
    total_pessoas = sum(c["quantidade"] for c in cargos)

    encargos = total_salarios * ENCARGOS_CLT_PERCENTUAL
    beneficios = total_pessoas * VALE_REFEICAO

    folha_mensal = total_salarios + encargos + beneficios
    folha_anual = folha_mensal * 12

    return folha_mensal, folha_anual, total_pessoas

def calcular_fator_r(folha_anual, receita_mensal):
    receita_anual = receita_mensal * 12
    return folha_anual / receita_anual if receita_anual > 0 else 0

def definir_anexo(fator_r):
    return "III" if fator_r >= 0.28 else "V"

def calcular_aliquota_efetiva(rbt12, anexo):
    for faixa in TABELA_SIMPLES:
        if faixa["anexo"] == anexo and faixa["min"] <= rbt12 <= faixa["max"]:
            return (rbt12 * faixa["aliquota"] - faixa["deducao"]) / rbt12
    return 0

def calcular_das(receita_mensal, aliquota):
    return receita_mensal * aliquota
