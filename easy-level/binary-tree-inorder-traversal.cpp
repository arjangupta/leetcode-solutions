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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (!root) {
            return ans;
        }
        vector<int> left = inorderTraversal(root->left);
        vector<int> right = inorderTraversal(root->right);
        ans.reserve(left.size() + 1 + right.size());
        for (int e: left) {
            ans.push_back(e);
        }
        ans.push_back(root->val);
        for (int e: right) {
            ans.push_back(e);
        }
        return ans;
    }
};