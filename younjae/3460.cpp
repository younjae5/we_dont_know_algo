#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    int time;
    cin >> time;
    while(time--){
        int num;
        cin >> num;
        int temp = 0;
        while(num > 0){
            if(num % 2 == 1){
                cout << temp << ' ';
            }
            num /= 2;
            temp++;
        }

        cout << endl;

    }
}