import cv2
import numpy as np

# Carregar a imagem de raio X (substitua 'raio_x.jpg' pelo caminho da sua imagem)
imagem_raio_x = cv2.imread('raiox.webp')

# Adicionar texto à imagem
texto_ufrrj = "UFRRJ"
texto_carlos_henrique = "Carlos Henrique"
texto_processamento = "Processamento de Imagem"

fonte = cv2.FONT_HERSHEY_SIMPLEX
escala_fonte = 1
cor_texto = (255, 255, 255)  # Branco
espessura_linha = 2

# Adicionar texto no canto esquerdo
posicao_ufrrj = (50, 50)
imagem_com_texto = imagem_raio_x.copy()
cv2.putText(imagem_com_texto, texto_ufrrj, posicao_ufrrj, fonte, escala_fonte, cor_texto, espessura_linha)

# Adicionar texto no canto direito
posicao_carlos_henrique = (imagem_raio_x.shape[1] - 300, 50)
cv2.putText(imagem_com_texto, texto_carlos_henrique, posicao_carlos_henrique, fonte, escala_fonte, cor_texto, espessura_linha)

# Adicionar texto abaixo
posicao_processamento = (50, imagem_raio_x.shape[0] - 50)
cv2.putText(imagem_com_texto, texto_processamento, posicao_processamento, fonte, escala_fonte, cor_texto, espessura_linha)

# Salvar a imagem com texto
cv2.imwrite('raio_x_com_texto.jpg', imagem_com_texto)

# Mostrar a imagem com texto
cv2.imshow('Imagem com Texto', imagem_com_texto)
cv2.waitKey(0)
cv2.destroyAllWindows()

