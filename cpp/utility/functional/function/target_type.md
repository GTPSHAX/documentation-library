---
title: std::function::target_type
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/target_type
---

ddcl|since=c++11|
const std::type_info& target_type() const noexcept;
Returns the type of the stored function.

## Parameters

(none)

## Return value

`typeid(T)` if the stored function has type `T`, otherwise `typeid(void)`

## Example


### Example

```cpp
#include <functional>
#include <iostream>

int f(int a) { return -a; }
void g(double) {}
int main()
{
    // fn1 and fn2 have the same type, but their targets do not
    std::function<int(int)> fn1(f),
                            fn2([](int a) {return -a;});
    std::cout << fn1.target_type().name() << '\n'
              << fn2.target_type().name() << '\n';

    // since C++17 deduction guides (CTAD) can avail
    std::cout << std::function{g}.target_type().name() << '\n';
}
```


**Output:**
```
PFiiE
Z4mainEUliE_
PFvdE
```


## See also


| cpp/utility/functional/function/dsc target | (see dedicated page) |
| cpp/types/dsc type_info | (see dedicated page) |

