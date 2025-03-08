Installing Python Packages and Libraries Used In This Book

This document provides more information on double-checking your installed Python version and packages. (Please see the ../01_optional-python-setup-preferences folder for more information on installing Python and Python packages.)

I used the following libraries listed here for this book. Newer versions of these libraries are likely compatible as well. However, if you experience any problems with the code, you can try these library versions as a fallback.

Note: If you you are using uv as described in Option 1: Using uv, you can replace pip via pip uv in the commands below. For example, pip install -r requirements.txt becomes uv pip install -r requirements.txt
To install these requirements most conveniently, you can use the requirements.txt file in the root directory for this code repository and execute the following command:

pip install -r requirements.txt
Alternatively, you can install it via the GitHub URL as follows:

pip install -r https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/requirements.txt
Then, after completing the installation, please check if all the packages are installed and are up to date using

python python_environment_check.py


It's also recommended to check the versions in JupyterLab by running the python_environment_check.ipynb in this directory, which should ideally give you the same results as above.



If you see the following issues, it's likely that your JupyterLab instance is connected to wrong conda environment:



In this case, you may want to use watermark to check if you opened the JupyterLab instance in the right conda environment using the --conda flag:



 

Installing PyTorch

PyTorch can be installed just like any other Python library or package using pip. For example:

pip install torch
However, since PyTorch is a comprehensive library featuring CPU- and GPU-compatible codes, the installation may require additional settings and explanation (see the A.1.3 Installing PyTorch in the book for more information).

It's also highly recommended to consult the installation guide menu on the official PyTorch website at https://pytorch.org.

