---
title: std::unary_function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/unary_function
---


```cpp
**Header:** `<`functional`>`
dcl|until=c++17|deprecated=c++11|1=
template< typename ArgumentType, typename ResultType >
struct unary_function;
```

`std::unary_function` is a base class for creating function objects with one argument.
`std::unary_function` does not define `operator()`; it is expected that derived classes will define this. `std::unary_function` provides only two types - `argument_type` and `result_type` - defined by the template parameters.
Some standard library function object adaptors, such as `std::not1`, require the function objects they adapt to have certain types defined; `std::not1` requires the function object being adapted to have a type named `argument_type`. Deriving function objects that take one argument from `std::unary_function` is an easy way to make them compatible with those adaptors.
`std::unary_function` is deprecated in C++11.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

struct less_than_7 : std::unary_function<int, bool>
{
    bool operator()(int i) const { return i < 7; }
};

int main()
{
    std::vector<int> v(10, 7);
    v[0] = v[1] = v[2] = 6;

    std::cout << std::count_if(v.begin(), v.end(), std::not1(less_than_7()));

    // C++11 solution:
    // Cast to std::function<bool (int)> somehow - even with a lambda
    // std::cout << std::count_if(v.begin(), v.end(),
    //     std::not1(std::function<bool (int)>([](int i) { return i < 7; })));
}
```


**Output:**
```
7
```


## See also


| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |
| cpp/utility/functional/dsc pointer_to_unary_function | (see dedicated page) |
| cpp/utility/functional/dsc binary_function | (see dedicated page) |

