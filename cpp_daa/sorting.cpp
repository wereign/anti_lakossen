#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main()
{
    cout<< "Sorting a vector\n";
    vector<int> v = {4, 2, 5, 6, 212, 64};
    sort(v.begin(), v.end());
    for (int i = 0; i < 6; i++)
    {
        cout << v[i] << '\n';
    }
    cout << '\n';
    cout << "Sorting an ordinary array\n";
    int n = 7;
    int a[] = {4, 2, 3, 5, 1, 7, 6};
    sort(a, a + n);
    for (int i = 0; i < 7; i++)
    {
        cout << a[i] << '\n';
    }

    cout << '\n';
    cout << "Sorting a string\n";
    string s = "monkey";
    sort(s.begin(),s.end());
    cout << s << '\n';

    // How to print out a pair of vectors
    // vector <pair<int,int>> v;
    // v.push_back({1,5});
    // v.push_back({5,2});
    // v.push_back({7,6});
    // v.push_back({6,7});
    // sort(v.begin(), v.end());
    // for (int i = 0; i < 4; i++ ){
    //     cout << v[i][0] << '\t' << v[i][1] << '\n';

    // }

    //External comparison functions

    bool comp(string a, string b){
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;

    }

    sort(v.begin(), v.end(), comp);
    
    vector<string> string_vector = {"string 123","string 22","string 3","string 4"};
    sort(string_vector.begin(),string_vector.end(),comp);
    for (int j = 0; j < 4; j++){
        cout << string_vector[j] << "\n";
    }
}
