#%%
import argparse
import subprocess
import os.path
import sys
from shutil import copyfile


def compress(input_file_path, output_file_path, power=3):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file")
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print("Error: input file is not a PDF")
        sys.exit(1)

    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(quality[power]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.1f}MB".format(final_size / 1000000))
    print("Done.")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-i', '--input', help='Relative or absolute path of the input djvu file')
    parser.add_argument('-o', '--out', help='Relative or absolute path of the output PDF file')
    parser.add_argument('-c', '--compress', help='compresses the output pdf file')
    parser.add_argument('-c', '--compress', type=int, help='Compression level from 0 to 4')
    
    args = parser.parse_args()
    op_file_path = args.out
    ip_file_path = args.input
    compress_flag = args.compress
    # ip_file_path = './Dr_Antonio_Gulli_-_A_collection_of_Advanced_Data_Science_and_Machine_Learning_Interview_Questions_Solved_in_Python_and_Spark_II_Hands-on_Big_Data_and_Machine_Programming_Interview_Questions_.djvu'
    # op_file_path = './ooo_test2.pdf'
    print(f'input_path = {ip_file_path}')
    print(f'output_path = {op_file_path}')
    subprocess.run('ddjvu -format=pdf -quality=85 -verbose {} {}'.format(ip_file_path, op_file_path), shell=True) 
    # print(s)
    if compress_flag is not None:
        ip_file_path = op_file_path
        op_file_path = '.' + op_file_path.split('.')[-2] + '_compressed' + '.pdf'
        compress(ip_file_path, op_file_path)






if __name__ == '__main__':
    main()