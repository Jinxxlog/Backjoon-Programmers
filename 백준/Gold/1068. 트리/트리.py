def search(tree, root, rmv):
    if root == rmv:
        return 0
    
    if root not in tree or not tree[root]:
        return 1
    
    cnt = 0
    for i in tree[root]:
        if i != rmv:
            cnt += search(tree, i, rmv)

    return cnt if cnt != 0 else 1
    
K = int(input())
node = list(map(int, input().split()))
rmv = int(input())

tree = {}
root = -1

for i, par in enumerate(node):
    if par == -1:
        root = i
    else:
        if par not in tree:
            tree[par] = []
        tree[par].append(i)

res = search(tree, root, rmv)
print(res)