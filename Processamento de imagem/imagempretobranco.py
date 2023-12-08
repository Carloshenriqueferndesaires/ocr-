from PIL import Image

if __name__ == "__main__":
    imagem =Image.open("nova-york.jpg")
    print(imagem.getpixel((100,100)))
    print(imagem.getpixel((500,300)))
    print(imagem.getpixel((300,180)))