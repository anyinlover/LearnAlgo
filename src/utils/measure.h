#ifndef MEASURE_H

#include <chrono>

using Seconds = std::chrono::duration<double>;

template<typename Function, typename... Args>
Seconds measure(Function&& toTime, Args&&... a)
{
    auto start{std::chrono::steady_clock::now()};
    std::invoke(std::forward<Function>(toTime), std::forward<Args>(a)...);
    auto stop{std::chrono::steady_clock::now()};
    return stop - start;
}

#endif // !MEASURE_H