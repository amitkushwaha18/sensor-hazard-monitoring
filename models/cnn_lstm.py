"""Reference CNN-LSTM architecture for the intended deep-learning model."""
try:
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Conv1D, MaxPooling1D, LSTM, Dropout, Dense
    def build_cnn_lstm(input_shape, filters=32, lstm_units=64, dropout=0.2, classes=7):
        m=Sequential([Conv1D(filters,3,activation='relu',input_shape=input_shape),MaxPooling1D(2),Conv1D(filters*2,3,activation='relu'),LSTM(lstm_units),Dropout(dropout),Dense(32,activation='relu'),Dense(classes,activation='softmax')])
        m.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy']); return m
except ImportError:
    def build_cnn_lstm(*args,**kwargs): raise ImportError('Install TensorFlow to train the CNN-LSTM model.')
