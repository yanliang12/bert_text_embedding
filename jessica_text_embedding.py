import numpy as np
from keras_bert import *
from keras.models import Model
from keras_bert.layers import Extract, MaskedGlobalMaxPool1D
from keras.layers import GlobalAvgPool1D, Concatenate
from keras.preprocessing.sequence import pad_sequences

model_path = 'wwm_uncased_L-24_H-1024_A-16'

paths = get_checkpoint_paths(model_path)
token_dict = load_vocabulary(paths.vocab)
tokenizer = Tokenizer(token_dict)

model = load_trained_model_from_checkpoint(
	paths.config, paths.checkpoint, 
	output_layer_num = 1)
#model.summary(line_length=120)

outputs = [
	Extract(index=0, name='Pool-NSP')(model.outputs[0]),
	MaskedGlobalMaxPool1D(name='Pool-Max')(model.outputs[0]),
	#GlobalAvgPool1D(name='Pool-Ave')(model.outputs[0]),
	]
outputs = Concatenate(name='Concatenate')(outputs)

model_sentence_emb = Model(
	inputs=model.inputs, 
	outputs=outputs)
