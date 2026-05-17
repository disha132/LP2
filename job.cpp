#include <iostream>
#include <algorithm>
using namespace std;

struct Job
{
    char id;
    int deadline;
    int profit;
};

// Function to compare jobs according to profit
bool compare(Job a, Job b)
{
    return a.profit > b.profit;
}

int main()
{
    Job jobs[] = {
        {'A', 2, 100},
        {'B', 1, 19},
        {'C', 2, 27},
        {'D', 1, 25},
        {'E', 3, 15}
    };

    int n = sizeof(jobs) / sizeof(jobs[0]);

    // Sort jobs by profit
    sort(jobs, jobs + n, compare);

    int slot[10] = {0};
    char result[10];

    int totalProfit = 0;

    // Job scheduling
    for (int i = 0; i < n; i++)
    {
        for (int j = jobs[i].deadline - 1; j >= 0; j--)
        {
            if (slot[j] == 0)
            {
                slot[j] = 1;
                result[j] = jobs[i].id;
                totalProfit += jobs[i].profit;
                break;
            }
        }
    }

    cout << "Selected Jobs: ";

    for (int i = 0; i < n; i++)
    {
        if (slot[i])
            cout << result[i] << " ";
    }

    cout << "\nTotal Profit: " << totalProfit;

    return 0;
}
