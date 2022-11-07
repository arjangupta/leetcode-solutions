// https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits == "") {
            return {};
        }
        unordered_map<int,vector<char>> um;
        um[2] = {'a', 'b', 'c'};
        um[3] = {'d', 'e', 'f'};
        um[4] = {'g', 'h', 'i'};
        um[5] = {'j', 'k', 'l'};
        um[6] = {'m', 'n', 'o'};
        um[7] = {'p', 'q', 'r', 's'};
        um[8] = {'t', 'u', 'v'};
        um[9] = {'w', 'x', 'y', 'z'};

        vector<string> ans = {""};
        for (char c: digits) {
            int num = c - '0';
            vector<string> new_ans = {};
            for (char mapped_char: um[num]) {
                for (string ans_str: ans) {
                    new_ans.push_back(ans_str + mapped_char);
                }
            }
            ans = new_ans;
        }
        return ans;
    }
};