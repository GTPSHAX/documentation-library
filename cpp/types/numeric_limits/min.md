---
title: std::numeric_limits::min
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/min
---


```cpp
**Header:** `<`limits`>`
dcl rev multi|until1=c++11
|dcl1=
static T min() throw();
|dcl2=
static constexpr T min() noexcept;
```

Returns the minimum finite value representable by the numeric type `T`.
For floating-point types with denormalization, `min()` returns the minimum positive normalized value.  ''Note that this behavior may be unexpected'', especially when compared to the behavior of `min()` for integral types. <sup>(since C++11)</sup> To find the value that has no values less than it, use
`min()` is only meaningful for bounded types and for unbounded unsigned types.

## Return value


| Item | Description |
|------|-------------|
| **{{tt** | T |


## Example


### Example

```cpp
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <limits>

// we want to print char types as an integer without leading Fs
auto p(auto x) { return x; }
auto p(char x) { return x & static_cast<unsigned char>(-1); }

template <typename T>
void print_one(std::string_view type_name)
{
    constexpr T min = std::numeric_limits<T>::min();

    std::cout 
        << std::dec << std::defaultfloat << std::setw(14) << type_name
        << " (" << std::setw(2) << sizeof(T) << " bytes): " << +min;

    if constexpr (min != 0)
        std::cout << " or " << std::showbase << std::hex << std::hexfloat << p(min);

    std::cout << '\n';
}

#define SHOW(T) print_one<T>(#T)

int main()
{
    SHOW(bool);
    SHOW(char);
    SHOW(unsigned char);
    SHOW(short);
    SHOW(unsigned short);
    SHOW(signed);
    SHOW(unsigned);
    SHOW(std::ptrdiff_t);
    SHOW(std::size_t);
    SHOW(float);
    SHOW(double);
    SHOW(long double);
}
```


**Output:**
```
<nowiki/>
          bool ( 1 bytes): 0
          char ( 1 bytes): -128 or 0x80
 unsigned char ( 1 bytes): 0
         short ( 2 bytes): -32768 or 0x8000
unsigned short ( 2 bytes): 0
        signed ( 4 bytes): -2147483648 or 0x80000000
      unsigned ( 4 bytes): 0
std::ptrdiff_t ( 8 bytes): -9223372036854775808 or 0x8000000000000000
   std::size_t ( 8 bytes): 0
         float ( 4 bytes): 1.17549e-38 or 0x1p-126
        double ( 8 bytes): 2.22507e-308 or 0x1p-1022
   long double (16 bytes): 3.3621e-4932 or 0x8p-16385
```


## See also


| cpp/types/numeric_limits/dsc lowest | (see dedicated page) |
| cpp/types/numeric_limits/dsc denorm_min | (see dedicated page) |
| cpp/types/numeric_limits/dsc max | (see dedicated page) |

