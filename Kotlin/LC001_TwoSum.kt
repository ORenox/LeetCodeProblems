class Solution {
    fun addBinary(a: String, b: String): String {
        
        val ans = StringBuilder()
        var carry = 0
        var i = a.length - 1
        var j = b.length - 1

        while (i >= 0 || j >= 0 || carry == 1) {
            if (i >= 0) {
                carry += a[i].digitToInt()
                i--
            }
            if (j >= 0) {
                carry += b[j].digitToInt()
                j--
            }

            ans.append(carry % 2)
            carry /= 2
        }

        return ans.reverse().toString()

    }
}
//kotlinc LC001_TwoSum.kt -include-runtime -d LC001_TwoSum.jar
//java -jar LC001_TwoSum.jar

//kotlinc LC001_TwoSum.kt -include-runtime -d run.jar && java -jar run.jar