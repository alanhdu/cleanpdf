# cleanpdf

Helper scripts to clean up scanned PDFs (use with Scantailor). The basic
workflow would be something like:

```bash
mkdir workspace
convert.py bad.pdf workspace/
scantailor          # clean up interface in scantailor GUI
cd workspace/out
make_pdf.sh         # final pdf wil lbe in workspace/out/final.pdf
```
