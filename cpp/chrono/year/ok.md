---
title: std::chrono::year::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year/ok
---

ddcl|since=c++20|1=
constexpr bool ok() const noexcept;
Checks if the year value stored in `*this` is in the valid range, i.e., .

## Return value

`true` if the year value stored in `*this` is in the range . Otherwise `false`.

## Possible implementation

See the implementations in
[https://github.com/gcc-mirror/gcc/blob/919858077f4b768c8472f29b977edf0aa6e0f1e5/libstdc%2B%2B-v3/include/std/chrono#L1606 libstdc++],
[https://github.com/llvm-mirror/libcxx/blob/78d6a7767ed57b50122a161b91f59f19c9bd0d19/include/chrono#L1832 libc++],
and Howard Hinnant's
[https://github.com/HowardHinnant/date/blob/0b72599bd43f72d8935e507e25e4f0063f9bb34e/include/date/date.h#L1630 date.h].
eq fun
|1=
class Year
{
short year_;   // exposition-only
public:
bool ok() const noexcept { return year_ != std::numeric_limits<short>::min(); }
/*...*/
};

## Example


### Example

```cpp
#include <chrono>
#include <iomanip>
#include <iostream>

int main()
{
    std::cout << "input year │ internal value │ ok()\n" << std::boolalpha;

    for (const int i : {2020, 0x8000, 0x8001, 0xFFFF, 0x18000})
    {
        const std::chrono::year y{i};
        std::cout << std::setw(10) << i << " │ "
                  << std::setw(14) << static_cast<int>(y) << " │ "
                  << y.ok() << '\n';
    }
}
```


**Output:**
```
input year │ internal value │ ok()
      2020 │           2020 │ true
     32768 │         -32768 │ false
     32769 │         -32767 │ true
     65535 │             -1 │ true
     98304 │         -32768 │ false
```

