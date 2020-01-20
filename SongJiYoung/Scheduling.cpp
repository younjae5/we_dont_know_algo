#include <iostream>
#include "math.h"

using namespace std;

int main()
{
    int n;
     //time, price 배열 만들기
    int time[15] = {0, };
    int price[15] = {0, };
    int answer[15] = {0, };
    cin >> n;

    //price, answer, time 배열에 입력값 넣기
    for(int i = 1; i <= n; i++)
    {
        cin >> time[i] >> price[i];
        answer[i] = price[i];
    }
    

    for(int i = 2; i <= n; i++)
    {
        for(int j = 1; j < i; j++)
        {
            //상담 시간이 겹치지 않으면
            if(i-j >= time[j])
            {
                answer[i] = max(price[i] + answer[j], answer[i]);
            }
                        
        }
    }
    int max = 0;
    for(int i = 1; i <= n; i++)
    {
        //퇴사일을 넘어가지 않는 기간 내애서
        if(i + time[i] <= n+1)
        {
            if(answer[i] >= max)
            {
                max = answer[i];
            }
        }
       
    }

    cout << max << endl;


}

