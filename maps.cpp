#include  <iostream>
#include <map>

using namespace std;

int main(){
    map<string, int> m;
    m["monkey"] = 4;
    m["banana"] = 3;
    m["harpischord"] = 9;
    cout << m["banana"] << "\n";
    cout << m["random"] << "\n";

    if (m.count("random")) cout << "random is in map\n";
    else cout << "random is not in map";

    if (m.count("rand")) cout << "rand is in map\n";
    else cout << "rand is not in map";
}