from avl import AVLTree

def main():
    avl_tree = AVLTree()
    root = None
    keys = [15, 25, 55, 45, 95, 35, 5]

    for key in keys:
        root = avl_tree.insert(root, key)

    max_key = avl_tree.max(root) # 95
    min_key = avl_tree.min(root) # 5
    sum = avl_tree.sum(root) # 275

    print(f"Max key: {max_key}")
    print(f"Min key: {min_key}")
    print(f"Sum: {sum}")

if __name__ == "__main__":
    main()
