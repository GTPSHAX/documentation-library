---
title: std::overflow_error
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/overflow_error
---

ddcl|header=stdexcept|
class overflow_error;
Defines a type of object to be thrown as exception. It can be used to report arithmetic overflow errors (that is, situations where a result of a computation is too large for the destination type).
rev|until=c++11|
The only standard library component that throws this exception is `std::bitset::to_ulong`.
rev|since=c++11|
The only standard library components that throw this exception are `std::bitset::to_ulong` and `std::bitset::to_ullong`.
The mathematical functions of the standard library components do not throw this exception (mathematical functions report overflow errors as specified in `math_errhandling`). Third-party libraries, however, use this. For example,
[https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/error_handling.html boost.math] throws `std::overflow_error` if `boost::math::policies::throw_on_error` is enabled (the default setting).

## Member functions


## Example


### Example

```cpp
#include <iostream>
#include <limits>
#include <stdexcept>
#include <utility>

template<typename T, int N>
    requires (N > 0) /*...*/
class Stack
{
    int top_{-1};
    T data_[N];

public:
    [[nodiscard]] bool empty() const { return top_ == -1; }

    void push(T x)
    {
        if (top_ == N - 1)
            throw std::overflow_error("Stack overflow!");
        data_[++top_] = std::move(x);
    }

    void pop()
    {
        if (empty())
            throw std::underflow_error("Stack underflow!");
        --top_;
    }

    T const& top() const
    {
        if (empty())
            throw std::overflow_error("Stack is empty!");
        return data_[top_];
    }
};

int main()
{
    Stack<int, 4> st;

    try
    {
        [[maybe_unused]] auto x = st.top();
    }
    catch (std::overflow_error const& ex)
    {
        std::cout << "1) Exception: " << ex.what() << '\n';
    }

    st.push(1337);
    while (!st.empty())
    	st.pop();

    try
    {
        st.pop();
    }
    catch (std::underflow_error const& ex)
    {
        std::cout << "2) Exception: " << ex.what() << '\n';
    }

    try
    {
        for (int i{}; i != 13; ++i)
            st.push(i);
    }
    catch (std::overflow_error const& ex)
    {
        std::cout << "3) Exception: " << ex.what() << '\n';
    }
}
```


**Output:**
```
1) Exception: Stack is empty!
2) Exception: Stack underflow!
3) Exception: Stack overflow!
```


## Defect reports

