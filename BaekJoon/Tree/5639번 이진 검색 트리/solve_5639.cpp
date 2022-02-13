#include <iostream>
using namespace std;


class Node{
public:
    int data;
    Node* left;
    Node* right;

    Node(int _data, Node* _left, Node* _right) : data(_data), left(_left), right(_right)
    { }
};


class BinaryTree{
public:
    Node* root;

    BinaryTree(){
        root = nullptr;
    }

    bool Insert(int insert_num){
        if (root == nullptr){
            root = new Node(insert_num, nullptr, nullptr);
            return true;
        }

        else {
            return InsertRecursion(root, insert_num);
        }
    }

    bool InsertRecursion(Node *cur_node, int num){
        // 현재 노드가 nullptr이면 노드 생성 후 넣기
        // 현재 노드와 비교했을 때 작으면 왼쪽 크면 오른쪽 노드와 비교
        if (num < cur_node->data) {
            if (cur_node->left == nullptr)
                cur_node->left = new Node(num, nullptr, nullptr);
            else
                InsertRecursion(cur_node->left, num);
        }
        else {
            if (cur_node->right == nullptr)
                cur_node->right = new Node(num, nullptr, nullptr);
            else
                InsertRecursion(cur_node->right, num);
        }

        return true;
    }

    void PostOrder(Node *cur_node){
        if (cur_node->left != nullptr)
            PostOrder(cur_node->left);
        if (cur_node->right != nullptr)
            PostOrder(cur_node->right);
        cout << cur_node->data << endl;
    }
};


int main() {
    BinaryTree bt;
    int n;
    while (cin >> n)
        bt.Insert(n);
    bt.PostOrder(bt.root);
    return 0;
}