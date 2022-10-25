#include <vector>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<TreeNode*> stack;
        stack.push_back(root);
        vector<int> result;
        while (!stack.empty()) {
            TreeNode* curr = stack[stack.size()-1];
            stack.pop_back();
            if (curr != nullptr) {
                result.push_back(curr->val);
                stack.push_back(curr->right);
                stack.push_back(curr->left);
            }
        }
        return result;
    }
};