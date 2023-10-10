import base64

import cv2
import face_recognition as fr
import numpy as np

from operacoes_db import get_user
from usuario.user import User


def encod_face(img=None):
    if img is None:
        raise "Image does not exists"
    # Carrega a imagem
    image = base64.b64decode(img)
    image = np.frombuffer(image, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Converte a imagem para RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Encontra os encodings dos rostos
    faces_enc = fr.face_encodings(img_rgb)
    if faces_enc == []:
        raise "Face not found"
    return faces_enc


# Função que reconhece o rosto
def verifica_rosto(user: User):
    # Carrega a imagem

    try:
        faces_1 = encod_face(user.image)

        user_db = get_user(user)

        faces_2 = encod_face(user_db[0][3])
    except Exception as e:
        if str(e) == "Face not found":
            return False
        else:
            raise e

    # Compara os dois rostos
    if faces_2 == [] or faces_1 == []:
        return False

    faces_1 = np.array(faces_1)
    faces_2 = np.array(faces_2)

    result = fr.compare_faces(faces_1, faces_2, tolerance=0.3)
    if result[0]:
        return True
    else:
        return False


if __name__ == '__main__':
    # Test
    pass
