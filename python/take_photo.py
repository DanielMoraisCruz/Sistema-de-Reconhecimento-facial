import cv2
import imutils


def take_photo():
    camera = cv2.VideoCapture(0)
    while True:
        (res, frame) = camera.read()
        if res:
            frame = imutils.resize(frame, width=600)
            # Mostra a foto (Tentar colocar um botão para tirar a foto)
            cv2.imshow("Foto", frame)

            key = cv2.waitKey(1) & 0xFF
            # Pressione 'k' para tirar a foto
            if key == ord("k"):
                image_file = "fotos/foto.png"
                cv2.imwrite(image_file, frame)
                break
            elif key == ord("q"):  # Pressione 'q' para sair
                break
    camera.release()
    cv2.destroyAllWindows()
    return image_file

