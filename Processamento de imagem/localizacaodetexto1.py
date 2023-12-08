import cv2
import numpy as np

# Carregar a imagem em tons de cinza
imagem_tons_de_cinza = cv2.imread('caixa_delimitada.png', cv2.IMREAD_GRAYSCALE)

# Definir um kernel para a operação de dilatação
kernel = np.ones((3, 3), np.uint8)

# Aplicar dilatação
imagem_dilatada = cv2.dilate(imagem_tons_de_cinza, kernel, iterations=1)

# Mostrar as imagens
cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)  # Definir a janela como redimensionável
cv2.imshow('Imagem Original', imagem_tons_de_cinza)
cv2.namedWindow('Imagem Dilatada', cv2.WINDOW_NORMAL)  # Definir a janela como redimensionável
cv2.imshow('Imagem Dilatada', imagem_dilatada)

cv2.waitKey(0)
cv2.destroyAllWindows()
