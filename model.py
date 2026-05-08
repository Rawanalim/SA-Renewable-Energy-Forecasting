from sklearn.linear_model import LinearRegression

#This function trains the model using the training data
def train_renewable_model(X_train, y_train):
    # Training a Linear Regression model for energy capacity forecasting
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

#This function generates predictions for the evaluation
def get_predictions(model, X_test):
    return model.predict(X_test)

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# This function evaluates the model performance
def evaluate_model(y_test, y_pred):
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f"R2 Score: {r2:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    return r2, mae, mse
