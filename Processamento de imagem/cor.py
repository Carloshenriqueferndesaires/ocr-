from PIL import Image

#image = Image.new("RGB",(500,500),(22,22,231))#string,(altura,largura),cor()
 

def criandoimagem(size):
    WRITE=(255,255,255)
    BLACK=(0,0,0)
    image=Image.new("RGB",(size,size),WRITE)
    
    for x in range((size)):
      for y in range((size)):
        if x < y:
            image.putpixel((x,y),BLACK)
      return image
    
if __name__ == "__main__":
    imagem = criandoimagem(700)
    imagem.show()