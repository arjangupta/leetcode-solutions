class Solution {
public:
    void printHashMap(const unordered_map<char, int>& u) {
        for (auto it = u.begin(); it != u.end(); ++it) {
            cout << " " << it->first << ":" << it->second;
        }
        cout << endl;
    }
    
    vector<string> commonChars(vector<string>& words) {        
        unordered_map<char, int> um;
        for (int i = 0; i < words[0].size(); ++i) {
            if (um.count(words[0][i]) > 0) {
                ++um[words[0][i]];
            } else {
                um[words[0][i]] = 1;
            }
        }
        
        unordered_map<char, int> um2;
        for (int i = 1; i < words.size(); ++i) {
            um2.clear();
            for (int j = 0; j < words[i].size(); ++j) {
                if (um.count(words[i][j])) {
                    if (um2.count(words[i][j]) == 0) {
                        um2[words[i][j]] = 1;
                    } else if (um2[words[i][j]] < um[words[i][j]]) {
                        ++um2[words[i][j]];
                    }
                }
            }
            um = um2;
        }
        
        vector<string> ans;
        for (auto it = um2.begin(); it != um2.end(); ++it) {
            for (int i = 0; i < it->second; ++i) {
                ans.push_back(string(1, it->first));                
            }
        }
        return ans;
    }
};