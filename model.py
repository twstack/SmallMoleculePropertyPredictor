import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# Load the data
file_path = 'chembl_data.csv'
data = pd.read_csv(file_path)

# Drop rows with NaN values in features and target columns
features = ['aromatic_rings', 'full_mwt', 'hba', 'hbd']
data = data.dropna(subset=features + ['alogp'])

X = data[features]
y = data['alogp']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
r2 = r2_score(y_test, y_pred)
print(f'R2 Score: {r2}')

# Scatter plot of Actual vs Predicted values
plt.scatter(y_test, y_pred, alpha=0.5)
plt.title('Actual vs Predicted alogP')
plt.xlabel('Actual alogP')
plt.ylabel('Predicted alogP')

# Plot a line representing perfect predictions
min_val = min(min(y_test), min(y_pred))
max_val = max(max(y_test), max(y_pred))
plt.plot([min_val, max_val], [min_val, max_val], 'r', label='Perfect Predictions Line')

plt.legend()
plt.show()