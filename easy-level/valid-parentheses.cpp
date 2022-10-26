#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, int> paren = {{')', '('}, {'}', '{'}, {']', '['}};
        vector<char> stack;
        for (char c: s) {
            if (stack.size() == 0) {
              stack.push_back(c);
            } else if (paren.count(c) && stack[stack.size()-1] != paren[c]) {
                return false;
            } else if (!paren.count(c)) {
                stack.push_back(c);
            } else {
                stack.pop_back();
            }
        }
        if (stack.size() == 0) {
            return true;
        }
        return false;
    }
};