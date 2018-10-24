wget https://github.com/brendenlake/omniglot/raw/master/python/images_background.zip
wget https://github.com/brendenlake/omniglot/raw/master/python/images_evaluation.zip

echo "Unziping Omniglot dataset ..."
unzip -q images_background.zip
unzip -q images_evaluation.zip

mkdir tmp
mv images_background/* ./tmp
mv images_evaluation/* ./tmp

mkdir tmp/.train
mkdir tmp/.test

# Creat testing split
mv tmp/Tengwar ./tmp/.test
mv tmp/Sylheti ./tmp/.test
mv tmp/Tibetan ./tmp/.test
mv tmp/Syriac_\(Serto\) ./tmp/.test
mv tmp/ULOG ./tmp/.test

# Create training split
mv tmp/* ./tmp/.train

mv tmp/.train ./train
mv tmp/.test ./test

rm -rf tmp
rm -rf images_background
rm -rf images_evaluation
rm -rf images_background.zip
rm -rf images_evaluation.zip

python preprocessing.py
