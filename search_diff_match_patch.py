# -*- coding: utf-8 -*-

from diff_match_patch import diff_match_patch


def search(key, text, from_position=0):
    diff = diff_match_patch()
    start = diff.match_main(text, key, from_position)
    if start < 0: return
    better_start = start
    eol_left = text.rfind('\n', 0, start)
    if eol_left >= 0:
        better_start = eol_left + 1;
    end = text.find('\n', start+1)
    if start < end:
        return text[better_start:end]


if __name__ == '__main__':
    key = ' 16 kbit/s Return Channel DCH Data Rate'
    file_path = './test_files/feature_name.txt'

    def test_search():
        with open(file_path, 'r') as f:
            text = f.read()
            print search(key, text)



    def print_list(in_list):
        for line in in_list:
            print line


    def test_diff_match_patch():
        diff = diff_match_patch()
        with open(file_path, 'r') as f:
            text = f.read()
            #print text
            result = diff.match_main(text, key, 0)
            print result

    def test_diff_main():
        diff = diff_match_patch()

        with open(file_path, 'r') as f:
            text = f.read()
            lines = text.splitlines()
            i = 0
            for line in lines:
                print line
                print diff.diff_main(line, key)
                i += 1
                if i > 4: return


    def test():
        #test_diff_match_patch()
        #test_search()
        test_diff_main()

    test()
