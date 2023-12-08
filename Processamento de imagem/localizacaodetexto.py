import cv2

# Carregar a imagem pré-processada (substitua 'imagem_pre_processada.png' pelo nome da sua imagem)
imagemprocessada = cv2.imread("raioxsuvicao.png")

# Aplicar detecção de bordas usando o algoritmo Canny
bordas = cv2.Canny(imagemprocessada, 30,70)

# Redimensionar a imagem para exibir completamente na tela
altura, largura = bordas.shape[:2]
nova_largura = 800  # Escolha a largura desejada
nova_altura = int((nova_largura / largura) * altura)
bordas_redimensionadas = cv2.resize(bordas, (nova_largura, nova_altura))


# Mostrar a imagem com as bordas detectadas
cv2.imshow("bordas Canny",bordas_redimensionadas)
cv2.waitKey(0)
cv2.destroyAllWindows()
