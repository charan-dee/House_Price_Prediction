
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("house_data.csv", sep="\t")
print(data.columns.tolist())

df = pd.get_dummies(data, columns=['Location'])

X = df.drop('Price', axis=1)
Y = df['Price']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)

def predict_price(area, bedrooms, bathrooms, age, location, parking):

    new_house = pd.DataFrame(0, index=[0], columns=X.columns)

    new_house['Area'] = area
    new_house['Bedrooms'] = bedrooms
    new_house['Bathrooms'] = bathrooms
    new_house['Age'] = age
    new_house['Parking'] = parking

    location_column = 'Location_' + location

    if location_column not in new_house.columns:
        raise ValueError("Location not found")

    new_house[location_column] = 1

    price = model.predict(new_house)

    return round(price[0], 2)
