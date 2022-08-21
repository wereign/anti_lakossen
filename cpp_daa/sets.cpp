#include <iostream>
#include <set>

using namespace std;

int main(){
    set<int> s;
    s.insert(3);
    s.insert(2);
    s.insert(2);
    s.insert(5);

    cout << s.count(3) << '\n';
    cout << s.count(2) << '\n';
    cout << s.count(5) << '\n';
    cout << s.count(6) << '\n';

    cout << "Size " << s.size() << '\n';

    for (auto x: s){
        cout << x << '\n';
    }
}