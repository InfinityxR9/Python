import json
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

with open("sources.json", "r") as f:
    data = json.load(f)
    
fdx_path = data["fdxLocation"]
txtLocation = data["txtLocation"]
pdfLocation = data["pdfLocation"]

with open(fdx_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "xml")

lines = []
for para in soup.find_all("Paragraph"):
    text = para.get_text(strip=True)
    if text:
        lines.append(text)

left_aligned_text = "\n".join(lines)
with open(txtLocation, "w", encoding="utf-8") as f:
    f.write(left_aligned_text)

# TXT TO PDF

text_path = txtLocation
pdf_path = pdfLocation

with open(text_path, "r", encoding="utf-8") as f:
    text = f.read()

doc = SimpleDocTemplate(pdf_path, pagesize=LETTER)
width, height = LETTER

x_margin = 1 * inch
y_margin = 1 * inch

text_width = width - 2 * x_margin

styles = getSampleStyleSheet()

normal_style = styles["Normal"]
normal_style.fontName = "Courier"
normal_style.fontSize = 11
normal_style.leading = 14
normal_style.spaceAfter = 12

heading_style = ParagraphStyle(
    "Heading1",
    parent=normal_style,
    fontName="Courier-Bold",
    fontSize=12,
    spaceAfter=12,
)

lines = text.splitlines()
formatted_lines = []

for line in lines:
    if line.isupper():
        formatted_lines.append(Paragraph(line, heading_style))
    else:
        formatted_lines.append(Paragraph(line, normal_style))

elements = formatted_lines
doc.build(elements)

print(f"PDF successfully created at: {pdf_path}")