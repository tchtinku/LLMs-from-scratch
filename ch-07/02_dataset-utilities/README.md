#### Chapter 7: Finetuning to Follow Instructions

###### This folder contains utility code that can be used for preparing an instruction dataset.

###### Install the additional package requirements via:

###### pip install -r requirements-extra.txt

##### Finding Near Duplicates

###### The find-near-duplicates.py function can be used to identify duplicates and near-duplicates in an instruction dataset. For example,

###### python find-near-duplicates.py --json_file instruction-examples.json

###### You can use the --threshold setting with a value between 0 and 1 to decrease or increase the sensitivity. The default threshold is 0.9.

##### Creating Passive Voice Entries

###### The create-passive-voice-entries.ipynb notebook uses OpenAI's GPT-4 to create "passive voice" entries for an instruction dataset, as shown in the example below