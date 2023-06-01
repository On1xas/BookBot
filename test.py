import re

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


text = '— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, в чём вопрос.'

print(*_get_part_text(text, 54, 70), sep='\n')

# start=54
# page_size=70
# regex=r'[,:;!?]|[\.]{3}|\.'
# match=re.search(regex, text[start+page_size-1:start:-1])
# print(start)
# print(start+page_size)
# print(text[start:start+page_size])
# if match:
#     print(match.span(0)[0])
#     print(text[start:start+page_size-match.span(0)[0]])
PAGE_SIZE=1050
book=dict()
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

prepare_book(r'D:\BookBot\book\book.txt')
print()