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
        int num_valleys = ceil(float(s.length() - numRows)/float(p));
        int rc = 2*num_peaks - 1;
        std::cout << "sl, num_peaks, p, rc: " << s.length() << " " << num_peaks << " " << p << " " << rc << std::endl;
        for (int i = 0; i < s.length(); ++i)
        {
            if (i < num_peaks)
            {
                zigzag_result[i] = s[i*p];
            }
            else if (i < (s.length() - num_valleys))
            {
                int row = (i - num_peaks)/rc + 1;
                int valley_len = p - 2*row;
                zigzag_result[i] = s[(i - num_peaks)/rc + 1];
            }
            else
            {
                zigzag_result[i] = s[(numRows - 1) + p*((i - s.length() + num_valleys)%(num_valleys))];
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