#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string max_prefix = "";
        string all_prefix = "";
        string current_prefix = "";
        for (int i = 0; i < strs.size(); i++)
        {
            for (int j = 1; j < strs.size(); j++)
            {
                if (i == j)
                {
                    continue;
                }

                for (int k = 0; k < strs.size(); k++)
                {
                    int shorter_str_len = (strs[i].size() < strs[j].size()) ? strs[i].size() : strs[j].size();
                    if (strs[i].substr(0, shorter_str_len - k) == strs[j].substr(0, shorter_str_len - k))
                    {
                        current_prefix = strs[i].substr(0, shorter_str_len - k);
                    }
                    
                    if (current_prefix.size() > max_prefix.size())
                    {
                        max_prefix = current_prefix;
                    }
                }
            }
        }
        return max_prefix;
    }
};