#include <unordered_map>

using namespace std;

class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_map<char,int> alphabet_hash_table;
        for (int i = 'a'; i <= 'z'; i++) {
            alphabet_hash_table.insert(make_pair((char)i, 0));
        }
        for (int i = 0; i < sentence.length(); i++) {
            ++alphabet_hash_table[sentence[i]];
        }
        unordered_map<char,int>::iterator it;
        for (it = alphabet_hash_table.begin(); it != alphabet_hash_table.end(); it++) {
            if (it->second == 0)
            {
                return false;
            }
        }
        return true;
    }
};