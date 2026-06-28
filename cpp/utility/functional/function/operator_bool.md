---
title: std::function::operator bool
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/operator_bool
---

ddcl|since=c++11|
explicit operator bool() const noexcept;
Checks whether `*this` stores a callable function target, i.e. is not empty.

## Parameters

(none)

## Return value

`true` if `*this` stores a callable function target, `false` otherwise.

## Example


### Example

```cpp
#include <functional>
#include <iostream>

void sampleFunction()
{
    std::cout << "This is the sample function!\n";
}

void checkFunc(std::function<void()> const& func)
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
    std::function<void()> f1;
    std::function<void()> f2(sampleFunction);

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


| cpp/utility/functional/move_only_function/dsc operator bool | (see dedicated page) |

