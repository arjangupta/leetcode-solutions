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
        vector<int> result;
        while (root != nullptr || !stack.empty()) {
            stack.push_back(root);
            result.push_back(root->val);
            root = root->left;
            if (!root) {
                root = root->right;
                stack.pop_back();
                root = stack[stack.size() - 1]->right;
            }
        }
        return result;
    }
};