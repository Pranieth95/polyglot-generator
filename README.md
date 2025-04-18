# polyglot-generator
A simple Python tool to create polyglot files by combining a valid image (JPEG, PNG, PDF, DOCX, MP4, etc.) with PHP code.

Features

Create polyglot files (Combine a valid image file with PHP shell code to execute it on vulnerable application.) with multiple formats, such as:

JPEG + PHP
PDF  + PHP
DOCX + PHP
MP4  + PHP

Installation

1. Clone the repository
git clone https://github.com/YOUR-USERNAME/polyglot-generator.git
cd polyglot-generator

2. Install dependencies
You need Python 3.x to run the script. Install the required libraries using pip:
pip install -r requirements.txt

2.1 If not, you can install the necessary libraries manually:
pip install Pillow python-magic

Usage Syntax
python polyglot_generator.py --input INPUT_FILE --shell PHP_SHELL_FILE --type FILE_TYPE --output OUTPUT_FILE


INPUT_FILE: The valid image or document file you want to use (e.g., input.jpg, input.pdf).

PHP_SHELL_FILE: The PHP shell file you want to inject (e.g., shell.php).

FILE_TYPE: The type of file you want to create (jpeg, pdf, docx, mp4, etc.).

OUTPUT_FILE: The output polyglot file to be generated (e.g., polyglot.php).


Example, JPEG + PHP
python polyglot_generator.py --input input.jpg --shell shell.php --type jpeg --output polyglot.php

How It Works
The script reads an input image/document file.
It then appends or injects PHP code into the file while preserving its structure.
Depending on the file type specified, the script combines the two to generate a polyglot file that behaves as both a valid image/document and an executable PHP script.
The resulting polyglot file can then be used in web security testing to exploit file upload vulnerabilities.