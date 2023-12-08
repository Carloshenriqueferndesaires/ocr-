import cv2

def equalizacao(imggray):
    img1 = cv2.equalizeHist(imggray)
    return imggray, img1

def main():
    img = cv2.imread("raiox1.png")

    if img is None:
        print('Could not open or find the image.')
        return

    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Colorida", img)
    cv2.imshow("Tons de Cinza", imggray)
    cv2.waitKey(0)

    imggray, img1 = equalizacao(imggray)

    cv2.imshow('Equalized Image', img1)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
