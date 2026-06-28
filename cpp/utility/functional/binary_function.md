---
title: std::binary_function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/binary_function
---


```cpp
**Header:** `<`functional`>`
dcl|until=c++17|deprecated=c++11|1=
template<
class Arg1,
class Arg2,
class Result
> struct binary_function;
```

`std::binary_function` is a base class for creating function objects with two arguments.
`std::binary_function` does not define `operator()`; it is expected that derived classes will define this. `std::binary_function` provides only three types - `first_argument_type`, `second_argument_type` and `result_type` - defined by the template parameters.
Some standard library function object adaptors, such as `std::not2`, require the function objects they adapt to have certain types defined; `std::not2` requires the function object being adapted to have two types named `first_argument_type` and `second_argument_type`. Deriving function objects that take two arguments from `std::binary_function` is an easy way to make them compatible with those adaptors.
`std::binary_function` is deprecated in C++11 and removed in C++17.

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

struct same : std::binary_function<int, int, bool>
{
    bool operator()(int a, int b) const { return a == b; }
};

int main()
{
    std::vector<char> v1{'A', 'B', 'C', 'D', 'E'};
    std::vector<char> v2{'E', 'D', 'C', 'B', 'A'};
    std::vector<bool> v3(v1.size());

    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), std::not2(same()));

    std::cout << std::boolalpha;
    for (std::size_t i = 0; i < v1.size(); ++i)
        std::cout << v1[i] << " != " << v2[i] << " : " << v3[i] << '\n';
}
```


**Output:**
```
A != E : true
B != D : true
C != C : false
D != B : true
E != A : true
```


## See also


| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |
| cpp/utility/functional/dsc pointer_to_binary_function | (see dedicated page) |
| cpp/utility/functional/dsc unary_function | (see dedicated page) |

