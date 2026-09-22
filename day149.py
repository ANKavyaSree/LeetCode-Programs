# day149.py

def solve(nums, k, queries):
    n = len(nums)
    prod = [0] * (4 * n)
    cnt = [[0] * k for _ in range(4 * n)]

    def merge(lp, lc, rp, rc):
        p = (lp * rp) % k
        c = lc[:]
        for r in range(k):
            c[(lp * r) % k] += rc[r]
        return p, c

    def build(node, l, r):
        if l == r:
            v = nums[l] % k
            prod[node] = v
            cnt[node][v] = 1
            return
        mid = (l + r) // 2
        build(node * 2, l, mid)
        build(node * 2 + 1, mid + 1, r)
        prod[node], cnt[node] = merge(prod[node * 2], cnt[node * 2],
                                      prod[node * 2 + 1], cnt[node * 2 + 1])

    def update(node, l, r, idx, value):
        if l == r:
            v = value % k
            prod[node] = v
            cnt[node] = [0] * k
            cnt[node][v] = 1
            return
        mid = (l + r) // 2
        if idx <= mid:
            update(node * 2, l, mid, idx, value)
        else:
            update(node * 2 + 1, mid + 1, r, idx, value)
        prod[node], cnt[node] = merge(prod[node * 2], cnt[node * 2],
                                      prod[node * 2 + 1], cnt[node * 2 + 1])

    def query(node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return prod[node], cnt[node][:]
        mid = (l + r) // 2
        if qr <= mid:
            return query(node * 2, l, mid, ql, qr)
        if ql > mid:
            return query(node * 2 + 1, mid + 1, r, ql, qr)
        a = query(node * 2, l, mid, ql, qr)
        b = query(node * 2 + 1, mid + 1, r, ql, qr)
        return merge(a[0], a[1], b[0], b[1])

    build(1, 0, n - 1)
    result = []
    for idx, value, start, x in queries:
        update(1, 0, n - 1, idx, value)
        _, counts = query(1, 0, n - 1, start, n - 1)
        result.append(counts[x])
    return result


def main():
    nums = list(map(int, input("Enter nums: ").split()))
    k = int(input("Enter k: "))
    q = int(input("Enter number of queries: "))
    queries = []
    print("Enter each query as: index value start x")
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    print("Output:", solve(nums, k, queries))


if __name__ == "__main__":
    main()
