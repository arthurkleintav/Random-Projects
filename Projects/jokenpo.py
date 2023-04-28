def write(msg):
    size = len(msg) + 4
    print('~' * len(msg))
    print(f'  {msg}  ')
    print('~' * len(msg))