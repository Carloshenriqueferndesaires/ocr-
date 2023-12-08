import cv2
import numpy as np

# Carregar a imagem com Canny aplicado e em tons de cinza
imagem_canny = cv2.imread('Cany_borda.png', cv2.IMREAD_GRAYSCALE)

# Encontrar contornos na imagem em tons de cinza
contornos, _ = cv2.findContours(imagem_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Criar uma cópia da imagem original
imagem_original = cv2.imread('Cany_borda.png')
imagem_com_caixas = imagem_original.copy()

# Iterar sobre os contornos encontrados
for contorno in contornos:
    # Encontrar a caixa delimitadora ao redor do contorno
    x, y, w, h = cv2.boundingRect(contorno)

    # Definir critérios para considerar apenas caixas delimitadoras de caracteres
    tamanho_minimo = 10  # Ajuste conforme necessário

    if w > tamanho_minimo and h > tamanho_minimo:
        # Desenhar a caixa delimitadora na imagem original
        cv2.rectangle(imagem_com_caixas, (x, y), (x + w, y + h), (255, 255, 255), 2)

# Mostrar a imagem com caixas delimitadoras
cv2.imshow('Imagem com Caixas Delimitadoras', imagem_com_caixas)
cv2.waitKey(0)
cv2.destroyAllWindows()
