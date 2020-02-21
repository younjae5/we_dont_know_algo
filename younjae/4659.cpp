#include <iostream>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

set<char> vow = {'a', 'e', 'i', 'o', 'u'}; //모음
set<char> con = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 
't', 'v', 'w', 'x', 'y', 'z'}; //자음

//연속된 세글자가 오는지 확인하기 위한 iterator
set <char>::iterator iter1;
set <char>::iterator iter2;
set <char>::iterator iter3;

int find_vow(char cha){
    iter1 = vow.find(cha);
    if(iter1 != vow.end()){
        return 1;
    }else return 0;
}

int main(){

    string word;
    
    while(1){
        bool accept = true;
        int num = 0; //모음 유무 관리
        cin >> word;
        
        if(word == "end"){
            break;
        }

        

        //word가 1글자 일때 모음 유무만 추리
        if(word.length() == 1){
            if(find_vow(word[0]))
                num++;
        }

        // word가 2글자일때 모음 유무와 같은 글자의 연속성 판정
        if(word.length() == 2){

            //모음 유무
            for(int i = 0; i < 2; i++){
                if(find_vow(word[i]))
                    num++;}
            }

            if(word[0] == word[1]){
                // 연속된 글자가 ee나 oo인 경우가 아니면 틀린 비밀번호
                if( word[0] != 'e' or word[0] != 'o'){
                    accept = false;
                }
            }
        }

        // word가 3글자 이상인 경우
        for(int i = 0 ; i < word.length(); i++){
            if(find_vow(word[i])){
                num++;}
        }



        
    }

}