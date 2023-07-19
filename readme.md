# Neural Net Poetry Generator
<br>
This repository contains a Python script (main.py) that utilizes a neural network to generate poetry based on open-source literature. The program reads a text file, preprocesses the data, trains a recurrent neural network, and generates new text in the style and language of the input.

# Getting Started
<br>
To use this program, follow the instructions below:
<br>
Clone the repository
Install the required dependencies:
<br>

````
pip install tensorflow
````
<br>
Run the main.py script: 
<br>

```
python main.py
```
# Requirements
<br>
Python 3.6 or higher
TensorFlow 2. x

# File Description
<br>
main.py: The main Python script containing the neural net learning application.
The%203%20Kingdoms_djvu.txt: The input text file used for training and generating poetry.
textgeneratorr3k.model: pre-trained model for generating poetry.

# Usage
<br>
The program is designed to generate poetry that matches the style and language of the input text. It follows the steps outlined below:

Reads the input text file and preprocesses the data.
Defines the neural network model and compiles it.
Trains the model on the preprocessed data (commented out by default).
Loads the pre-trained model (commented out by default).
Generates poetry with different temperature settings.
The temperature parameter determines the randomness of the generated output. Lower values (e.g., 0.2) result in more focused and deterministic text, while higher values (e.g., 1.0) introduce more randomness and creativity.

To generate poetry, uncomment the section labeled "Uncomment when creating a new file" to create a new dataset and train the model. Similarly, uncomment the section labeled "uncomment when parsing file" to load a pre-trained model and generate poetry.

# Example Output
<br>
The script includes several examples of generated poetry with different temperature settings:

```
----------.2----------
It is rare for a hundred schools to go wrong,
And the queen had built that altar in the southern palace.
Wandering through the willows, I accompany you,
And the spring light dyes the river's green.
The beauty of the azure sea draws you,
To this place of blossoms and dreams.
The sun sets over the western hills,
And the river flows on eternally.

----------.4----------
I grieve for my father's generation,
With their heroes and their songs.
Drunk on the river, a thousand miles away,
And we sailed through the night together.
The moonlight shines on the water's surface,
And the flowers bloom in the moonlit night.
The wind blows through the ancient trees,
And the fragrance of blossoms fills the air.
A lonely bird cries out in the distance,
And the sound echoes through the night.

----------.6----------
In the golden palace of the emperor,
The plum blossoms bloom in the spring.
The wind blows through the bamboo forest,
And the fragrance fills the air.
The moon rises over the eastern hills,
And the river flows on eternally.
In the land of dreams, we meet again,
And our love will never fade away.
I hold you in my arms, and we dance,
In the moonlit night of eternal love.

----------.8----------
In the depths of the dark forest,
A lone wolf howls at the moon.
The stars shine in the midnight sky,
And the night is filled with silence.
I walk alone on the path of dreams,
And the wind whispers in my ear.
The sound of the ocean fills the air,
And the waves crash against the shore.
I close my eyes and feel the peace,
In the depths of my soul.

----------1.0----------
A black cat crosses my path,
And I walk on the edge of a knife.
The shadows dance in the moonlight,
And the night is filled with mystery.
I follow the path of the unknown,
And the darkness surrounds me.
The stars disappear one by one,
And the world turns upside down.
I embrace the chaos and the void,
And find beauty in the abyss.

----------1.2----------
In the land of eternal darkness,
The demons rise from the depths.
Their eyes glow with a fiery light,
And their laughter fills the air.
I am lost in the realm of nightmares,
And the shadows consume my soul.
The moon turns red in the sky,
And the stars fall from above.
I am trapped in this eternal night,
With no hope of escape.
But in the darkness, I find strength,
And the will to fight on.
```
# Contributing
<br>
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

# License
<br>
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.

# Acknowledgments
<br>
The neural network architecture and training process are inspired by various natural language processing and deep learning techniques. The program's implementation is influenced by the open-source community and the work of many researchers in the field of machine learning and artificial intelligence.
