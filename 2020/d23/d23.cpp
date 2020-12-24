#include <stdlib.h>
#include <iostream>
#include <map>

class Node {
  public:
    int value;
    Node* next;
    Node(int _value, Node* _next) {
        value = _value;
        next = _next;
    }
    Node() {
        value = 0;
        next = NULL;
    }
};

bool inArray(int value, int list[3]) {
    for(int i = 0; i < 3; i++) {
        if (value == list[i])
            return true;
    }
    return false;
}


void crab_cups(Node* f,int length, int iterations, Node* d[]) {
    Node* curr = f;
    int num = length;
    for(int i = 0; i < iterations; i++) {
        //printf("Iteration %d started\n", i);
        // Get pointers & values to next 3 nodes        
        Node* n1 = curr->next;
        Node* n3 = n1->next->next;
        Node* n4 = n3->next;
        int rmvd [3] = {n1->value, n1->next->value, n3->value};
        //printf("Values moved: %d, %d, %d \n",n1->value, n1->next->value, n3->value);
        // Update pointers for current
        curr->next = n4;
        // Find destination
        int n = curr->value;
        Node* dest = NULL;
        while(true) {
            n--;
            if (n == 0)
                n = num;
            if (!inArray(n,rmvd)) {
                dest = d[n-1];
                break;
            }
        }
        //printf("Moved after %d \n\n",n);
        // Assign updated pointers
        Node* destn1 = dest->next;
        dest->next = n1;
        n3->next = destn1;
        // Update current node
        curr = curr->next;
    }
    return;
}

int main() {
    char inp[] = "215694783";
    // === Part 1 ===
    //std::map<int,Node*> d;
    int len = 9;
    Node* d [len];
    Node node_l[len];
    for (int i = 0; i < len; i++) {
        int v = inp[i] - '0';
        Node n = Node(v, NULL);
        node_l[i] = n;
    }
    for (int i = 0; i < len; i++) {
        Node* n = &node_l[i];
        n->next = &node_l[(i+1)%len];
        d[n->value-1] = n;
    }

    crab_cups(&node_l[0],len,100,d);

    printf("/P1/ Order starting from one:");
    Node* curr = d[0]->next;
    for (int i = 0; i < 9; i++) {
        int v = curr->value;
        printf("%d", v);
        curr = curr->next;
    }
    printf("\n");

    // === Part 2 ===
    //std::map<int,Node*> _d;
    len = 1000000;
    Node*_node_l = (Node*) malloc(len * sizeof(Node));
    Node** _d = (Node**) malloc(len * sizeof(Node*));

    //Node* _d [1000000];
    
    for (int i = 0; i < 9; i++) {
        int v = inp[i] - '0';
        Node n = Node(v, NULL);
        _node_l[i] = n;
    }
    for (int i = 9; i < len; i++) {
        Node n = Node(i+1, NULL);
        _node_l[i] = n;
    }
    for (int i = 0; i < len-1; i++) {
        Node* n = &_node_l[i];
        n->next = &_node_l[(i+1)];
        _d[n->value-1] = n;
    }
    Node* n = &_node_l[len-1];
    n->next = &_node_l[0];
    _d[n->value-1] = n;
    crab_cups(&_node_l[0],len,10000000,_d);

    Node* c = _d[0];
    long long int fs = c->next->value;
    long long int sn = c->next->next->value;
    long long int res = fs*sn;
    printf("/P2/ Values after 1: %lld * %lld = %lld\n",fs,sn,res);


    return 0;
}