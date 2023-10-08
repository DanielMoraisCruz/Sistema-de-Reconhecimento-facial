import cv2
import face_recognition as fr

from operacoes_db import get_user
from usuario.user import User


def encod_face(img=None):
    if img is None:
        raise LookupError("Image does not exists")
    # Carrega a imagem
    img = cv2.imread(img)

    # Converte a imagem para RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Encontra os rostos na imagem
    faces_loc = fr.face_locations(img_rgb)[0]

    cv2.rectangle(img, (faces_loc[3], faces_loc[0]),
                  (faces_loc[1], faces_loc[2]), (0, 255, 0), 2)

    # Encontra os encodings dos rostos
    faces_enc = fr.face_encodings(img_rgb)[0]

    return faces_enc


# Função que reconhece o rosto
def verifica_rosto(user: User):
    # Carrega a imagem

    faces_1 = encod_face(user.image)

    user_db = get_user(user.email)
    faces_2 = user_db[0][3]  # carrega_encoda_rosto(user_db[0][3])

    # Compara os dois rostos
    result = fr.compare_faces([faces_1], faces_2, tolerance=0.5)

    if result[0]:
        return True
    else:
        return False


if __name__ == '__main__':
    user = User()
    user.email = 'daniel.jack.dmc@gmail.com'
    # tirar a foto usando opencv
    # video = cv2.VideoCapture(0)
    # _, frame = video.read()
    # cv2.imwrite('daniel.jpg', frame)
    # video.release()
    # cv2.destroyAllWindows()

    user.image = 'daniel.jpg'

    verifica_rosto(user)
