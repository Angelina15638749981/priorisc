import random
import re
import string
import requests

from bs4 import BeautifulSoup

# 通过读取指定文件中的行来创建所有字符串
def create_strings_from_file(filename, count):
    strings = []

    with open(filename, 'r', encoding="utf8") as f:
        lines = [l.strip()[0:200] for l in f.readlines()]
        if len(lines) == 0:
            raise Exception("没读到任何行")
        while len(strings) < count:
            if len(lines) >= count - len(strings):
                strings.extend(lines[0:count - len(strings)])
            else:
                strings.extend(lines)

    return strings

# 通过在字典中选择一个随机单词来创建所有字符串
def create_strings_from_dict(length, allow_variable, count, lang_dict):

    dict_len = len(lang_dict)
    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, random.randint(1, length) if allow_variable else length):
            current_string += lang_dict[random.randrange(dict_len)][:-1]
            current_string += ' '
        strings.append(current_string[:-1])
    return strings

# 通过随机挑选维基百科文章并从中获取句子来创建所有字符串。
def create_strings_from_wikipedia(minimum_length, count, lang):
    sentences = []

    while len(sentences) < count:
        # 取一个随机页面
        page = requests.get('https://{}.wikipedia.org/wiki/Special:Random'.format(lang))

        soup = BeautifulSoup(page.text, 'html.parser')

        for script in soup(["script", "style"]):
            script.extract()

        # 指定长度
        lines = list(filter(
            lambda s:
                len(s.split(' ')) > minimum_length
                and not "Wikipedia" in s
                and not "wikipedia" in s,
            [
                ' '.join(re.findall(r"[\w']+", s.strip()))[0:200] for s in soup.get_text().splitlines()
            ]
        ))

        # 删除最后几行
        sentences.extend(lines[0:max([1, len(lines) - 5])])

    return sentences[0:count]

# 通过从字符池中随机抽样来创建所有字符串
def create_strings_randomly(length, allow_variable, count, let, num, sym, lang):

    # 如果没有指定，使用全部
    if True not in (let, num, sym):
        let, num, sym = True, True, True

    pool = ''
    if let:
        if lang == 'cn':
            pool += ''.join([chr(i) for i in range(19968, 40908)]) # Unicode range of CHK characters
        else:
            pool += string.ascii_letters
    if num:
        pool += "0123456789"
    if sym:
        pool += "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~"

    if lang == 'cn':
        min_seq_len = 1
        max_seq_len = 2
    else:
        min_seq_len = 2
        max_seq_len = 10

    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, random.randint(1, length) if allow_variable else length):
            seq_len = random.randint(min_seq_len, max_seq_len)
            current_string += ''.join([random.choice(pool) for _ in range(seq_len)])
            current_string += ' '
        strings.append(current_string[:-1])
    return strings