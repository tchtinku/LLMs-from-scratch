#### Chapter 7: Finetuning to Follow Instructions

##### Main Chapter Code

###### ch07.ipynb contains all the code as it appears in the chapter
###### previous_chapters.py is a Python module that contains the GPT model we coded and trained in previous chapters, alongside many utility functions, which we reuse in this chapter
###### gpt_download.py contains the utility functions for downloading the pretrained GPT model weights
###### exercise-solutions.ipynb contains the exercise solutions for this chapter

##### Optional Code

###### load-finetuned-model.ipynb is a standalone Jupyter notebook to load the instruction finetuned model we created in this chapter

###### gpt_instruction_finetuning.py is a standalone Python script to instruction finetune the model as described in the main chapter (think of it as a chapter summary focused on the finetuning parts)

###### Usage:

###### python gpt_instruction_finetuning.py

###### ollama_evaluate.py is a standalone Python script to evaluate the responses of the finetuned model as described in the main chapter (think of it as a chapter summary focused on the evaluation parts)

###### Usage:

###### python ollama_evaluate.py --file_path instruction-data-with-response-standalone.json

###### exercise_experiments.py is an optional script that implements the exercise solutions; for more details see exercise-solutions.ipynb
