
title   = '20,000 leagues of und er the sea'


from fpdf import FPDF
class PDF(FPDF):
    def header (self):
        self.set_font("arial","B", 15)
        title_w = self.get_string_width(title)
        self.cell(30,10,"TITLE", border  = True, ln = 1,  align='C')
        self.ln(20)
            
    def footer(self):
        self.set_y(-15,)
        self.set_font('helvetica','I',10)
        self.cell(0,10, f'Page{self.page_no()}/{{nb}}', align='C')


pdf  = PDF ('P','mm','letter')
pdf.add_page()
pdf.set_font('helvetica','',16)
# pdf.set_text_color(100,0,0)
pdf.cell(0,10,'hello world!',ln=True)
pdf.cell(40,10,"i am valentine",ln = True)

pdf.alias_nb_pages()
pdf.set_auto_page_break(auto = True , margin= 15)


for i in range (1,41):
    pdf.cell(20,10, f'Mr neutral {i}', ln = True)

pdf.output('valy.pdf')