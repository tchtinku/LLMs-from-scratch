#### Additional Classification Finetuning Experiments

###### The table below adds experiments to answer additional questions about various design choices. The first row uses the same settings as the main chapter and is used as a reference. For example,

###### comparing rows 1 and 2 answers the question: "What is the performance difference when we train the last or first token?";
###### comparing rows 1 and 3 answers the question: "What is the performance difference when we train only the last layer instead of the last block?";
###### and so forth.

#### Usage

###### You can use the following code to reproduce the experiments:

###### Row 1: python additional_experiments.py
###### Row 2: python additional_experiments.py --trainable_token_pos first
###### Row 3: python additional_experiments.py --trainable_layers last_layer
###### Row 4: python additional_experiments.py --trainable_layers last_two_blocks
###### Row 5: python additional_experiments.py --trainable_layers all
###### Row 6: python additional_experiments.py --model_size "gpt2-medium (355M)"
###### Row 7: python additional_experiments.py --model_size "gpt2-large (774M)"
###### Row 8: python additional_experiments.py --model_size "gpt2-xl (1558M)"
###### Row 9: python additional_experiments.py --model_size "gpt2-xl (1558M)"--trainable_layers all
###### Row 10: python additional_experiments.py --weights random --trainable_layers all
###### Row 11: python additional_experiments.py --trainable_layers lora --lora_rank 16 --lora_alpha 16
###### Row 12: python additional_experiments.py --trainable_layers lora --lora_rank 16 --lora_alpha 8 --model_size "gpt2-xl (1558M)"
###### Row 13: python additional_experiments.py --context_length "model_context_length"
###### Row 14: python additional_experiments.py --no_padding --batch_size 1
###### Row 15: python additional_experiments.py --no_padding --batch_size 1 --accumulation_steps 8
###### Row 16: python additional_experiments.py --trainable_token_pos "flexible"
###### Row 17: python additional_experiments.py --disable_causal_mask
###### Row 18: python additional_experiments.py --ignore_index 50256
###### Row 19: python additional_experiments.py --average embeddings

###### I've kept the LLM and dataset small on purpose, so you can run the training on a regular laptop like a MacBook Air M3 in about 15 minutes (for the default setting) in case you don't have access to a GPU.

#### Interpretation

###### Training the Last vs. First Output Token Position (Row 1 vs. 2): Training the last output token position results in substantially better performance compared to the first. This improvement is expected due to the causal self-attention mask.
###### Training the Last Transformer Block vs. Last Layer (Row 1 vs. 3): Training the entire last transformer block is also results in substantially better results than training only the last layer.
###### Training the Last vs. Last Two Last Transformer Blocks (Row 1 vs. 4): Training the two last transformer blocks instead of only the last block results in a noticeable 3.33% accuracy boost.
###### Training Last Transformer Block vs All Layers (Row 1 vs. 5): Training all layers shows a modest improvement of ~2% over just training the last transformer block, but it requires almost three times longer in terms of training duration. Also, it does not perform as well as training only the last two out of 12 transformer blocks.
###### Using Larger Pretrained Models (Row 1 vs 6, and Row 1 vs. 7 and 8): Employing a 3x larger pretrained model leads to worse results. However, using a 5x larger model improves performance compared to the initial model, as was anticipated. Similarly, the 12x larger model improves the predictive performance even further. (The medium model was perhaps not well pretrained or the particular finetuning configuration works not as well for this model.)
###### Using a Model with Random Weights vs. Pretrained Weights (Row 1 and 5 vs. 10): Utilizing a model with random weights yields results that are only slightly worse (by 3% and 1.3%) compared to using pretrained weights.
###### Using LoRA (Low-Rank Adaptation) vs Training All Layers (Row 11 vs. 5, and row 12 vs. 9): Keeping the model frozen and adding trainable LoRA layers (see Appendix E for details) is a viable alternative to training all model parameters and even improves the performance by 1% point (row 11 vs. 5). As it can be seen by the ~1% lower gap between the training and validation accuracy when using LoRA, this is likely due to less overfitting. Moreover, using LoRA is also more memory-efficient because fewer parameters have to be updated. When training the larger model (row 12 vs. 9), we can also see that LoRA trains much faster (5.79 min instead of 8.12 min).
###### Padding Input to Full Context Length vs. Longest Training Example (Row 1 vs. 13): Padding the input to the full supported context length results is significantly worse.
###### Padding vs no padding (Row 1 vs. 14 & 15, and 16): The --no_padding option disables the padding in the dataset, which requires training the model with a batch size of 1 since the inputs have variable lengths. This results in a better test accuracy but takes longer to train. In row 15, we additionally enable gradient accumulation with 8 steps to achieve the same batch size as in the other experiments, which helps reduce overfitting and slightly boost the test set accuracy. In row 16, padding is applied, but the token position is selected based on the last non-padding token. Row 16 should be mathematically similar to row 15, which uses gradient accumulation. However, due to some challenges with gradient accumulation in cases of unequal token counts, there may be small discrepancies (this is discussed in this blog post).
###### Disabling the causal attention mask (Row 1 vs. 17): Disables the causal attention mask used in the multi-head attention module. This means all tokens can attend all other tokens. The model accuracy is slightly improved compared to the GPT model with causal mask.
###### Ignoring the padding indices in the loss and backpropagation (Row 1 vs. 18): Setting --ignore_index 50256 excludes the |endoftext| padding tokens in the cross_entropy loss function in PyTorch. In this case, it does not have any effect because we replaced the output layers so that the token IDs are either 0 or 1 for the binary classification example. However, this setting is useful when instruction finetuning models in chapter 7.
###### Averaging the embeddings over all tokens (Row 1 vs. 19): Setting --average_embeddings will average the embeddings over all tokens. If this option is not used (the default), only the output embeddings at the chosen token position (specified by --trainable_token_pos) are considered; for example, the embeddings of the last token. Enabling --average_embeddings will mean-pool the embeddings of all tokens into the position chosen by --trainable_token_pos (the last token by default). As we can see, this improves the performance from 95.00% to 96.33% with only a minimal increase in run time (0.28 min to 0.32 min) and might be worthwhile considering in practice.