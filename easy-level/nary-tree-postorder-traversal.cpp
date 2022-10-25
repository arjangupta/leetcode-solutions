#include <iostream>
#include <vector>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> ans;
        if (root == nullptr) {
            return ans;
        }
        vector<vector<int>> subtrees;
        for (Node* child: root->children) {
            subtrees.push_back( postorder(child) );
        }
        for (vector<int> subtree: subtrees) {
            for (int i: subtree) {
                ans.push_back(i);
            }
        }
        ans.push_back(root->val);
        return ans;
    }
};