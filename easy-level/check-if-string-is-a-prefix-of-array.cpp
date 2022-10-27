class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string concat = "";
        for (string word: words) {
            concat += word;
            if (concat == s) {
                return true;
            }
        }
        return false;
     }
};