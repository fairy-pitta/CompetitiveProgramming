
# UnionFind 

# edges 
N = int(input())
# all edges in list 
li = [i for i in range(N+1)]

# path compression 
def find(x):
    if li[x] == x:
        return x 
    else:
        # find the root recursively
        li[x] = find(li[x])
        return li[x]
# same
def same(a,b):
    # are the roots same? 
    return find[a] == find[b]

def unite(a,b):
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root:
        return 0
    li[a] = b_root




