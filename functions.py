from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
import config as conf
from reportlab.lib.units import cm, mm
from reportlab.lib.utils import ImageReader

def table_content(preitog: dict):
    """Функция для преобразования словаря в табличный формат"""
    table = [['+', '-']]
    def pl(preitog):
        for keys, table_content in preitog.items():
            if '+' in keys and table_content != '':
                row = [table_content, ' ']
                table.append(row)
            else:
                pass
        return table

    def mn(preitog):
        for keys, table_content in preitog.items():
            if '-' in keys and table_content != '':
                row = [' ', table_content]
                table.append(row)
            else:
                pass
        return table

    num_pl = 0
    num_mn = 0
    for keys, table_content in preitog.items():
        if '+' in keys and table_content != '':
            num_pl += 1
        elif '-' in keys and table_content != '':
            num_mn += 1
    if num_pl >= num_mn:
        pl(preitog)
        n = 0
        for keys, table_content in preitog.items():
            if '-' in keys and table_content != '':
                table[n + 1][1] = table_content
                n += 1
    else:
        mn(preitog)
        n = 0
        for keys, table_content in preitog.items():
            if '+' in keys and table_content != '':
                table[n + 1][0] = table_content
                n += 1
    return table

def para_4_table(users_table):
    """Функция для преобразования данных таблицы в ячейки с учетом стиля и размеров ячеек"""
    for i in range(len(users_table)):
        for j in range(len(users_table[i])):
            if '+' in users_table[i][j] or '-' in users_table[i][j]:
                p = Paragraph(users_table[i][j], conf.style_title)
                users_table[i][j] = p
            else:
                p = Paragraph(users_table[i][j], conf.style)
                users_table[i][j] = p


def table_style(users_table):
    """Функция для задания стиля таблице"""
    table = Table(users_table)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), conf.my_color),
                               ('TEXTCOLOR', (0, 0), (-1, 0), conf.colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                               ('BOTTOMPADDING', (0, 1), (-1, -1), 12),
                               ('GRID', (0, 0), (-1, -1), 1, colors.white)]))
    return table

def add_page_numb(canvas, doc):
    """Добавляет нумерацию страниц"""
    page_num = canvas.getPageNumber()
    canvas.setFont('TimesNewRoman', 10)
    page = f'Страница {page_num}'
    canvas.drawCentredString(10*cm, cm, page)

def add_logo(canvas, doc):
    """Добавляет логотип"""
    img = ImageReader("logo.jpg")
    canvas.drawImage(img, 3.1 * cm, 297 * mm - 2.88 * cm, width=6.85 * cm, height=1.88 * cm)

def add_every_page(canvas, doc):
    """Вызывает фунции нумерации и логотипа на каждую страницу"""
    add_logo(canvas, doc)
    add_page_numb(canvas, doc)