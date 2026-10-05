from reportlab.pdfgen import canvas

file_name = "test_internship_offer.pdf"

pdf = canvas.Canvas(file_name)

pdf.setFont("Helvetica", 12)

text = [
    "AI INTERNSHIP SELECTION LETTER",
    "",
    "Congratulations!",
    "",
    "You have been selected for our AI Internship Program.",
    "",
    "To confirm your internship seat, you must pay a registration",
    "fee of Rs. 2,999 within 24 hours.",
    "",
    "After payment, you will receive training access and an",
    "internship certificate.",
    "",
    "Limited seats are available.",
    "",
    "Pay immediately to secure your position.",
    "",
    "Regards,",
    "AI Internship Team"
]

y = 750

for line in text:
    pdf.drawString(60, y, line)
    y -= 25

pdf.save()

print("✅ Test PDF created successfully!")