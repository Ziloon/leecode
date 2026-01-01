#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int* returnDigits = (int *)malloc(sizeof(int) * digitsSize);
    if (returnDigits == NULL || returnSize == NULL)
    {
        return NULL;
    }
    memcpy(returnDigits, digits, digitsSize * sizeof(digits[0]));
    *returnSize = digitsSize;
    for (int i = (digitsSize-1); i >= 0; i--)
    {
        if(returnDigits[i] < 9) {
            returnDigits[i] += 1;
            return returnDigits;
        }
        returnDigits[i] = 0;
    }

    *returnSize += 1;
    free(returnDigits);
    returnDigits = (int *)malloc(sizeof(int) * (digitsSize+1));
    if (returnDigits == NULL) {
        return NULL;
    }
    returnDigits[0] = 1;
    memset(&(returnDigits[1]), 0, sizeof(int) * digitsSize);
    return returnDigits;
}

int main(int argc, char const *argv[])
{
    {
        int digits[] = {9,9,9,9};
        int digitsSize = sizeof(digits)/sizeof(digits[0]);
        int returnSize = 0;
        int *returnDigits = plusOne(digits, digitsSize, &returnSize);
        printf("%d\n", returnSize);
    }
    return 0;
}
