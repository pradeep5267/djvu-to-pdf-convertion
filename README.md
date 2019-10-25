### credits to https://github.com/theeko74 for pdf compression, https://superuser.com/questions/100572/how-do-i-convert-a-djvu-document-to-pdf-in-linux-using-only-command-line-tools for djvu to pdf conversion

### install ghostscript for running the script

### To install djvulibre
- sudo apt install djvulibre-bin

Options for compression 
-------
* `-c` or `--compress` specifies 5 levels of compression, similar to standard pdf generator level:
  * 0: default
  * 1: prepress
  * 2: printer
  * 3: ebook
  * 4: screen

### for manual operation in CLI for convertion only
- To convert djvu file into pdf (warning: the converted size is pretty big) use:
- ddjvu -format=pdf -quality=85 -verbose a.djvu a.pdf
