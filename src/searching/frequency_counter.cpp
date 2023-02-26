#include <string>
#include <iostream>
#include "st.h"
#include "binary_search_tree_st.h"

using namespace std;

/* int test(int minLen, ST<string, int> st)
{
    string word;
    while (cin >> word) {
        if (word.size() >= minLen) {
            if (!st.Contains(word))
                st.Put(std::move(word), 1);
            else
                st.Put(std::move(word), st.Get(word) + 1);
        }
    }
    st.Put("", 0);
    auto maxIter = st.KeyIter("");
    for (auto iter = st.Begin(); iter != st.End(); iter++) {
        if (iter->second > maxIter->second) {
            maxIter = iter;
        }
    }
    cout << maxIter->first << " " << maxIter->second << endl;
} */

int main(int argc, char* argv[])
{
    int minLen;
    if (argc > 1)
        minLen = stoi(argv[1]);
    else {
        cerr << "Lack a integer param!" << endl;
        return 1;
    }

    auto st = BST<string, int>();
    st.Put("a",2);
    st.Get("a");
    return 0;


}