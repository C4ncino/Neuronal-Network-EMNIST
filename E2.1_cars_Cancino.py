import os
import cv2
import tensorflow as tf
from matplotlib import pyplot as plt 
import numpy as np
from class_mapping import classes

def listar_carpetas(directorio):
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return
    
    carpetas = [nombre for nombre in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, nombre))]
    
    print("\nCarpetas en el directorio:")
    for i in range(len(carpetas)): 
        print(f"{i}: {carpetas[i]}")
    
    return carpetas

def listar_elementos(directorio):
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return
    
    elementos = os.listdir(directorio)

    print("\nElementos en el directorio:")
    for i in range(len(elementos)): 
        print(f"{i}: {elementos[i]}")

    return elementos

def menu():
    print("\n1. JP's models")
    print("2. Cancino's models")
    print('0. Exit')


def main():

    op = ' ' 
    while op != '0':
        menu()
        op = input('Select the player: ')
        
        player = ""

        if op == '0':
            break

        elif op == '1':
            player = 'juanpablo'

        elif op == '2':
            player = 'cancino'
        
        
        models = listar_elementos(f"models/{player}")

        model_selection = input("Select a model: ")

        print()

        folders = listar_carpetas("images")
        
        test_example = input("Seleccione un folder: ")

        tf_model = tf.keras.models.load_model(f"models/{player}/{models[int(model_selection)]}")

        original_image = cv2.imread(f"images/{folders[int(test_example)]}.jpg", 0)
        
        cv2.imshow('image', original_image)

        n_items = len(listar_elementos(f"images/{folders[int(test_example)]}"))

        items = []

        for i in range(n_items//2):
            items.append(cv2.imread(f"images/{folders[int(test_example)]}/{i}.jpg", 0))
            items.append(cv2.imread(f"images/{folders[int(test_example)]}/{i}_R.jpg", 0))


        for item in items:
            predict = tf_model.predict(item.reshape(1, 784))
            
            plt.imshow(item, cmap='binary_r')
            plt.xlabel(f"Yo digo que es: {classes[np.argmax(predict)]}")
            plt.show()

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()