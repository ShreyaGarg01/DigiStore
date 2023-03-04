import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression

# convert the dataset into csv
inventory_data = pd.read_csv("inventory.csv") 


X_train, X_test, y_train, y_test = train_test_split(
    inventory_data.drop("sales", axis=1), inventory_data["sales"], test_size=0.2, random_state=42
)

model = LinearRegression()


model.fit(X_train, y_train)


predictions = model.predict(X_test)

# accuracyy of model
score = model.score(X_test, y_test)
print(f"Model score: {score:.2f}")


