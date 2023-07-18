import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

filepath = tf.keras.utils.get_file('The%203%20Kingdoms_djvu.txt',
                                   'https://archive.org/stream/The3Kingdoms/The%203%20Kingdoms_djvu.txt')

text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()

text = text[300000:8000000]

characters = sorted(set(text))

char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))

SEQ_LENGTH = 40
STEP_SIZE = 3

##Uncomment when creating a new file
# sentences = []
# next_characters = []
#
# for i in range(0,len(text) - SEQ_LENGTH, STEP_SIZE):
#     sentences.append(text[i:i+SEQ_LENGTH])
#     next_characters.append(text[i+SEQ_LENGTH])
#
# x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=bool)
# y = np.zeros((len(sentences), len(characters)), dtype=bool)
#
# for i, sentence in enumerate(sentences):
#     for t, character in enumerate(sentence):
#         x[i, t, char_to_index[character]] = 1
#         y[i, char_to_index[next_characters[i]]] = 1


##uncomment when parsing file
model = tf.keras.models.load_model('textgeneratorr3k.model')

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
    generated = ''
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, character in enumerate(sentence):
            x[0, t, char_to_index[character]] = 1

        predictions = model.predict(x, verbose=0)[0]
        next_index = sample(predictions, temperature)
        next_character = index_to_char[next_index]

        generated += next_character
        sentence = sentence[1:] + next_character
    return generated

print('----------.2----------')
print(generate_text(300, 0.2))

print('----------.4----------')
print(generate_text(300, 0.4))

print('----------.6----------')
print(generate_text(300, 0.6))

print('----------.8----------')
print(generate_text(300, 0.8))

print('----------1.0----------')
print(generate_text(300, 1.0))

print('----------1.2----------')
print(generate_text(300, 1.2))


##Uncomment when creating a new file
# model = Sequential()
# model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters))))
# model.add(Dense(len(characters)))
# model.add(Activation('softmax'))
#
# model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01))
#
# model.fit(x, y, batch_size=256, epochs=4)
#
# model.save('textgeneratorr3k.model')
