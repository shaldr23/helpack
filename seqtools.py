# Расстояние Левенштейна
from difflib import SequenceMatcher
import re


def similarity(a, b, skip_pattern=None):
    """
    Функция, рассчитывающая расстояние Левенштейна
    """
    if skip_pattern:
        a = re.sub(skip_pattern, '', a)
        b = re.sub(skip_pattern, '', b)
    s = SequenceMatcher(None, a, b)
    return s.ratio()


if __name__ == '__main__':
    word1 = 'са ша'
    word2 = 'саша    1234'
    result = similarity(word1, word2, r'[ \d]')
    print(f'word1: {word1}\n'
          f'word2: {word2}\n'
          f"similarity: {result}")
