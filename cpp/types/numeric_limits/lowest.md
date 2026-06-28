---
title: std::numeric_limits::lowest
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/lowest
---


```cpp
dcl|since=c++11|
static constexpr T lowest() noexcept;
```

Returns the lowest finite value representable by the numeric type `T`, that is, a finite value `x` such that there is no other finite value `y` where `y < x`. This is different from `std::numeric_limits<T>::min()` for floating-point types. Only meaningful for bounded types.

## Return value


## Notes

For every standard C++ floating-point type `T` `1=std::numeric_limits<T>::lowest() == -std::numeric_limits<T>::max()`, but this does not necessarily have to be the case for any third-party specialization.

## Example


### Example

```cpp
#include <iostream>
#include <limits>
#include <string_view>

template<typename T>
void print_twice(std::string_view type, T value)
{
    std::cout << '\t' << type << ": "
              << std::defaultfloat << value << " or "
              << std::hexfloat << value << '\n';
}

int main()
{
    // min()
    std::cout << "std::numeric_limits<T>::min():\n";
    print_twice("float", std::numeric_limits<float>::min());
    print_twice("double", std::numeric_limits<double>::min());
    print_twice("long double", std::numeric_limits<long double>::min());

    // lowest()
    std::cout << "std::numeric_limits<T>::lowest():\n";
    print_twice("float", std::numeric_limits<float>::lowest());
    print_twice("double", std::numeric_limits<double>::lowest());
    print_twice("long double", std::numeric_limits<long double>::lowest());

    // max()
    std::cout << "std::numeric_limits<T>::max():\n";
    print_twice("float", std::numeric_limits<float>::max());
    print_twice("double", std::numeric_limits<double>::max());
    print_twice("long double", std::numeric_limits<long double>::max());
}
```


**Output:**
```
std::numeric_limits<T>::min():
	float: 1.17549e-38 or 0x1p-126
	double: 2.22507e-308 or 0x1p-1022
	long double: 3.3621e-4932 or 0x8p-16385
std::numeric_limits<T>::lowest():
	float: -3.40282e+38 or -0x1.fffffep+127
	double: -1.79769e+308 or -0x1.fffffffffffffp+1023
	long double: -1.18973e+4932 or -0xf.fffffffffffffffp+16380
std::numeric_limits<T>::max():
	float: 3.40282e+38 or 0x1.fffffep+127
	double: 1.79769e+308 or 0x1.fffffffffffffp+1023
	long double: 1.18973e+4932 or 0xf.fffffffffffffffp+16380
```


## See also


| cpp/types/numeric_limits/dsc min | (see dedicated page) |
| cpp/types/numeric_limits/dsc denorm_min | (see dedicated page) |
| cpp/types/numeric_limits/dsc max | (see dedicated page) |

