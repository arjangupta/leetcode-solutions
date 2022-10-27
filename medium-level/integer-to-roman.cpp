#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        int tf = 10;
        while (tf < num) {
            tf *= 10;
        }
        tf /= 10;
        
        string ans = "";
        unordered_map<int,string> um = 
        {{1,"I"},{5,"V"},{10,"X"},{50,"L"},{100,"C"},{500,"D"},{1000,"M"},{4,"IV"},{9,"IX"},{40,"XL"},{90,"XC"},{400,"CD"},{900,"CM"}};
        int curr = 0;
        while (tf != 0) {
            curr = num/tf;
            if (um.count(curr * tf)) {
                ans += um[curr * tf];
            } else {
                int singles = curr;
                if (curr > 5) {
                    ans += um[tf*5];
                    singles = curr - 5;
                }
                for (int i = 0; i < singles; ++i) {
                    ans += um[tf];
                }
            }
            num = num - (curr*tf);
            if (num == 0) {
                tf = 0;
            } else {
                tf /= 10;
            }
        }
        return ans;
    }
};