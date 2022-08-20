#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> v;
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

//     for (int i =0; i < 3; i ++){
//         cout << v[i] << "\n";
//     }

    for (auto x: v){
        cout << x <<'\n';
    }

    cout << v.back() << "\n";
    v.pop_back() ;
    cout << v.back()<< "\n";
}
