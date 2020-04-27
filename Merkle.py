from hashlib import sha256


# Build root from two merged nodes, and again recursively, every iteration construct single layer
def recursive_merkle_build(args_dict):
    # If got to the root, single node, return him
    if len(args_dict) is 1:

        # Because the args passed as list, extract him (return dict)
        return args_dict[0]
    else:

        # Node represented in dict, value = hash string, left, right = child trees
        # Chain left and right nodes, apply sha256, the loop work for pairs ((0=left,1=right),(2=left,3=right)...)
        return recursive_merkle_build(
            [dict(value=sha256((left['value'] + (right['value'])).encode()).hexdigest(), left=left, right=right)
             for left, right in zip(args_dict[0::2], args_dict[1::2])])


# Bottom -> Top approach , first construct the leafs then the internal nodes
def build_merkle_tree(args):
    leafs = [dict(value=arg) for arg in args]
    return recursive_merkle_build(leafs)


if __name__ == '__main__':

    terminal_on = True
    current_merkle_tree = None
    user_input = ' '
    try:

        while terminal_on:

            user_input = list(map(str, input().split()))
            mode = user_input[0]
            if mode is '1':
                current_merkle_tree = build_merkle_tree(user_input[1:])
                print(current_merkle_tree["value"])
            elif mode is 2:
                print('2')
            elif mode is 3:
                print('3')
            elif mode is 4:
                print('4')
            else:
                print('5')
                terminal_on = False
    except ValueError:
        exit(0)
