import cv2

from take_photo import take_photo


def menu_inicial():
    print("Bem-vindo ao sistema gererico")
    print("================================")
    print("1 - Entrar")
    print("2 - Criar conta")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


x = menu_inicial()
match x:
    case 1:
        print("Entrar")
    case 2:
        image_file = take_photo()
        imagem = cv2.imread(image_file)
    case _:
        pass

# Mostrar foto
# cv2.imshow("Foto", imagem)
# cv2.waitKey(0)
