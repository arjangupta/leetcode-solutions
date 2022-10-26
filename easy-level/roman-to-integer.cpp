#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int> um = {{'I',1},{'V',5},{'X',10},{'L', 50},{'C',100},{'D',500},{'M',1000}};
        unordered_map<string,int> um2 = {{"IV",4},{"IX",9},{"XL",40},{"XC",90},{"CD",400},{"CM",900}};
        int total = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (i+1 < s.size() && um2.count(s.substr(i,2))) {
                total += um2[s.substr(i,2)];
                ++i;
            } else {
                total += um[s[i]];
            }
        }
        return total;
    }
};