// https://leetcode.com/problems/generate-parentheses/


// --------- FLAWED APPROACH - DOES NOT GIVE THE CORRECT SOLUTION -----------


class Solution {
public:
    vector<string> generateParenthesis(int n) {
        unordered_set<string> string_set;
        for (int open = n; open >= 1; open--) {
            for (int close = 1; close <= n; close++) {
                if (open == n && close < n || open == 1 && close > 1 || close > open) {
                    continue;
                }
                string parens_list = "";
                int total_open_listed = 0;
                int total_close_listed = 0;
                while (parens_list.length() < 2*n) {
                    int curr_open_listed = 0;
                    int curr_close_listed = 0;
                    while (curr_open_listed < open && total_open_listed < n) {
                        parens_list += '(';
                        ++curr_open_listed;
                        ++total_open_listed;
                    }
                    while (curr_close_listed < close && total_close_listed < n && total_close_listed <= total_open_listed) {
                        parens_list += ')';
                        ++curr_close_listed;
                        ++total_close_listed;
                    } 
                }
                string_set.insert(parens_list);
                string reversed_parens_list = "";
                for (int i = 0; i < parens_list.length(); ++i) {
                    const char c = parens_list[parens_list.length() - 1 - i];
                    reversed_parens_list += (c == '(') ? (')') : ('(');
                }
                string_set.insert(reversed_parens_list);
            }
        }
        vector<string> parens_list_vec;
        for (const string parens_str: string_set) {
            parens_list_vec.push_back(parens_str);
        }
        return parens_list_vec;
    }
};