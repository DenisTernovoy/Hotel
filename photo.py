import cv2
from services import main_services, accept_services


def main_photo(num):
    global ID

    face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    ID = num
    cap = cv2.VideoCapture(0)
    filename = f'{num}.png'

    while True:
        ret, image = cap.read()

        faces = face_cascade_db.detectMultiScale(image, 1.1, 19)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("camera", image)

        ret, image = cap.read()
        if cv2.waitKey(10) == 27:  # Клавиша Esc
            cv2.imwrite(filename, image)
            break

    img = cv2.imread(f'{num}.png')
    crop_img = img.copy()
    crop_img = crop_img[10:400, 180:500]
    cv2.imwrite(filename, crop_img)

    cap.release()
    cv2.destroyAllWindows()
    main_services(ID)


if __name__ == '__main__':
    main_photo('2')
