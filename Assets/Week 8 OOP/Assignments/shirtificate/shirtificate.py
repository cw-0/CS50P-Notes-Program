from fpdf import FPDF


        

def main():
    # ---- GET NAME ----
    name = input("What's your name? ").strip().lower()

    # ---- SET PDF ----
    class PDF(FPDF):
        FPDF(orientation="P", unit="mm", format="A4")
        def header(self):
            self.image(r"D:\VScode\Projects\CS50\Week 8 OOP\Assignments\shirtificate\shirtificate.png", 85, 25, 33)
            self.set_font("helvetica", style="B", size=12)
            self.cell(75)
            self.cell(35, 10, "CS50 Shirtificate", border=1, align="C")
            self.ln(20)


    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=4)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(182, 15, f"{name.title()} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.output("shirtificate.pdf")
    print("Done.")


if __name__ == "__main__":
    main()