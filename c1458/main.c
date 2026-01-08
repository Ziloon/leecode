#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MAX(a, b) (((a) >= (b)) ? (a) : (b))
int maxDotProduct(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    int rows = nums1Size + 1;
    int cols = nums2Size + 1;

    int *dp = (int *)malloc(sizeof(int) * rows * cols);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            dp[i * cols + j] = -1e9;
        }
    }

    for (int i = 1; i <= nums1Size; i++)
    {
        for (int j = 1; j <= nums2Size; j++)
        {
            int cur_pair = nums1[i - 1] * nums2[j - 1];
            int with_prev = cur_pair + MAX(0, dp[(i - 1) * cols + (j - 1)]);
            dp[i * cols + j] = MAX(MAX(dp[(i - 1) * cols + j],
                                       dp[i * cols + (j - 1)]),
                                   with_prev);
        }
    }

    int result = dp[nums1Size * cols + nums2Size];
    free(dp);
    return result;
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
        int nums2[] = {2, -6, 7};
        assert(21 == maxDotProduct(nums1, sizeof(nums1) / sizeof(nums1[0]), nums2, sizeof(nums2) / sizeof(nums2[0])));
    }
    {
        int nums1[] = {-1, -1};
        int nums2[] = {1, 1};
        assert(-1 == maxDotProduct(nums1, sizeof(nums1) / sizeof(nums1[0]), nums2, sizeof(nums2) / sizeof(nums2[0])));
    }
    return 0;
}
