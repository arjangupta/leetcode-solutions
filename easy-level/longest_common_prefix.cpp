#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs[0];
        int s_i = 0;
        int p_i = prefix.size();
        bool keep_going = true;
        while (keep_going)
        {
            if (prefix.substr(0, p_i) != strs[s_i].substr(0, p_i))
            {
                prefix = prefix.substr(0, --p_i);
            }
            else
            {
                if (++s_i == strs.size())
                {
                    keep_going = false;
                }
            }
        }
        return prefix;
    }
};