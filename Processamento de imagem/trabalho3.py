import cv2

def gaussiano(imagem, kernel_size=(11, 11), desvio_padrao=0):

    imagem_suavizada = cv2.GaussianBlur(imagem, kernel_size, desvio_padrao)
    return imagem_suavizada


imagem = cv2.imread("raioxequa")


imagem_suavizada = gaussiano(imagem)

cv2.imshow('Imagem Suavizada', imagem_suavizada)
cv2.waitKey(0)
