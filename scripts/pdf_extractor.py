from pypdf import PdfReader, PdfWriter

reader = PdfReader("docs/test-4-pages.pdf")
writer = PdfWriter()

for page in reader.pages[0:1]:
    writer.add_page(page)

with open("docs/test-image.pdf", "wb") as f:
    writer.write(f)

print("Test PDF ready:", len(writer.pages), "pages")