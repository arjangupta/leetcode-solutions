/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        vector<int> stack;
        while (curr != nullptr) {
            stack.push_back(curr->val);
            curr = curr->next;
        }
        curr = head;
        while (curr != nullptr) {
            curr->val = stack[stack.size()-1];
            stack.pop_back();
            curr = curr->next;
        }
        return head;
    }
};