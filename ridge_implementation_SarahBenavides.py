import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Ridge Regression
class RidgeRegression():
    
    def __init__(self, learning_rate, iterations, l2_penality):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.l2_penality = l2_penality

    # Function for model training
    def fit(self, X, Y):
        # Get number of samples and features
        self.m, self.n = X.shape
        
        # Initialize weights and bias
        self.W = np.zeros(self.n)
        self.b = 0
        
        # Store features and target variable
        self.X = X
        self.Y = Y

        # History of the loss to visualize later
        self.loss_history = []

        # Perform gradient descent for the given number of iterations
        for _ in range(self.iterations):
            # Compute the gradient descent (students to implement)
            self.compute_gradient_descent()

            # Update the weights (students to implement)
            self.update_weights()

            # Track the loss at each iteration
            self.track_loss()

        return self

    # Function for computing gradient descent (students to implement)
    def compute_gradient_descent(self):
        # Placeholder for the logic to compute gradient descent
        
        #prediction
        Y_pred = self.X.dot(self.W) + self.b
        
        #error
        error = Y_pred - self.Y
        
        #gradients
        self.dW = (2 * self.X.T.dot(error)) + (2 * self.l2_penality * self.W)
        
        self.db = 2 * np.sum(error)

    # Function for updating weights (students to implement)
    def update_weights(self):
        # Placeholder for the logic to update weights using the gradients
        
        #updating coefficients
        self.W -= self.learning_rate * self.dW
        self.b -= self.learning_rate * self.db

    # Function for tracking loss history
    def track_loss(self):
        Y_pred = self.predict(self.X)   # Predicted values from current weights
        error = self.Y - Y_pred         # Calculate error (residuals)

        # Compute loss (with L2 regularization)
        loss = np.sum(error**2) + self.l2_penality * np.sum(self.W**2)
        
        # Append loss to history for visualization later
        self.loss_history.append(loss)

    # Make predictions using the current weights and bias
    def predict(self, X):
        return X.dot(self.W) + self.b


# Driver code
def main():
    # Importing dataset
    df = pd.read_csv("salary_data.csv")
    X = df.iloc[:, :-1].values   # Features (all columns except last)
    Y = df.iloc[:, -1].values    # Target variable (last column)

    # Splitting dataset into train and test set (1/3 test, 2/3 train)
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=1/3, random_state=0)

    # Create model with hyperparameters
    model = RidgeRegression(
        iterations=3000,       # Number of iterations for gradient descent
        learning_rate=1e-6,    # Learning rate for weight updates
        l2_penality=0.1       # Regularization strength
    )

    # Train model on training data
    model.fit(X_train, Y_train)

    # Prediction on the test set
    Y_pred = model.predict(X_test)

    # Print the first few predictions and their corresponding true values
    print("Predicted values ", np.round(Y_pred[:3], 2))
    print("Real values      ", Y_test[:3])

    # Visualization of predictions and loss during training
    plt.figure(figsize=(12, 5))

    # Plotting Actual vs Predicted on the test set
    plt.subplot(1, 2, 1)
    plt.scatter(X_test, Y_test, color='blue', label='Actual')
    plt.plot(X_test, Y_pred, color='red', linewidth=2, label='Predicted')
    plt.title('Ridge Regression: Predictions')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()

    # Plotting loss over iterations
    plt.subplot(1, 2, 2)
    plt.plot(model.loss_history, color='green')
    plt.title('Loss over Iterations')
    plt.xlabel('Iteration')
    plt.ylabel('Loss')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
