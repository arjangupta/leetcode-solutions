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

struct TreeNodeTraversal {
    bool visited;
    TreeNode* node;
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        vector<TreeNodeTraversal> stack;
        stack.push_back({false, root});
        while (!stack.empty()) {
            TreeNodeTraversal curr = stack[stack.size()-1];
            stack.pop_back();
            if (curr.node != nullptr) {
                if (curr.visited) {
                    result.push_back(curr.node->val);
                }
                else {
                    curr.visited = true;
                    stack.push_back(curr);
                    stack.push_back({false, curr.node->right});
                    stack.push_back({false, curr.node->left});
                }
            }
        }
        return result;
    }
};