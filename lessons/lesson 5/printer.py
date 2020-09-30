from pathlib import Path
import sys


path = Path(sys.argv[0])
path.resolve()
with open(path, 'r') as f:
    print(f.read())
    f.seek(0)
    comments = 0
    functions = 0
    for line in f:
        if line != '\n':
            check = line.strip().split()
            if check[0] == 'def':
                functions += 1
            elif check[0] == '#':
                comments += 1
            elif '#' in check[0] and len(check[0]) > 1:
                if check[0][0] == '#':
                    comments += 1
print('*' * 50)
print(f'Comments: {comments}')
print(f'Functions: {functions}')