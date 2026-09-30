#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

class BIT {
private:
    vector<int> tree;
    int size;

public:
    // Constructor
    BIT(int n) : size(n), tree(n + 1, 0) {}

    // Add a value to the tree
    void add(int i, int x) {
        while (i <= size) {
            tree[i] += x;
            i += i & -i; // Calculating the least significant bit
        }
    }

    // Compute the sum from index 0 to i
    int sum(int i) {
        int total = 0;
        while (i > 0) {
            total += tree[i];
            i -= i & -i; // Calculating the least significant bit
        }
        return total;
    }
};

int InversionNumberByBIT(const vector<int>& A) {
    int ans = 0;
    BIT bit(A.size());
    for (int i = 0; i < A.size(); ++i) {
        ans += i - bit.sum(A[i]);
        bit.add(A[i], 1); // Mark the position
    }
    return ans;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int cnt = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (A[i] > A[j]) {
                cnt++;
            }
        }
    }

    int num = InversionNumberByBIT(A);
    long long ans = 0;
    for (int i = 0; i < K; ++i) {
        ans += num;
        ans += static_cast<long long>(i) * cnt;
        ans %= MOD;
    }

    cout << ans << endl;

    return 0;
}
