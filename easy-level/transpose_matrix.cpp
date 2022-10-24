class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        vector<vector<int>> transpose;
        transpose.resize(matrix[0].size());
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[0].size(); ++j) {
                transpose[j].push_back(matrix[i][j]);
            }
        }
        return transpose;
    }
};