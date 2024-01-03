import numpy as np

class LinearRegression():
    #initialize
    def __init__(self) -> None:
        self.learning_rate = 0.01
        self.iterations = 15000
    
    #predicted y value
    def yhat(self, X, weights):
        return np.dot(weights.T, X)
    
    #loss function
    def loss(self, yhat, y):
        lossret = 1/self.m * np.sum(np.power(yhat - y, 2))
        return lossret

    #gradient descent function
    def gradient_descent(self, weights, X, y, yhat):
        pass

    def main():
        pass

    