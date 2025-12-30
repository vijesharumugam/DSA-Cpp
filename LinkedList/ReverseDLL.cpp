// https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

/*
class Node {
  public:
    int data;
    Node *next;
    Node *prev;
    Node(int val) {
        data = val;
        next = NULL;
        prev = NULL;
    }
};

*/
class Solution {
  public:
    Node *reverse(Node *head) {
        // code here
        Node* curr = head;
        Node* last = NULL;
        while(curr != NULL){
            Node* temp = curr -> next;
            curr -> next = curr -> prev;
            curr -> prev = temp;
            last = curr;
            curr = temp;
        }
        return last;
    }
};