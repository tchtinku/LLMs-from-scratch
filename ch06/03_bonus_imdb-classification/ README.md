#### Additional Experiments Classifying the Sentiment of 50k IMDB Movie Reviews

##### Step 1: Install Dependencies
###### pip install -r requirements-extra.txt

##### Step 2: Download Dataset
###### The codes are using the 50k movie reviews from IMDb (dataset source) to predict whether a movie review is positive or negative.

###### Run the following code to create the train.csv, validation.csv, and test.csv datasets:
###### python download_prepare_dataset.py

##### Step 3: Run Models

###### The 124M GPT-2 model used in the main chapter, starting with pretrained weights, and finetuning all weights:
###### python train_gpt.py --trainable_layers "all" --num_epochs 1

###### A 340M parameter encoder-style BERT model:
###### python train_bert_hf.py --trainable_layers "all" --num_epochs 1 --model "bert"

###### A 66M parameter encoder-style DistilBERT model (distilled down from a 340M parameter BERT model), starting for the pretrained weights and only training the last transformer block plus output layers:

###### python train_bert_hf.py --trainable_layers "all" --num_epochs 1 --model "distilbert"

###### A 355M parameter encoder-style RoBERTa model, starting for the pretrained weights and only training the last transformer block plus output layers:

###### python train_bert_hf.py --trainable_layers "last_block" --num_epochs 1 --model "roberta" 

###### A scikit-learn logistic regression classifier as a baseline:

###### python train_sklearn_logreg.py


