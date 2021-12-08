import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r'#+\s(?P<position>\d+)' \
             r'\.\s\[(?P<book>[^\]]+)\]' \
             r'\((?P<book_url>[^\)]+)\)' \
             r'\sby\s+(?P<author>\S[^\)]+\S)' \
             r'\s+\((?P<recommended>[0-9\.%]+)[^\)]+\)' \
             r'\n*!\[\]\((?P<cover_url>[^\)]+)\)' \
             r'\n*"(?P<description>[^"]+)"'
# TODO записать ругулярное выражения для поиска книги
def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)
    # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
'''
#### 25. [Python: Learn Python in One Day and Learn It Well](https://amzn.to/2VFKJcf) 
 by Jamie Chan (7.9% recommended)
![](https://www.daolf.com/images/python_book_list/25.png#center)'''
