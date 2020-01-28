#include <iostream>

using namespace std;

int main()
{
    int n, m, answer;
    cin >> n >> m;
    answer = (n-1) + (m-1) * n;
    cout << answer;
}