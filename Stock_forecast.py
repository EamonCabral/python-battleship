# Analytics test on Power DAH and forecast analytics
# Loading and building data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
import os

"""
First we will read the dataset witha ll info from Intraday trading of AAPL stock
We will use Pandas to read file and extract raw data as given on www.kaggle.com
Next we will extract the useful training data and have everything ready to run the model
"""

dataset = pd.read_csv('AAPL_dataset.csv')


print(dataset.head())

# We will create a simple list with all indexed columns, just so we can keep track of data
columns = []

for i in range(len(dataset.columns)):
    columns.append(dataset.columns[i])

# Since we are interested in forecasting the future opening price, we will use this as our training data
opn_price = dataset['open'].values
opn_price = opn_price.reshape(-1,1)
print(opn_price[:5],'\n')

"""
Now that we have extracted the prices to train the model, we will proceed to use everything accordingly
"""

# Training data split
data_train = np.array(opn_price[:int(opn_price.shape[0] * 0.80)]) # we will be using 80% Opening price data
data_test = np.array(opn_price[int(opn_price.shape[0] * 0.80)-50:]) # the remaining 20 are used, plus 50 overlapping

print(data_train.shape)
print(data_test.shape)

# Recall Linear regression problems work best with normalized data
"""
We could either hard code the math (see below) or use MinMaxScaler

def featscaling(Input):
    Normalized = []
    for i in Input:
        Xmin = min(Input)
        Xmax = max(Input)
        Normalized.append( (i - Xmin ) / (Xmax - Xmin) );

    Normalized = np.array(Normalized)
    return Normalized

Train_norm = featscaling(data_train);
print(Train_norm[:5],'\n')
"""

"""
 Alternatively, use normal trasformation from MinMaxScaler function (skitlearn)
"""
scaler = MinMaxScaler(feature_range=(0,1))

train_scaled = scaler.fit_transform(data_train)
test_scaled = scaler.transform(data_test)

print(train_scaled[:5])
print(test_scaled[:5],'\n')

"""
Now we proceed to create the dataset using X - Y vals
"""

def build_dataset(Input_Dataset):
    X = []
    Y = []
    for i in range(50,Input_Dataset.shape[0]):
        X.append(Input_Dataset[i-50:i, 0])
        Y.append(Input_Dataset[i,0])
    X = np.array(X)
    Y = np.array(Y)
    return X,Y

x_train, y_train = build_dataset(train_scaled)
print(x_train[:1])
print(x_train.shape,'\n')

x_test, y_test = build_dataset(test_scaled)
print(x_test[:1])
print(x_test.shape,'\n')

# Reshape features for LSTM Layer
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Building RNN model

model = Sequential()
model.add(LSTM(units=96, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=96, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

if(not os.path.exists('stock_prediction.h5')):
    model.fit(x_train, y_train, epochs=50, batch_size=32)
    model.save('stock_prediction.h5')

model = load_model('stock_prediction.h5')


predictions = model.predict(x_test)
predictions_scaled = scaler.inverse_transform(predictions)

# fig, ax = plt.subplots(figsize=(8,4))
# plt.plot(opn_price, color='red', label='Real Price')
# ax.plot(range(len(y_train)+50,len(y_train)+50+len(predictions_scaled)),predictions_scaled, color='blue',label='Predicted Test Stock Price')
# plt.legend()

y_test_scaled = scaler.inverse_transform(y_test.reshape(-1,1))

# fig, ax = plt.subplots(figsize=(8,4))
# ax.plot(y_test_scaled, color='red',label='True Stock Testing Price')
# plt.plot(predictions_scaled, color='blue', label='Predicted Stock Test Price')
# plt.legend()

x = x_test[-1]
no_timestep = 100
preds = []

for i in range(no_timestep):
    preds_data = np.expand_dims(x, axis=0)
    predicted = model.predict(preds_data)
    predicted = scaler.inverse_transform(predicted)
    preds.append(predicted[0][0])
    x = np.delete(x, 0, axis=0) # Deleting first row
    x = np.vstack([x, predicted])  # Adding newly predicted value

print(preds)

