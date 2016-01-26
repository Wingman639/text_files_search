# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def search(text, key):
    candidates = []
    lines = text.splitlines()
    for line in lines:
        s = line_similarity_of_key(line, key)
        if s > (len(key.split()) / 2):
            candidates.append((s, line))
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates


def line_similarity_of_key(line, key):
    key_words = key.lower().split()
    easy_line = line.lower()
    i = 0
    s_sum = 0
    for word in key_words:
        s, new_i = line_similarity_of_word(line=easy_line, start=i, word=word)
        if s:
            s_sum += s
        if new_i >= 0:
            i = new_i
    return s_sum


def line_similarity_of_word(line, start, word):
    i = line.find(word, start)
    similarity = 1 if i >= 0 else 0
    return similarity, i


def result_str(result):
    return u'\n'.join([str(x[0]) + ':' + x[1] for x in result])


if __name__ == '__main__':

    import unittest

    line = 'this is a line of text which shall match key in search'
    text = '''
This is a test text for search.
Words order is important. But case insensitive.
I create this search is for specified purposes.
'''
    search_result = [(3, 'This is a test text for search.'),
                     (2, 'I create this search is for specified purposes.'),
                     (1, 'Words order is important. But case insensitive.')]

    class FunctionTestCase(unittest.TestCase):
        def test_line_similarity_of_word(self):
            result = line_similarity_of_word(line, 0, 'of')
            expect = (1, 15)
            self.assertEqual(expect, result)

        def test_line_similarity_of_key(self):
            result = line_similarity_of_key(line, 'line of search')
            expect = 3
            self.assertEqual(expect, result)

        def test_search(self):
            result = search(text, 'is for search')
            expect = search_result
            self.assertEqual(expect, result)

        def test_result_str(self):
            result = result_str(search_result)
            expect = '''This is a test text for search.
I create this search is for specified purposes.
Words order is important. But case insensitive.'''
            self.assertEqual(expect, result)

    unittest.main()
