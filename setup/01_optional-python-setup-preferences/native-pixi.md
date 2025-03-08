Native pixi Python and package management

This tutorial is an alternative to the ./native-uv.md document for those who prefer pixi's native commands over traditional environment and package managers like conda and pip.

Note that pixi uses uv add under the hood, as described in ./native-uv.md.

Pixi and uv are both modern package and environment management tools for Python, but pixi is a polyglot package manager designed for managing not just Python but also other languages (similar to conda), while uv is a Python-specific tool optimized for ultra-fast dependency resolution and package installation.

Someone might choose pixi over uv if they need a polyglot package manager that supports multiple languages (not just Python) or prefer a declarative environment management approach similar to conda. For more information, please visit the official pixi documentation.

In this tutorial, I am using a computer running macOS, but this workflow is similar for Linux machines and may work for other operating systems as well.

 

1. Install pixi

Pixi can be installed as follows, depending on your operating system.


macOS and Linux

curl -fsSL https://pixi.sh/install.sh | sh
or

wget -qO- https://pixi.sh/install.sh | sh

Windows

powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
Note: For more installation options, please refer to the official pixi documentation.
 

1. Install Python

You can install Python using pixi:

pixi add python=3.10
Note: I recommend installing a Python version that is at least 2 versions older than the most recent release to ensure PyTorch compatibility. For example, if the most recent version is Python 3.13, I recommend installing version 3.10 or 3.11. You can find out the most recent Python version by visiting python.org.
 

3. Install Python packages and dependencies

To install all required packages from a pixi.toml file (such as the one located at the top level of this GitHub repository), run the following command, assuming the file is in the same directory as your terminal session:

pixi install
Note: If you encounter issues with dependencies (for example, if you are using Windows), you can always fall back to pip: pixi run pip install -U -r requirements.txt
By default, pixi install will create a separate virtual environment specific to the project.

You can install new packages that are not specified in pixi.toml via pixi add, for example:

pixi add packaging
And you can remove packages via pixi remove, for example,

pixi remove packaging
 

4. Run Python code

Your environment should now be ready to run the code in the repository.

Optionally, you can run an environment check by executing the python_environment_check.py script in this repository:

pixi run python setup/02_installing-python-libraries/python_environment_check.py

Launching JupyterLab

You can launch a JupyterLab instance via:

pixi run jupyter lab
