// 148. Sort List (Leetcode)

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
    ListNode* merge(ListNode* node1, ListNode* node2){
        ListNode* dummy = new ListNode(-1);
        ListNode* curr = dummy;
        while(node1 != nullptr && node2 != nullptr){
            if(node1 -> val < node2 -> val)
            {
             curr -> next = node1;
             node1 = node1 -> next;
            }    
            else {
                curr -> next= node2;
                node2 = node2 -> next;
            }
            curr = curr -> next;
        }
        if(node1 != nullptr) curr -> next = node1;
        if(node2 != nullptr) curr -> next = node2;
        return dummy -> next;
    }
    ListNode* middle(ListNode* head){
         if (!head || !head->next) return head;
        ListNode* slow = head;
        ListNode* fast = head -> next;
        while(fast != nullptr && fast -> next != nullptr){
            slow = slow -> next;
            fast = fast -> next -> next;
        }
        return slow;
    }
    ListNode* sortList(ListNode* head) {
         if (!head || !head->next) return head;
        ListNode* mid = middle(head);
        ListNode* right = mid-> next;
        mid -> next = nullptr;
        ListNode* left = head;
        left = sortList(left);
        right = sortList(right);
        return merge(left,right);
    }
};