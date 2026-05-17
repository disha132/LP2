#include <iostream>
using namespace std;

int N = 4;

char board[4][4];

// Arrays for Branch and Bound
bool column[4];
bool leftDiagonal[10];
bool rightDiagonal[10];

// Function to solve N-Queens
bool solve(int row)
{
    // All queens placed
    if (row == N)
    {
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
        return true;
    }

    // Try every column
    for (int col = 0; col < N; col++)
    {
        // Check if safe
        if (!column[col] &&
            !leftDiagonal[row - col + N - 1] &&
            !rightDiagonal[row + col])
        {
            // Place queen
            board[row][col] = 'Q';

            // Mark occupied
            column[col] = true;
            leftDiagonal[row - col + N - 1] = true;
            rightDiagonal[row + col] = true;

            // Recursive call
            if (solve(row + 1))
                return true;

            // Backtrack
            board[row][col] = '.';

            column[col] = false;
            leftDiagonal[row - col + N - 1] = false;
            rightDiagonal[row + col] = false;
        }
    }

    return false;
}

int main()
{
    // Initialize board
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            board[i][j] = '.';
        }
    }

    solve(0);

    return 0;
}
