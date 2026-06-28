---
title: std::move_only_function::operator bool
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/move_only_function/operator_bool
---

ddcl|since=c++23|
explicit operator bool() const noexcept;
Checks whether `*this` stores a callable target, i.e. is not empty.

## Parameters

(none)

## Return value

`true` if `*this` stores a callable target, `false` otherwise.

## Example


### Example

```cpp
#include <functional>
#include <iostream>

void sampleFunction()
{
    std::cout << "This is the sample function!\n";
}

void checkFunc(std::move_only_function<void() const> const& func)
{
    // Use operator bool to determine if callable target is available.
    if (func)
    {
        std::cout << "Function is not empty! Calling function.\n";
        func();
    }
    else
        std::cout << "Function is empty. Nothing to do.\n";
}

int main()
{
    std::move_only_function<void() const> f1{};
    std::move_only_function<void() const> f2{sampleFunction};

    std::cout << "f1: ";
    checkFunc(f1);

    std::cout << "f2: ";
    checkFunc(f2);
}
```


**Output:**
```
f1: Function is empty. Nothing to do.
f2: Function is not empty! Calling function.
This is the sample function!
```


## See also


| cpp/utility/functional/move_only_function/dsc operator{{== | (see dedicated page) |
| cpp/utility/functional/function/dsc operator bool | (see dedicated page) |

