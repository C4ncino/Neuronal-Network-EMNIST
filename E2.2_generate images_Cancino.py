import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
import json
import os

def listar_elementos(directorio):
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return
        
    elementos = [nombre for nombre in os.listdir(directorio) if not os.path.isdir(os.path.join(directorio, nombre))]

    print("\nElementos en el directorio:")
    for i in range(len(elementos)): 
        print(f"{i}: {elementos[i]}")

    return elementos

def get_images(data, destiny_folder_name):
    
    image = cv2.imread(data['path'], 0)

    images_letters = []

    for item in data['caracteres']:
        images_letters.append(image[item['y'][0]:item['y'][1], item['x'][0]:item['x'][1]])
    
    for i in range(len(images_letters)):
        arr = np.array(images_letters[i].shape)
        
        numMax = np.argmax(arr)
        
        canvas = np.ones((arr[numMax], arr[numMax]), dtype=np.uint8) * 255

        start_x = (arr[numMax] - images_letters[i].shape[1]) // 2
        start_y = (arr[numMax] - images_letters[i].shape[0]) // 2
        end_x = start_x + images_letters[i].shape[1]
        end_y = start_y + images_letters[i].shape[0]
        canvas[start_y:end_y, start_x:end_x] = images_letters[i]
        
        # ----------------------------------------------------------------------
        # Recorrer la imagen y todo aquel pixel que supere el valor 100, 
        # se pasara a blanco para poder invertir los colores y mandarlo al modelo
        for j in range(len(canvas)):
            for k in range(len(canvas[i])):
                if canvas[j][k] > 70:
                    canvas[j][k] = 0
                else:
                    canvas[j][k] = 255


        canvasResized = cv2.resize(canvas, (28, 28))

        canvas28 = canvasResized.reshape(-1, 28)

        # Prueba rotando la imagen -------------------------------------------------
        altura, anchura = canvas28.shape[:2]
        
        angulo_rotacion = random.randint(25, 271)

        centro = (anchura // 2, altura // 2)

        matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo_rotacion, 1.0)

        imagen_rotada = cv2.warpAffine(canvas28, matriz_rotacion, (anchura, altura))
        # --------------------------------------------------------------------------

        # plt.imshow(canvas28, cmap='gray')
        # plt.show()

        os.makedirs(f"images/{destiny_folder_name}", exist_ok=True)
        
        cv2.imwrite(f"images/{destiny_folder_name}/{str(i)}.jpg", imagen_rotada)

def check_color(pixel):

    if pixel <71:
        return 'n'
    elif pixel < 101:
        return 'g'
    else:
        return 'b'

def menu():
    print('\n1. Show with matplotlib')
    print('2. Get Images from JSON')
    print('0. Exit')

def main():
    op = ' ' 

    while op != '0':
        menu()
        op = input('Enter an option: ')
        
        if op == '1':
            elements = listar_elementos('images')

            f_i = input("Select an image: ")  
            
            image = cv2.imread(f"images/{elements[int(f_i)]}", 0)
            
            plt.imshow(image, cmap='gray')
            plt.show()
        
        elif op == '2':
            with open('coches.json', 'r') as f:
                data = json.load(f)

            for register in data:
                get_images(register, register['name'])


if __name__ == '__main__':
    main()