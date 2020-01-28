#include <iostream>
#include <algorithm>

using namespace std;

int llist[10001] = {0, };

void self_num(int n){
    int sum;
    sum += n;

    while(n){
        sum += n % 10;
        n /= 10;
    }
    llist[sum] = 1;
}

int main(){
    for(int i = 1; i < 10001; i++){
        self_num(i);
    }

    for(int i = 1; i < 10001; i++){
        if(llist[i] == 0){
            cout << i << endl;
        }
    }

}