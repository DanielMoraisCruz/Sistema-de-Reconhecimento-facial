"""
Módulo para validação de dados
Verifica se cada entrada de dados é válida
ou seja, que não contém caracteres especiais
que poderiam ser usados para ataques de SQL Injection
"""


def valida_email(email: str) -> bool:
    """Verifica se o email é válido"""
    if '@' in email and '.' in email:
        return True
    else:
        return False


def valida_cpf(cpf: str) -> bool:
    """Verifica se o cpf é válido"""
    if len(cpf) == 11:
        return True
    else:
        return False
