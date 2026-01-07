# Código JS
```js
function addBinary(a, b) {
    let ans = [];
    let carry = 0;
    let i = a.length - 1;
    let j = b.length - 1;

    while (i >= 0 || j >= 0 || carry === 1) {
        if (i >= 0) {
            carry += Number(a[i]);
            i--;
        }
        if (j >= 0) {
            carry += Number(a[i]);
            j--;
        }

        ans.push(carry % 2);
        carry = Math.floor(carry / 2);
    }

    return ans.reverse().join('');
}
