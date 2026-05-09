from sklearn.linear_model import LinearRegression

# Train Linear Regression forecasting model
def train_renewable_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model
