// https://leetcode.com/problems/merge-k-sorted-lists/description/
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<int, std::vector<int>, std::greater<int>> heap;
        for (ListNode* list: lists) {
            ListNode* curr = list;
            while (curr != nullptr) {
                heap.push(curr->val);
                curr = curr->next;
            }
        }
        ListNode* builder = nullptr;
        ListNode* ans = nullptr;
        if (!heap.empty()) {
            builder = new ListNode(heap.top(), nullptr);
            heap.pop();
            ans = builder;
        }
        while (!heap.empty()) {
            builder->next = new ListNode(heap.top(), nullptr);
            heap.pop();
            builder = builder->next;
        }
        return ans;
    }
};