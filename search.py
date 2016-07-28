# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def search(text, key, more_line=False):
    if more_line:
        return fetch_previous_and_current_line_search(text, key)
    else:
        return only_fetch_current_line_search(text, key)


def fetch_previous_and_current_line_search(text, key):
    print 'fetch_previous_and_current_line_search'
    candidates = []
    lines = text.splitlines()
    for i in range(len(lines)):
        line = lines[i]
        s = line_similarity_of_key(line, key)
        if s > (len(key.split()) / 2):
            better_line = line
            if i > 1:
                better_line = lines[i-1] + '\n' + line
            candidates.append({'s': s, 'line': better_line, 'line_num': i+1})
    if not candidates:
        return [], 0
    candidates.sort(key=lambda x: x['s'], reverse=True)
    return candidates, candidates[0]['s']

def only_fetch_current_line_search(text, key):
    candidates = []
    i = 0
    lines = text.splitlines()
    for line in lines:
        i += 1
        s = line_similarity_of_key(line, key)
        if s > (len(key.split()) / 2):
            candidates.append({'s': s, 'line': line, 'line_num': i})
    if not candidates:
        return [], 0
    candidates.sort(key=lambda x: x['s'], reverse=True)
    return candidates, candidates[0]['s']

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
    i = 0
    try:
        i = line.find(word, start)
    except:
        print line
        return 0, 0
    similarity = 1 if i >= 0 else 0
    return similarity, i


def result_str(result):
    output_count = min(3, len(result))
    output_list = []
    for i in range(output_count):
        output_list.append(result[i])
    return u'\n'.join([item_str(x) for x in output_list]) + u'\n'



def item_str(x):
    return ''.join([str(x['s']), ': (', str(x['line_num']) , ')', x['line']])

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
