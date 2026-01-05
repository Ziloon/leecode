#include <stdlib.h>
#include <stdio.h>

long long maxMatrixSum(int **matrix, int matrixSize, int *matrixColSize)
{
    long long sum = 0;
    int neg_cnt = 0;
    int num_min = INT_MAX;
    for (size_t i = 0; i < matrixSize; i++)
    {
        for (size_t j = 0; j < matrixColSize[i]; j++)
        {
            long long num_abs = abs(matrix[i][j]);
            sum += num_abs;
            if (matrix[i][j] < 0)
            {
                neg_cnt ^= 1;
            }
            if (num_abs < num_min)
            {
                num_min = num_abs;
            }
        }
    }
    sum = sum - num_min * 2 * neg_cnt;
    return sum;
}

int main(int argc, char const *argv[])
{
    {
        int *matrix[] = {
            (int[]){1, -1},
            (int[]){-1, 1}};
        int matrixColSize[] = {2, 2};
        printf("4, %ld\n", maxMatrixSum(matrix, 2, matrixColSize));
    }
    {
        int *matrix[] = {
            (int[]){1, 2, 3},
            (int[]){-1, -2, -3},
            (int[]){1, 2, 3}};
        int matrixColSize[] = {3, 3, 3};
        printf("16, %ld\n", maxMatrixSum(matrix, 3, matrixColSize));
    }
    return 0;
}
