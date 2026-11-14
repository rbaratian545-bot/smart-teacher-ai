
from pptx import Presentation
from pptx.enum.text import PP_ALIGN

class PPTGenerator:
    def create_ppt(self, content):
        prs = Presentation()
        slide = prs.slides.add_slide(prs.slide_layouts[0])
        title = slide.shapes.title
        title.text = "SmartTeacher AI"
        prs.save("output.pptx")
        return "output.pptx"
