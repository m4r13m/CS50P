from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="portrait", format="A4")
pdf.set_display_mode(zoom="default", layout="TWO_COLUMN_LEFT")
pdf.set_font("helvetica", size=30)
pdf.add_page()
pdf.cell(text="CS50 Shirtificate")
pdf.image("shirtificate.png", h=pdf.eph, w=pdf.epw)
pdf.set_font(style="U")
pdf.cell(text=f"{name} took CS50")
pdf.output("shirtificate.pdf")
