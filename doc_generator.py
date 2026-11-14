
from docx import Document

class DocGenerator:
    def save_as_word(self, text, filename):
        doc = Document()
        doc.add_paragraph(text)
        doc.save(filename)
        return filename
