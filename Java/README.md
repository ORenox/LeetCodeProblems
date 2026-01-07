# Código Java

```java
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder ans = new StringBuilder();
        int carry = 0;
        int i = a.length() - 1;
        int j = b.length() - 1;

        while (i >= 0 || j >= 0 || carry == 1) {
            if (i >= 0) {
                carry += Integer.parseInt(String.valueOf(a.charAt(i)));;
                i--;
            }
            if (j >= 0) {
                carry += Integer.parseInt(String.valueOf(b.charAt(j)));
                j--;
            }

            ans.append(carry % 2);
            carry /= 2;
        }

        return ans.reverse().toString();
    }
}
