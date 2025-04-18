#  polyglot-generator

A simple Python tool to create **polyglot files** by combining a valid image or document (JPEG, PNG, PDF, DOCX, MP4, etc.) with PHP shell code.

---

##  Features

✅ Generate polyglot files that pass file-type validation and can still execute PHP code on vulnerable servers.  
✅ Supports multiple file format combinations:

-  **JPEG + PHP**
-  **PDF + PHP**
-  **DOCX + PHP**
-  **MP4 + PHP**

---

## 🚀 Installation

### 1. Clone the repository
git clone https://github.com/Pranieth95/polyglot-generator.git

### 2. Install dependencies (You need Python 3.x to run the script)

#### Option A: Install via requirements.txt
pip install -r requirements.txt

#### Option B: Install manually
pip install Pillow python-magic

## ⚙️ Usage - Basic Syntax
python polyglot_generator.py --input INPUT_FILE --shell PHP_SHELL_FILE --type FILE_TYPE --output OUTPUT_FILE

### Arguments
--input: Valid image or document file to use (e.g., input.jpg, input.pdf)

--shell: PHP shell file to inject (e.g., shell.php)

--type: Type of file you want to generate (jpeg, pdf, docx, mp4, etc.)

--output: Output polyglot file name (e.g., polyglot.php)

### Example: JPEG + PHP
python polyglot_generator.py --input image.jpg --shell exploit.php --type jpeg --output polyglot.php

## 🔍 How It Works
1) The script reads the input image or document file.

2) It appends or injects the provided PHP code into the file while preserving its original structure and signature.

3) Based on the specified type, the tool creates a polyglot file that behaves as both a valid file (e.g., image/pdf) and an executable PHP script.

4) The output file can be used for testing file upload vulnerabilities in web security assessments.

 ## ⚠️ Disclaimer
This tool is for educational and ethical web security testing only. Do NOT use it on any systems without explicit permission.
