#### PyTorch Performance Tips for Faster LLM Training

###### Note that the book is written for education purposes, meaning the original code is kept purposefully simple. This is to aid readability and ensure compatibility across different hardware, including CPUs and GPUs. However, you might be curious about some more advanced PyTorch and GPU features to make the LLM training more performant.

###### This folder contains 3 code files to showcase PyTorch tips to improve the performance of the LLM and LLM training function in Chapter 5.

###### 00_orig.py: The original code from Chapter 5 for CPU and single-GPU training; run it via python 00_orig.py
###### 01_opt_single_gpu.py: The optimized code for single-GPU training; run it via python 01_opt_single_gpu.py
###### 02_opt_multi_gpu_dpp.py: The optimized code for multi-GPU training via distributed data parallelism; run it via torchrun --nproc_per_node=4 02_opt_multi_gpu_dpp.py
###### Note that these modifications take the training speed from 12,525 tokens per second (single A100) to 142,156 tokens per second (single A100) and 419,259 tokens per second (4x A100s).

###### I plan to expand on the differences in a more detailed write-up sometime in the future. For now, the easiest way to see what improvements have been added to the code is to open the files in Visual Studio Code and look at the differences via the "Compare Selected" feature.