from hashlib import sha256


def hello():
    print("H")


def build_merkle_tree(args):

    for a in args:
        print(a)
    root = dict()
    root["left"] = None

    return root


if __name__ == '__main__':

    terminal_on = True
    current_merkle_tree = None
    mode = ' '
    while terminal_on:

        mode = int(input())
        if mode is 1:
            print('1')
            current_merkle_tree = build_merkle_tree(list(map(str, input().split())))
        elif mode is 2:
            print('2')
        elif mode is 3:
            print('3')
        elif mode is 4:
            print('4')
        else:
            print('5')
            terminal_on = False
