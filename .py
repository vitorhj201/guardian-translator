# ---------------------------------------------------------
# PROJETO: Guardian - Mapeamento de Dados e Conformidade
# ANALISTA: Vitor (ADS - UniCesumar)
# FUNÇÃO: Tradutor e Normalizador de Termos Técnicos
# ---------------------------------------------------------

# Base de conhecimento de risco e tradução
dicionario_analise = {
    "compliance": "conformidade jurídica e técnica",
    "risk_level": "nível de risco da operação",
    "data_privacy": "proteção e privacidade de dados"
}

def analisar_termo(termo):
    """
    Função de busca segura utilizando o método .get()
    Evita que o sistema falte ou dê erro (Programação Defensiva)
    """
    termo_limpo = termo.strip().lower()
    return dicionario_analise.get(termo_limpo, "Alerta: Termo não mapeado na base de dados.")

# Simulação de Auditoria
if __name__ == "__main__":
    termo_teste = "compliance"
    resultado = analisar_termo(termo_teste)
    print(f"Resultado da Análise: {resultado}")
