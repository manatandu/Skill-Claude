import pymupdf

doc = pymupdf.open()
page = doc.new_page(width=595, height=842)  # A4

# --- Encadré deux colonnes (type "Figure" EY) : deux blocs cote a cote
page.draw_rect(pymupdf.Rect(50, 60, 545, 240), color=(0.3,0.3,0.3))
page.draw_line(pymupdf.Point(297, 60), pymupdf.Point(297, 240))
page.insert_textbox(pymupdf.Rect(60, 70, 290, 235),
    "Relevance\n\nRelevant sustainability-related financial information is capable of "
    "making a difference in the decisions made by primary users. It has predictive "
    "value, confirmatory value or both.", fontsize=9)
page.insert_textbox(pymupdf.Rect(305, 70, 535, 235),
    "Faithful representation\n\nInformation represents phenomena in words and numbers. "
    "Faithful representation is achieved when the depiction is complete, neutral and "
    "accurate.", fontsize=9)

# --- Tableau chiffre avec filets
page.insert_text(pymupdf.Point(50, 285), "Table 8: Financed emissions by asset class", fontsize=10)
rows = [
    ["", "Long-term bonds", "Publicly traded equities", "Total"],
    ["Scope 1", "48,600,415", "101,487,332", "150,087,747"],
    ["Scope 2", "33,805,025", "27,187,765", "60,992,790"],
    ["Scope 3", "159,615,008", "301,001,718", "460,616,726"],
    ["Total reported", "242,020,448", "429,676,815", "671,697,263"],
]
x = [50, 190, 300, 420, 545]
y0, h = 300, 22
for i, row in enumerate(rows):
    yt = y0 + i*h
    page.draw_line(pymupdf.Point(50, yt), pymupdf.Point(545, yt))
    for j, cell in enumerate(row):
        page.insert_textbox(pymupdf.Rect(x[j]+3, yt+5, x[j+1]-3, yt+h),
                            cell, fontsize=8)
page.draw_line(pymupdf.Point(50, y0+len(rows)*h), pymupdf.Point(545, y0+len(rows)*h))
for xi in x:
    page.draw_line(pymupdf.Point(xi, y0), pymupdf.Point(xi, y0+len(rows)*h))

doc.save("test.pdf")
print("ok")
