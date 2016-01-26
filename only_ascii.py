
file_path = './test_files/fc_t.sdt'
new_file_path = './test_files/ascii_fc_t.sdt'

new_lines = []

with open(file_path, 'r') as f:
    text = f.read()
    lines = text.splitlines()
    for line in lines:
        try:
            line.find('a')
            new_lines.append(line)
        except Exception, e:
            print e
            pass

text = '\n'.join(new_lines)

with open(new_file_path, 'w') as f:
    f.write(text)
