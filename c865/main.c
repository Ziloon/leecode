#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define EMPTY (-10e9)

/*
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {
    return NULL;
}

struct TreeNode* newNode(int val) {
    if (val < 0) {
        return NULL;
    }
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = val;
    root->left = NULL;
    root->right = NULL;
    return root;
}
struct TreeNode* buildTree(int tree[], int treeSize) {
    if (treeSize == 0 || tree[0] < 0) {
        return NULL;
    }
    struct TreeNode* root = newNode(tree[0]);
    struct TreeNode** queue = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * treeSize);
    int head = 0;
    int tail = 0;
    queue[tail++] = root;
    for (size_t i = 1; i < treeSize;) {
        struct TreeNode* cur = queue[head++];
        if (i < treeSize) {
            cur->left = newNode(tree[i++]);
            if (cur->left != NULL) {
                queue[tail++] = cur->left;
            }
        }
        if (i < treeSize) {
            cur->right = newNode(tree[i++]);
            if (cur->right != NULL) {
                queue[tail++] = cur->right;
            }
        }
    }
    free(queue);
    return root;
}

void destroyTree(struct TreeNode** root) {
    if (root == NULL || (*root) == NULL) {
        return;
    }
    destroyTree(&((*root)->left));
    destroyTree(&((*root)->right));
    free(*root);
    *root = NULL;
    return;
}

bool compareTree(struct TreeNode* a, struct TreeNode* b) {
    if (a == NULL && b == NULL) {
        return true;
    } else if (a == NULL || b == NULL) {
        return false;
    }
    if (compareTree(a->left, b->left) == false) {
        return false;
    }
    if (compareTree(a->right, b->right) == false) {
        return false;
    }
    return true;
}

int main(int argc, char const* argv[]) {
    {
        int root[] = {3, 5, 1, 6, 2, 0, 8, EMPTY, EMPTY, 7, 4};
        struct TreeNode* tree = buildTree(root, sizeof(root) / sizeof(root[0]));
        int rec[] = {2, 7, 4};
        struct TreeNode* expectTree = buildTree(rec, sizeof(rec) / sizeof(rec[0]));
        assert(compareTree(expectTree, subtreeWithAllDeepest(tree)));
    }
    return 0;
}
