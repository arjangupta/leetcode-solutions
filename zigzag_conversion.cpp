#include <string>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        string zigzag_result = s;
        int p = 2*numRows - 2;
        int num_peaks = ceil(float(s.length())/float(p));
        int rc = 2*num_peaks - 1;
        std::cout << "sl, num_peaks, p, rc: " << s.length() << " " << num_peaks << " " << p << " " << rc << std::endl;
        for (int i = 0; i < s.length(); ++i)
        {
            if (i < num_peaks)
            {
                zigzag_result[i] = s[i*p];
            }
            else
            {
                zigzag_result[i] = s[(i - num_peaks)/rc + ((i - num_peaks)%rc) + 1];
            }
        }
        return zigzag_result;
    }
};

// # Exceeds the time limit
// # class Solution:
// #     def convert(self, s: str, numRows: int) -> str:
// #         result: str = ""
// #         for j in range(numRows):
// #             for i in range(len(s)):
// #                 if 2*numRows - 2 == 0 or ((i) % (2*numRows - 2)) == j or (i % (2*numRows - 2) == (2*numRows - 2 - j)):
// #                     result += s[i]
// #         return result