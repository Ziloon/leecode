#include <stdio.h>

int countNegatives(int **grid, int gridSize, int *gridColSize)
{
    int cnt = 0;
    int i = 0;
    int j = *gridColSize - 1;
    for (int i = 0; i < gridSize; i++)
    {
        while (j >= 0 && grid[i][j] < 0)
        {
            j--;
        }
        cnt += (*gridColSize) - j - 1;
    }
    return cnt;
}

int main(int argc, char const *argv[])
{
    {
        int *grid[] = {
            (int[]){4, 3, 2, -1}, (int[]){3, 2, 1, -1}, (int[]){1, 1, -1, -2}, (int[]){-1, -1, -2, -3}
        };
        int cosSize = 4;
        printf("8, %d\n", countNegatives(grid, 4, &cosSize));
    }
        {
        int *grid[] = {
            (int[]){3,2}, (int[]){1,0}
        };
        int cosSize = 2;
        printf("0, %d\n", countNegatives(grid, 2, &cosSize));
    }
    return 0;
}
