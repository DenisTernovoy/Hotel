import cv2
from services import main_services, accept_services


def main_photo(num):
    global ID
    ID = num
    cap = cv2.VideoCapture(0)
    filename = 'person.jpg'

    while True:
        ret, img = cap.read()
        cv2.imshow("camera", img)
        if cv2.waitKey(10) == 27: # Клавиша Esc
            cv2.imwrite(filename, img)
            break

    cap.release()
    cv2.destroyAllWindows()
    main_services(ID)


if __name__ == '__main__':
    main_photo('2')