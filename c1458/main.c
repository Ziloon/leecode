#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MAX(a, b) (((a) >= (b)) ? (a) : (b))
#define EMPTY (-1e9-7)
int getSubProduct(int *nums1, int i, int *nums2, int j, int *memo, int colSize)
{
    int product = INT_MIN;
    if (memo[i * colSize + j] != EMPTY)
    {
        return memo[i * colSize + j];
    }
    if (i == 0 || j == 0)
    {
        return -1e9;
    }
    int cur_pair = nums1[i - 1] * nums2[j - 1] + MAX(0, getSubProduct(nums1,  i - 1, nums2, j - 1, memo, colSize));

    memo[i * colSize + j] = MAX(MAX(getSubProduct(nums1,  i, nums2, j - 1, memo, colSize), getSubProduct(nums1,  i - 1, nums2, j, memo, colSize)), cur_pair);
    return memo[i * colSize + j];
}
int maxDotProduct(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    int *memo = (int *)malloc(sizeof(int) * ((nums1Size + 1) * (nums2Size + 1)));
    for (size_t i = 0; i < (nums1Size + 1) * (nums2Size + 1); i++)
    {
        memo[i] = EMPTY;
    }
    int product = getSubProduct(nums1, nums1Size, nums2, nums2Size, memo, nums2Size+1);
    free(memo);
    memo = NULL;
    return product;
}

int main(int argc, char const *argv[])
{
    {
        int nums1[] = {2, 1, -2, 5};
        int nums2[] = {3, 0, -6};
        assert(18 == maxDotProduct(nums1, sizeof(nums1) / sizeof(nums1[0]), nums2, sizeof(nums2) / sizeof(nums2[0])));
    }
    {
        int nums1[] = {3, -2};
        int nums2[] = {
            2,
            -6,
        };
        assert(21 == maxDotProduct(nums1, sizeof(nums1) / sizeof(nums1[0]), nums2, sizeof(nums2) / sizeof(nums2[0])));
    }
    {
        int nums1[] = {-1, -1};
        int nums2[] = {1, 1};
        assert(-1 == maxDotProduct(nums1, sizeof(nums1) / sizeof(nums1[0]), nums2, sizeof(nums2) / sizeof(nums2[0])));
    }
    return 0;
}
