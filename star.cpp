#include <iostream>
using namespace std;
int main(){
    int space, rows;
    cout <<"Enter number of rows: ";
    cin >> rows;
    int i, k=0;

    for(i=1; i <= rows; ++i, k = 0){
        for(space = 1; space <= rows-i; space++){
            cout <<"  ";
        }

        while(k != 2*i-1){
            cout << "* ";
            ++k;
        }
        cout << endl;
    }    
    return 0;
}
