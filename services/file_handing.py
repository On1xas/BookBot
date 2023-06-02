import os
import re

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text, start, page_size):
    if len(text[start:])>page_size:
        if "?.." in text and text.index("?..")<page_size<text.index("?..")+3:
            page_size=text.index("?..")-1
        elif "!.." in text and text.index("!..")<page_size<text.index("!..")+3:
            page_size=text.index("!..")-1
        elif "..." in text and text.index("...")<page_size<text.index("...")+3:
            page_size=text.index("...")-1
        regex=r'\?\.\.|\?!|[,:;!?]|\.{3}|\.'
        match=re.search(regex, text[start+page_size-1:start:-1])
        result=text[start:start+page_size-match.span(0)[0]]
    else:
        result=text[start:]
    return (result, len(result))


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as books:
        text=books.read()
    start = 0
    page=0
    while start < len(text):
        result =_get_part_text(text, start, PAGE_SIZE)
        page+=1
        start+=result[1]
        book[page]=book.get(page,result[0].lstrip())


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))