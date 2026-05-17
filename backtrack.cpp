#include <iostream>
using namespace std;

int N = 4;
char board[4][4];

// Function to check if position is safe
bool isSafe(int row, int col)
{
    // Check upper column
    for (int i = 0; i < row; i++)
    {
        if (board[i][col] == 'Q')
            return false;
    }

    // Check left diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
    {
        if (board[i][j] == 'Q')
            return false;
    }

    // Check right diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++)
    {
        if (board[i][j] == 'Q')
            return false;
    }

    return true;
}

// Backtracking function
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

    // Try each column
    for (int col = 0; col < N; col++)
    {
        if (isSafe(row, col))
        {
            board[row][col] = 'Q';

            if (solve(row + 1))
                return true;

            // Backtrack
            board[row][col] = '.';
        }
    }

    return false;
}

int main()
{
    // Initialize board with '.'
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
