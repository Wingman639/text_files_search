# -*- coding:UTF-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

SIMILARITY = 0    #I have no idea how to define suitable similarity in re search case yet

def search(text, patternStr):
	candidates = []
	pattern = re.compile(patternStr)
	i = 0
	for line in text.splitlines():
		i += 1
		match_str = _match_pattern(pattern, line)
		if match_str:
			candidates.append({'s': SIMILARITY, 'line': line, 'line_num': i})
	return candidates, SIMILARITY


def _match_pattern(pattern, text):
    match = pattern.search(text)
    if match:
        return match.group()

if __name__ == '__main__':
	def test():
		print search('abcde\nfghijk\ncba', 'a\w?')
	test()