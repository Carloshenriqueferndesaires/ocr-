import cv2
import numpy as np

# Carregar a imagem em tons de cinza
imagem_tons_de_cinza = cv2.imread('dilatacao.png', cv2.IMREAD_GRAYSCALE)

# Definir um kernel para a operação de erosão
kernel_erosao = np.ones((3, 3), np.uint8)

# Aplicar erosão
imagem_erodida = cv2.erode(imagem_tons_de_cinza, kernel_erosao, iterations=1)

# Mostrar as imagens
cv2.imshow('Imagem Original', imagem_tons_de_cinza)
cv2.imshow('Imagem Erodida', imagem_erodida)

cv2.waitKey(0)
cv2.destroyAllWindows()
