import sys
import re

environments = {"document", "itemize", "enumerate", "minted"}


def process_file(filename: str) -> str:
    content = []
    with open(filename, "rt", encoding="utf-8") as rf:
        line = rf.readline()
        while "document" not in line:
            line = rf.readline()
        line = rf.readline()
        while line:
            found = False
            for item in environments:
                if item in line:
                    found = True
                    break
            if not found:
                content.append(line)
            line = rf.readline()
        content = "§".join(content)
    content = content.replace(r'\\', '')
    content = content.replace(r'{', '')
    content = content.replace(r'}', '')
    content = content.replace(r'\item', '')
    return content


def get_file(filename: str) -> str:
    with open(filename, "rt", encoding="utf-8") as rf:
        _content = rf.readlines()
    _content = "§".join(_content)
    return _content




def replace_pythoninline(text: str) -> str:
    pattern = r"\\mintinline{python}{[^}]*}"

    lpat = len(r"\\mintinline{python}{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + "`#!python " + text[a + lpat - 1:b - 1] + "`" + text[b:]
        match_result = re.search(pattern, text)
    return text


def replace_subsection(text: str) -> str:
    pattern = r"\\subsection{[^}]*}"
    lpat = len(r"\\subsection{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + "### " + text[a + lpat - 1:b - 1] + text[b:]
        match_result = re.search(pattern, text)
    return text


def replace_section(text: str) -> str:
    pattern = r"\\section{[^}]*}"
    lpat = len(r"\\section{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + "## " + text[a + lpat - 1:b - 1] + text[b:]
        match_result = re.search(pattern, text)
    return text


def replace_textbf(text: str) -> str:
    pattern = r"\\textbf{[^}]*}"

    lpat = len(r"\\textbf{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + "**" + text[a + lpat - 1:b - 1] + "**" + text[b:]
        match_result = re.search(pattern, text)
    return text

def replace_textsc(text: str) -> str:
    pattern = r"\\textsc{[^}]*}"

    lpat = len(r"\\textsc{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + text[a + lpat - 1:b - 1] + text[b:]
        match_result = re.search(pattern, text)
    return text

def replace_texttt(text: str) -> str:
    pattern = r"\\texttt{[^}]*}"

    lpat = len(r"\\texttt{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + "`" + text[a + lpat - 1:b - 1] + "`" + text[b:]
        match_result = re.search(pattern, text)
    return text


def replace_textit(text: str) -> str:
    pattern = r"\\textit{[^}]*}"

    lpat = len(r"\\textit{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + "*" + text[a + lpat - 1:b - 1] + "*" + text[b:]
        match_result = re.search(pattern, text)
    return text

def replace_pythonfile(text:str)->str:

    pattern = r"\\pythonfile{scripts/[^}]*}"

    lpat = len(r"\\pythonfile{scripts/")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a] + "{{py('" + text[a + lpat - 1:b - 1] + "')}}" + text[b:]
        match_result = re.search(pattern, text)
    return text
def replace_np(text: str) -> str:
    pattern = r"\\np{[^}]*}"

    lpat = len(r"\\np{")
    match_result = re.search(pattern, text)
    while match_result:
        a, b = match_result.span()
        text = text[:a]  + text[a + lpat - 1:b - 1] + text[b:]
        match_result = re.search(pattern, text)
    return text


def replace_minted(text):
    text = text.replace(r"\begin{minted}{python}", "```python")
    text = text.replace(r"\end{minted}", "```")
    return text

def replace_pythoncode(text):
    text = text.replace(r"\begin{pyc}", "```python")
    text = text.replace(r"\end{pyc}", "```")
    return text

def finish(text):
    _content = text.split("§")
    content2 = []
    found = False
    for line in _content:
        if r"\begin{document}" in line:
            found = True
        if found and not (r"\begin" in line or r"\end" in line):
            content2.append(line)
    _content="".join(content2)
    _content = _content.replace("§", "")
    _content = _content.replace(r"\_", "_")

    _content = _content.replace(r"\item", "- ")
    _content = _content.replace("\\\\", "")
    _content = _content.replace("\«", "«")
    _content = _content.replace("\»", "»")
    _content = _content.replace("\\'E", "É")
    _content = _content.replace("\\scriptsize", "")
    _content = _content.replace("\\normalsize", "")
    return _content

def tex2md(filename:str)->None:
    content = get_file(filename)
    content = replace_subsection(content)
    content = replace_section(content)
    content = replace_section(content)
    content = replace_textit(content)
    content = replace_textbf(content)
    content = replace_texttt(content)
    content = replace_pythoninline(content)
    content = replace_minted(content)
    content = replace_pythoncode(content)
    content = replace_np(content)
    content = replace_textsc(content)
    content = replace_pythonfile(content)
    content = finish(content)
    with open(filename[:-3]+'md','wt',encoding='utf8')  as wf:
        wf.write(content)


tex2md(sys.argv[1])