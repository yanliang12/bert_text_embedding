# Text embedding for text similarity based on BERT pre-trained word embedding

Embedding a text to a vector by pre-trained BERT word embeddings and pooling layers

<img src="https://github.com/gaoyuanliang/bert_text_embedding/blob/master/bert_text_embedding_similarity.gif" width="600">

<img src="https://raw.githubusercontent.com/gaoyuanliang/bert_text_embedding/master/WX20200826-115118%402x.png" width="800">



## Instillation 

```bash
git clone https://github.com/gaoyuanliang/bert_text_embedding.git
cd bert_text_embedding
pip3 install -r requirements.txt

wget https://storage.googleapis.com/bert_models/2019_05_30/wwm_uncased_L-24_H-1024_A-16.zip
unzip wwm_uncased_L-24_H-1024_A-16.zip
```

## Usage

Within one line of code, you can convert a text to a list of 2048 numbers. We call this list the embedding vector.

```python
>>> import numpy 
>>> from jessica_text_embedding import text_embedding
>>> 
>>> x1 = text_embedding(u"Abu Dhabi Finance")
>>> x2 = text_embedding(u"Dubai Islam Bank")
>>> x3 = text_embedding(u"This is a negative")
```

check the imbedding vector and the length of the vector

```python
>>> print(x1)
[0.01866205781698227, 0.20125442743301392, -0.2105996310710907, -0.5797083973884583, 0.5044286847114563, -0.00011515617370605469, -0.9871041178703308, 0.45565372705459595,..., 1.3363279104232788]
>>> len(x1)
2048
```

check the similarity of ```(x1,x2)``` and ```(x1,x3)``` measured by the dot-product

```python
>>> numpy.dot(numpy.array(x1), numpy.array(x2))
626.4380145019333
>>> numpy.dot(numpy.array(x1), numpy.array(x3))
591.97747068839
```

The similarity between ```"Abu Dhabi Finance"``` and ```"Dubai Islam Bank"``` is largher than its similarity to ```"This is a negative"```. Since these three texts have no overlapping words at all, why ```"Abu Dhabi Finance"``` is more similar to ```"Dubai Islam Bank"``` than ```"This is a negative"```? Because the BERT word embedding has the semantic similariies. 

## TODO

Building more layers on top of the embedding of words to train these layers by supervision of similar/dissimilar pairs of texts.

Building a REST API docker image to provide text to embedding vector conversion as a service. 

If you are working on similar projects, I am happy to help. Contact me by gaoyuanliang@outlook.com
