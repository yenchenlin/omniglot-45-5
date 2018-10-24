# omniglot-45-5

This repo contains the code to get Omniglot 45-5 split dataset used for few-shot density estimation [1, 2, 3].

## Usage
```
git clone git@github.com:yenchenlin/omniglot-45-5.git
cd omniglot-45-5
bash get_dataset.sh
```

Then, the layout of `omniglot-45-5` should be:
```
.
├── train/                  # Repository contains the training split (45 alphabets)
├── test/                   # Repository contains the testing split (5 alphabets)
├── get_dataset.sh          # Main script
├── preprocessing.py        # Preprocessing script
├── LICENSE
└── README.md
```

## Reference
```
[1] One-Shot Generalization in Deep Generative Models, Rezende et al.
[2] Variational Memory Addressing in Generative Models, Bornschein et al.
[3] Few-shot Autoregressive Density Estimation: Towards Learning to Learn Distributions, Reed et al.
```
