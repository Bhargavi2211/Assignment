import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("/annthyroid.csv")
x = dataset.iloc[:, 0:6]
y = dataset.iloc[:, 6]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

model = Sequential()
model.add(Dense(50, input_dim=6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=720, batch_size=10)

_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' %(accuracy*100))

