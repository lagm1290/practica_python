print('Ingrese primer conjunto')
a = set(input())
print('ingrese segundo conjunto')
b = set(input())
import pdb; pdb.set_trace()
result='False'
if len(a) == len(b):
    if not a.difference(b):
        result = 'True'

print(result)


if __name__ == '__main__':
    pass
