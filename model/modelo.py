import pickle
import numpy as np
import joblib

class Modelo:

    def carrega_modelo(self, path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                modelo = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return modelo
    
    def preditor(self, modelo, X_input):
        """Realiza a predição de um cliente com base no modelo treinado
        """
        diagnosis = modelo.predict(X_input)
        return diagnosis