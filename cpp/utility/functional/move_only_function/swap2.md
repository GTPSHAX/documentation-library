---
title: swap(std::move_only_function)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/move_only_function/swap2
---


# swappetty|(std::move_only_function)

ddcl|since=c++23|
friend void swap( std::move_only_function& lhs, std::move_only_function& rhs ) noexcept;
Overloads the `std::swap` algorithm for `std::move_only_function`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - `std::move_only_function` objects whose states to swap

## Return value

(none)

## Example


### Example

```cpp
#include <concepts>
#include <functional>
#include <iostream>

void foo(const char* str, int x)
{
    std::cout << "foo(\"" << str << "\", " << x << ")\n";
}

void bar(const char* str, int x)
{
    std::cout << "bar(\"" << str << "\", " << x << ")\n";
}

int main()
{
    std::move_only_function<void(const char*, int) const> f1{foo};
    std::move_only_function<void(const char*, int) const> f2{bar};

    f1("f1", 1);
    f2("f2", 2);

    std::cout << "std::ranges::swap(f1, f2);\n";
    std::ranges::swap(f1, f2); // finds the hidden friend

    f1("f1", 1);
    f2("f2", 2);
}
```


**Output:**
```
foo("f1", 1)
bar("f2", 2)
std::ranges::swap(f1, f2);
bar("f1", 1)
foo("f2", 2)
```


## See also


| cpp/utility/functional/move_only_function/dsc swap | (see dedicated page) |
| cpp/utility/functional/function/dsc swap2 | (see dedicated page) |

