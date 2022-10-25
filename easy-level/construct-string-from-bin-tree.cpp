/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    string tree2str(TreeNode* root) {
        string ans = "";
        if (root == nullptr) {
            return ans;
        }
        ans = to_string(root->val) + "(" + tree2str(root->left) + ")(" + tree2str(root->right) + ")";
        for (int i = 0; i < ans.size(); ++i) {
            if (ans.substr(i, 4) == "()()") {
                ans.erase(i, 4);
            } else if (ans.substr(i,3) == "())") {
                ans.erase(i,2);
            } else if (i == ans.size() - 2 && ans.substr(i,2) == "()") {
                ans.erase(i,2);
            }
        }
        return ans;
    }
};