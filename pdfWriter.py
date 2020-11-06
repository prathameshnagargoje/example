from string import hexdigits
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

width = 8
heigth = 11

canvas = Canvas('example.pdf',pagesize=A4)

canvas.drawString(width*inch,heigth*inch,'Hello World!')

canvas.save()