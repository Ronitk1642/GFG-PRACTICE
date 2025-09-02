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
   Node* revLogic(Node* head){
       Node* p = NULL;
       Node* c = head;
       Node* n = head;
       
       while(n){
           n = n->next;
           c->next = p;
           c->prev = n;
           
           p = c;
           c = n;
       }
       
       return p;
   }
  
    Node *reverse(Node *head) {
        // code here
        
        return revLogic(head);
    }
};

