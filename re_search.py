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


def result_str(result):
    output_count = len(result)
    output_list = []
    for i in range(output_count):
        output_list.append(result[i])
    return u'\n'.join([item_str(x) for x in output_list]) + u'\n'


def item_str(x):
    return ''.join([str(x['line_num']) , ':', x['line']])

if __name__ == '__main__':
	def test():
		print search('abcde\nfghijk\ncba', 'a\w?')
		print search('TASK ret_status := /*IUR_FRLC_ENA_HSPA_DIS_EC*/ 2888;', ':=[ ]*(/\*.*\*/)[ ]*\d{2,5}')

	test()