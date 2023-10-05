import pandas as pd

# data = {
#     'email': ['juquinha123@gmail.com', ' denis.the.row@gmail.com'],
#     'cpf': ['123.456.789-00', '987.654.321-00'],
#     'password': ['123456', '654321'],
#     'img': ['juquinha.jpg', 'denis.jpg'],
#     'token': ['12345678900', '98765432100'],
#     'nivel_acesso': [3, 2]
# }

# df = pd.DataFrame(data)
# df.to_excel('output.xlsx', index=False)

db = pd.read_excel('output.xlsx')
