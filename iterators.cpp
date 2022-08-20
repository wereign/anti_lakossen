#include <iostream>
#include <set>


using namespace std;
int main(){
    set<int> s;
    s.insert(1);
    s.insert(2);
    s.insert(3);
    s.insert(4);

    // auto it = s.begin();
    set<int>::iterator it = s.begin();
    cout << *it << "\n";
}