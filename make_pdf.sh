#!/bin/bash

tiffcp $(ls -v1 *.tif) all.tiff
tiff2pdf all.tiff > output.pdf
pdfnup --nup 2x1 output.pdf --outfile nup.pdf
pdfcrop -margins '25 25 25 25' nup.pdf final.pdf
