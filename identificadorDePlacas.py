import numpy as np
# import matplotlib.pyplot as plt
import cv2
import json

def main():

    with open('coches.json', 'r') as f:
        data = json.load(f)

    image1 = cv2.imread(data[0]['path'], 0)
    image2 = cv2.imread(data[1]['path'], 0)
    image3 = cv2.imread(data[2]['path'], 0)

    # FRACCION DE IMAGENES COCHE 1--------------->
    listImage1 = []

    for i in data[0]['caracteres']:
        listImage1.append(image1[i['y'][0]:i['y'][1], i['x'][0]:i['x'][1]])
    
    for i in range(len(listImage1)):
        arr = np.array(listImage1[i].shape)
        
        numMax = np.argmax(arr)
        
        canvas = np.ones((arr[numMax], arr[numMax]), dtype=np.uint8) * 255

        start_x = (arr[numMax] - listImage1[i].shape[1]) // 2
        start_y = (arr[numMax] - listImage1[i].shape[0]) // 2
        end_x = start_x + listImage1[i].shape[1]
        end_y = start_y + listImage1[i].shape[0]
        canvas[start_y:end_y, start_x:end_x] = listImage1[i]
        
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

        cv2.imwrite('coche1_imagenes/'+str(i)+'.jpg', canvas28)

    # FRACCION DE IMAGENES COCHE 2--------------->
    listImage2 = []

    for i in data[1]['caracteres']:
        listImage2.append(image2[i['y'][0]:i['y'][1], i['x'][0]:i['x'][1]])
    
    for i in range(len(listImage2)):
        arr = np.array(listImage2[i].shape)
        
        numMax = np.argmax(arr)
        
        canvas = np.ones((arr[numMax], arr[numMax]), dtype=np.uint8) * 255

        start_x = (arr[numMax] - listImage2[i].shape[1]) // 2
        start_y = (arr[numMax] - listImage2[i].shape[0]) // 2
        end_x = start_x + listImage2[i].shape[1]
        end_y = start_y + listImage2[i].shape[0]
        canvas[start_y:end_y, start_x:end_x] = listImage2[i]
        
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

        cv2.imwrite('coche2_imagenes/'+str(i)+'.jpg', canvas28)

    # FRACCION DE IMAGENES COCHE 3--------------->
    listImage3 = []

    for i in data[2]['caracteres']:
        listImage3.append(image3[i['y'][0]:i['y'][1], i['x'][0]:i['x'][1]])

    for i in range(len(listImage3)):
        arr = np.array(listImage3[i].shape)
        
        numMax = np.argmax(arr)
        
        canvas = np.ones((arr[numMax], arr[numMax]), dtype=np.uint8) * 255

        start_x = (arr[numMax] - listImage3[i].shape[1]) // 2
        start_y = (arr[numMax] - listImage3[i].shape[0]) // 2
        end_x = start_x + listImage3[i].shape[1]
        end_y = start_y + listImage3[i].shape[0]
        canvas[start_y:end_y, start_x:end_x] = listImage3[i]
        
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

        cv2.imwrite('coche3_imagenes/'+str(i)+'.jpg', canvas28)


    # plt.imshow(image1, cmap='gray')
    # plt.show()

    # plt.imshow(image2, cmap='gray')
    # plt.show()

    # plt.imshow(image3, cmap='gray')
    # plt.show()


if __name__ == '__main__':
    main()