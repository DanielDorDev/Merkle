from hashlib import sha256



# Return the proof inclusion path, pass target index, current root and container for path
def check_proof(target_value, root, proof_path):

    print("H")

# Check if the index is right to the root, if so return true
def is_index_to_right(node_index, root):
    if node_index >= root['count'] - 1:
        return True
    else:
        return False


# Return the proof inclusion path, pass target index, current root and container for path
def get_proof(target_idx, root, proof_path):

    # Got to the target node = leaf
    if root['count'] is 1:
        return proof_path
    elif is_index_to_right(target_idx, root):
        return get_proof(target_idx - root['left']['count'], root['right'], proof_path + [root['left']['value'], 'l'])
    else:
        return get_proof(target_idx, root['left'], proof_path + [root['right']['value'], 'r'])


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
            [dict(value=sha256((left['value'] + (right['value'])).encode()).hexdigest(), left=left, right=right,
                  count=(right['count'] + left['count'])) for left, right in zip(args_dict[0::2], args_dict[1::2])])


# Bottom -> Top approach , first construct the leafs then the internal nodes
def build_merkle_tree(args):
    leafs = [dict(value=arg, count=1) for arg in args]
    return recursive_merkle_build(leafs)


if __name__ == '__main__':

    terminal_on = True
    current_merkle_tree = None
    user_input = ' '
    try:

        while terminal_on:

            user_input = list(map(str, input().split()))
            mode = int(user_input[0])
            if mode is 1:
                current_merkle_tree = build_merkle_tree(user_input[1:])
                print(current_merkle_tree["value"])

            elif mode is 2:
                path = get_proof(int(user_input[1]), current_merkle_tree, list())
                print(' '.join(path[::-1]))
            elif mode is 3:
                print('op: 3')
            elif mode is 4:
                print('op: 4')
            else:
                print('op: 5')
                terminal_on = False
    except ValueError:
        exit(0)
