# Código en C++

```cpp
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string ans = "";
        int carry = 0;
        int i = a.size() - 1;
        int j = b.size() - 1;

        while (i >= 0 || j >= 0 || carry == 1) {
            if (i >= 0) {
                carry += stoi(string(1, a[i]));
                i--;
            }
            if (j >= 0) {
                carry += stoi(string(1, b[j]));
                j--;
            }

            ans.push_back((carry % 2) + '0');
            carry /= 2;
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
