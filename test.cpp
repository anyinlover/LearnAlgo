#include <iostream>;
#include <map>
#include <string>
#include <functional>

using namespace std;

struct Test {
optional<reference_wrapper<const int>> make(bool a)
{
    if (a) {
        reference_wrapper<const int> b = cref(_a);
        return b;
    }
    return nullopt;
}
int _a = 10;
};

int main()
{
    auto t = Test();
    if (auto a = t.make(true)) {
        cout << *a << endl;
    }
    return 0;
}