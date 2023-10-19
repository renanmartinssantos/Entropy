from PIL import Image
import requests
from io import BytesIO

#Binarização de Imagem
def BinaryColorConvert(image,threshold):
    #Setando Altura e Largura em uma variável
    width, height = image.size
    
    #Percorrendo toda a largura e altura
    for x in range(width):
        for y in range(height):
            #Pegando todos os pixels de cada ponto x,y
            R, G, B = image.getpixel((x,y))
            #Fazer a média do pixel e saber se ele é maior ou igual ao 
            #limiar(Onde será usado para saber onde colocar os RGBs de branco ou preto)
            if((R + G + B) / 3) <= threshold:
                image.putpixel((x,y), (0,0,0))
            else:
                image.putpixel((x,y), (255,255,255))
    #Retorna a imagem convertida por 0 ou 255.
    return image
 
def grayScaleImageConvert(image):
    #Setando Altura e Largura em uma variável
    width, height = image.size
    
    #Percorrendo toda a largura e altura
    for x in range(width):
        for y in range(height):
            #Pegando todos os pixels de cada ponto x,y
            R, G, B = image.getpixel((x,y))
            #obtendo a média do pixel por localização(x,y)
            median = int((R + G + B) / 3)
            #Substituindo os valores das cores RGB pela média dos Pixels
            image.putpixel((x,y), (median,median,median))
            
    return image
   
def startImageChange(image):
    #Escolhendo o tratamento da imagem entre Cinza ou Binario
    methodChoice = input("Escolha entre Cinza ou Binario: ")
    
    if(methodChoice == 'Binario'):
        #Retornando a imagem tratada da função
        imageConverted = BinaryColorConvert(image, 100)
        #Mostrando a imagem com tratamento
        imageConverted.show()
    else:
        #Retornando a imagem tratada da função
        imageConverted = grayScaleImageConvert(image)
        #Mostrando a imagem com tratamento
        imageConverted.show()
     
def init():
    #FUNÇÂO INICIAL
    #EXEMPLOS DE IMAGEM
    #https://images.pexels.com/photos/18157680/pexels-photo-18157680/free-photo-of-alpino-alpes-austria-lago.jpeg
    #https://images.pexels.com/photos/7683629/pexels-photo-7683629.jpeg
    #https://images.pexels.com/photos/1314186/pexels-photo-1314186.jpeg
    
    #Escolhendo entre Imagem Local ou URL de Imagem
    imgChoice = input("Digite LOCAL ou a url da imagem escolhida: ")
    #Caso escolha LOCAL, irá pegar a imagem da pasta do projeto.
    if imgChoice == "LOCAL":
        #Abrindo a imagem com o PIL
        newImage = Image.open('image.jpg')
        #Convertendo a Imagem caso ela não seja RGB para RGB
        image = newImage.convert('RGB')
        #Inciando a escolha e tratamento da imagem
        startImageChange(image)
        
    else:
        #Pegando a imagem pela URL.
        response = requests.get(imgChoice)
        #Transformando ela em Bytes para o PIL ler
        newImage = Image.open(BytesIO(response.content))
        #Forçando a imagem ser RGB
        image = newImage.convert('RGB')
        #Iniciando a escolha e tratamento da imagem
        startImageChange(image)
    
init()