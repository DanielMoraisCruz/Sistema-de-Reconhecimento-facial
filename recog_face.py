import base64

import cv2
import face_recognition as fr

from operacoes_db import get_user
from usuario.user import User


def encod_face(img=None):
    if img is None:
        raise "Image does not exists"
    # Carrega a imagem
    img = cv2.imread(img)

    # Converte a imagem para RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Encontra os encodings dos rostos
    faces_enc = fr.face_encodings(img_rgb)
    if faces_enc == []:
        raise "Face not found"
    return faces_enc


# Função que reconhece o rosto
def verifica_rosto(user: User):
    # Carrega a imagem

    faces_1 = encod_face(decoda_img(user.image))

    user_db = get_user(user)

    faces_2 = encod_face(decoda_img(user_db[0][3]))

    # Compara os dois rostos
    if faces_2 == [] or faces_1 == []:
        return False

    result = fr.compare_faces([faces_1], faces_2, tolerance=0.7)
    if result[0]:
        return True
    else:
        return False


def decoda_img(img):
    image = base64.b64decode(img)
    with open('imagem.jpg', 'wb') as f:
        f.write(image)
    return 'imagem.jpg'


if __name__ == '__main__':
    user = User()
    user.email = 'daniel.jack.dmc@gmail.com'

    user.image = 'daniel.jpg'

    print('foi') if verifica_rosto(user) else print('não foi')
