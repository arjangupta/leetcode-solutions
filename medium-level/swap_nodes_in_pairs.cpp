// https://leetcode.com/problems/swap-nodes-in-pairs/description/

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
    ListNode* swapPairs(ListNode* head) {
        ListNode* first = head;
        if (first == nullptr) {
            return head;
        }
        ListNode* second = first->next;
        if (second == nullptr) {
            return head;
        }
        head = second;
        while (true) {
            ListNode* pair_head = first;
            // Swap
            first->next = second->next;
            second->next = first;
            // Advance
            if (first->next != nullptr && first->next->next != nullptr) {
                first = first->next;
                second = first->next;
                pair_head->next = second;
            }
            else {
                break;
            }
        };
        return head;
    }
};