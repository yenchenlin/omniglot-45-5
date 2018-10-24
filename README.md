# omniglot-45-5

<img src="https://user-images.githubusercontent.com/7057863/47463742-1cfa0580-d7b5-11e8-8b76-757430b71ab7.png" width="216" />

This repo contains the code to get Omniglot 45-5 split dataset used for few-shot density estimation [1, 2, 3].

## Download

[Here](https://github.com/yenchenlin/omniglot-45-5/blob/master/omniglot-45-5.zip) is the processed dataset.

## Usage

If you want to create the dataset yourself, run:
```
git clone git@github.com:yenchenlin/omniglot-45-5.git
cd omniglot-45-5
bash get_dataset.sh
```

Then, the layout of `omniglot-45-5` should be:
```
.
├── train/                  # Repository contains the training set (45 alphabets)
├── test/                   # Repository contains the testing set (5 alphabets)
├── get_dataset.sh          # Main script
├── preprocessing.py        # Preprocessing script
├── LICENSE
└── README.md
```

## Splits of Alphabets

- Training set:
```
Alphabet_of_the_Magi
Gurmukhi
Cyrillic
Oriya
Avesta
Gujarati
Japanese_(katakana)
Sanskrit
Japanese_(hiragana)
Korean
Malay_(Jawi_-_Arabic)
Balinese
Latin
Mkhedruli_(Georgian)
Blackfoot_(Canadian_Aboriginal_Syllabics)
Kannada
Grantha
Asomtavruli_(Georgian)
Burmese_(Myanmar)
Armenian
Old_Church_Slavonic_(Cyrillic)
Bengali
Atemayar_Qelisayer
Anglo-Saxon_Futhorc
Tifinagh
Glagolitic
Ojibwe_(Canadian_Aboriginal_Syllabics)
Braille
Manipuri
Greek
Keble
Tagalog
N_Ko
Malayalam
Early_Aramaic
Angelic
Aurek-Besh
Arcadian
Ge_ez
Inuktitut_(Canadian_Aboriginal_Syllabics)
Futurama
Mongolian
Hebrew
Syriac_(Estrangelo)
Atlantean
```

- Testing set:
```
Tengwar
Sylheti
Tibetan
Syriac_(Serto)
ULOG
```

## Reference
```
[1] One-Shot Generalization in Deep Generative Models, Rezende et al.
[2] Variational Memory Addressing in Generative Models, Bornschein et al.
[3] Few-shot Autoregressive Density Estimation: Towards Learning to Learn Distributions, Reed et al.
```
