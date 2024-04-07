import numpy as np
import matplotlib.pyplot as plt
import cv2
import json
import os

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
        
        # plt.imshow(canvas28, cmap='gray')
        # plt.show()

        os.makedirs(f"images/{destiny_folder_name}", exist_ok=True)

        cv2.imwrite(f"images/{destiny_folder_name}/{str(i)}.jpg", canvas28)

def menu():
    print('1. Show with matplotlib')
    print('2. Get Images from JSON')
    print('0. Exit')

def main():
    op = ' ' 

    while op != '0':
        menu()
        op = input('Enter an option: ')
        
        if op == '1':
            file_name = input("Enter the name of the image: ")  
            
            image = cv2.imread(f"images/{file_name}", 0)
            
            plt.imshow(image, cmap='gray')
            plt.show()
        
        elif op == '2':
            with open('coches.json', 'r') as f:
                data = json.load(f)

            for register in data:
                get_images(register, register['name'])


if __name__ == '__main__':
    main()