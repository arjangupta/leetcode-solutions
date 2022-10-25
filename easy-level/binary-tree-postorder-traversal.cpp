#include <vector>
#include <iostream>
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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        vector<TreeNode*> stack;
        stack.push_back(root);
        while (!stack.empty()) {
            TreeNode* curr = stack[stack.size()-1];
            stack.pop_back();
            if (curr != nullptr) {
                cout << curr->val << " ";
                if (curr->left == nullptr && curr->right == nullptr) {
                    result.push_back(curr->val);
                }
                else {
                    stack.push_back(curr);
                    stack.push_back(curr->right);
                    stack.push_back(curr->left);
                }
            }
        }
        return result;
    }
};