from hashlib import sha256


def brute_find(complexity, root):
    print("H")


# Merge two string and apply hash256 on the result, the chain order decided by 'side' input
def merge_hash_by_side(side, start_value, path_value):
    if side == 'r':
        return sha256((start_value + path_value).encode()).hexdigest()
    else:
        return sha256((path_value + start_value).encode()).hexdigest()


# Check for given leaf, root, and path, if proof of inclusion is validate
def check_proof(leaf_value, root_value, check_path):

    # Return bool from comparison between constructed root(from path) and given root
    if len(check_path) == 0:
        return leaf_value == root_value
    else:
        # Merge and hash the first 2 values by the instruction (form the path)
        # Send recursively the merged value, the given target root, and rest of the path
        return check_proof(merge_hash_by_side(check_path[0], leaf_value, check_path[1]), root_value,
                           check_path[2:])


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

    # If index to the right
    elif is_index_to_right(target_idx, root):
        # Send recursively (target index subtracted left tree size (keep relative rule), relative root,
        # Append inclusion value(and which side) to the path container
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
            if mode is 1:  # Construct merkle tree
                current_merkle_tree = build_merkle_tree(user_input[1:])
                print(current_merkle_tree["value"])

            elif mode is 2: # Create proof of inclusion
                path = get_proof(int(user_input[1]), current_merkle_tree, list())
                print(' '.join(path[::-1]))
            elif mode is 3: # Check proof of inclusion
                print(check_proof(user_input[1], user_input[2], user_input[3:]))
            elif mode is 4: # Find nonce with brute force
                print('op: 4')
            else:   # Exit
                print('op: 5')
                terminal_on = False
    except ValueError:
        exit(0)
