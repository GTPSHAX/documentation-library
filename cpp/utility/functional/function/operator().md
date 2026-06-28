---
title: std::function::operator()
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/operator()
---

ddcl|since=c++11|
R operator()( Args... args ) const;
Invokes the stored callable function target with the parameters `args`.
Effectively does , where `f` is the `target object` of `*this`.

## Parameters


### Parameters

- `args` - parameters to pass to the stored callable function target

## Return value

None if `R` is `void`. Otherwise the return value of the invocation of the stored callable object.

## Exceptions

Throws `std::bad_function_call` if `*this` does not store a callable function target, i.e. `1=!*this == true`.

## Example


### Example

```cpp
#include <functional>
#include <iostream>

void call(std::function<int()> f) // can be passed by value
{ 
    std::cout << f() << '\n';
}

int normal_function()
{
    return 42;
}

int main()
{
    int n = 1;
    std::function<int()> f;
    try
    {
        call(f);
    }
    catch (const std::bad_function_call& ex)
    {
        std::cout << ex.what() << '\n';
    }

    f = [&n](){ return n; };
    call(f);

    n = 2;
    call(f);

    f = normal_function;
    call(f);

    std::function<void(std::string, int)> g;
    g = [](std::string str, int i) { std::cout << str << ' ' << i << '\n'; };
    g("Hi", 052);
}
```


**Output:**
```
bad_function_call
1
2
42
Hi 42
```


## See also


| cpp/utility/functional/move_only_function/dsc operator() | (see dedicated page) |
| cpp/utility/functional/reference_wrapper/dsc operator() | (see dedicated page) |
| cpp/utility/functional/dsc bad_function_call | (see dedicated page) |
| cpp/utility/functional/dsc invoke | (see dedicated page) |

