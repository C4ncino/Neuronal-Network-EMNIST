import random
import tensorflow as tf
from matplotlib import pyplot as plt 
import numpy as np
import seaborn as sns
import pandas as pd
from models import path, player
from models import model_jp, model_cancino, epochs_jp, epochs_cancino
from class_mapping import classes

def load_dataset(path: str) -> tuple[pd.DataFrame, pd.Series]:
    """
    Loads the dataset from a csv file and normalizes it.

    Args:
        path (str): The path to the csv file.

    Returns:
        x: The normalized dataset.
        y: The labels of the dataset.
    """

    train_dataset = pd.read_csv(path, header=None)

    x = train_dataset.drop(columns=0)
    y = train_dataset[0]

    x = x / 255

    return x, y


def train(x_train: pd.DataFrame, y_train: pd.Series, x_test: pd.DataFrame, y_test: pd.Series, model_path: str, player: str)-> tf.keras.Sequential:
    """
    Train the model using the training set and saves it to the path specified.

    Args:
        x_train: The training set.
        y_train: The labels of the training set.
        x_test: The test set.
        y_test: The labels of the test set.
        model_path: The path where the model will be saved.
        player: The player that will be used to train the model.
    
    Returns:
        model: The trained model.
    """


    if player == 'cancino':
        model = model_cancino
        epochs = epochs_cancino

    else:
        model = model_jp
        epochs = epochs_jp

    print("Compiling...")

    model.compile(
        optimizer = 'adam', 
        loss="sparse_categorical_crossentropy",
        metrics=['accuracy']
    )

    print("Training...")
    model_history = model.fit(
        x_train, 
        y_train, 
        epochs=epochs, 
        batch_size=128,
        validation_data=(x_test, y_test)
    )

    plt.plot(model_history.history['loss'])
    plt.plot(model_history.history['val_loss'])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()

    model.save(f'{model_path}.h5')

    return model


def test(model: tf.keras.Sequential, x_test: pd.DataFrame, y_test: pd.Series) -> None:
    """
    Test the model using the test set making one prediction at random
    pltoting the image and the prediction and 
    calculating the confusion matrix.

    Args:
        model: The trained model.
        x_test: The test set.
        y_test: The labels of the test set.
    """

    predict = model.predict(x_test)

    n = random.randint(0, 10000)

    row_array = x_test.iloc[n].values.flatten()

    image_array = row_array.reshape((28, 28))

    plt.imshow(image_array, cmap='binary_r')
    plt.title(f"Esto es: {classes[y_test[n]]}")
    plt.xlabel(f"Yo digo que es: {classes[np.argmax(predict[n])]}")
    plt.show()

    # PREDICCIÓN
    predict = model.predict(x_test)

    # MATRIZ DE CONFUSION
    conf_matrix = tf.math.confusion_matrix(y_test, np.argmax(predict, axis=1))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("Reales")
    plt.show()

    # ACCURACY
    print(f"Accuracy: {model.evaluate(x_test, y_test)}")


def menu():
    """
    Prints the menu to the user.
    """

    print('1. Train and test')
    print('2. Just train')
    print('3. Just test')
    print('0. Exit')


def main(model_path: str, player: str) -> None:
    """
    Menu that allows the user to choose between training and testing a model.

    Args:
        model_path: The path where the model will be saved.
        player: The player that will be used to train the model.
    """

    op = ' ' 

    while op != '0':
        menu()

        op = input('Enter an option: ')
        
        if op == '1' or op == '2' or op == '3':
            x_test, y_test = load_dataset('data/test.csv')

            if op == '1' or op == '2':
                x_train, y_train = load_dataset('data/train.csv')

                model = train(x_train, y_train, x_test, y_test, model_path, player)

            else:
                model = tf.keras.models.load_model(f"{model_path}.h5")
            
            if op != '2':
                test(model, x_test, y_test)


if __name__ == '__main__':
    main(path, player)
