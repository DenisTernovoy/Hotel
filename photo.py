import cv2


def main_photo():

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


if __name__ == '__main__':
    main_photo()