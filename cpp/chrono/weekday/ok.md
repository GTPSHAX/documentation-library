---
title: std::chrono::weekday::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday/ok
---

ddcl|since=c++20|
constexpr bool ok() const noexcept;
Checks if the weekday value stored in `*this` is in the valid range, i.e., .

## Return value

`true` if the weekday value stored in `*this` is in the range . Otherwise `false`.

## Example


### Example

```cpp
#include <chrono>
#include <iomanip>
#include <iostream>
#include <locale>
#include <string>

struct weekday_ok : std::numpunct<char>
{
    std::string do_truename()  const override { return " (is valid weekday)"; }
    std::string do_falsename() const override { return " (is not valid weekday)"; }
};

int main()
{
    std::cout.imbue(std::locale(std::cout.getloc(), new weekday_ok));
    std::cout << std::boolalpha;

    for (const unsigned u : {0 /* Sun */, 1 /* Mon */, 6, 7 /* Sun */, 8, 9})
    {
        const std::chrono::weekday wd{u};
        std::cout << "u: " << u << "; wd: " << wd.c_encoding() << wd.ok() << '\n';
    }
}
```


**Output:**
```
u: 0; wd: 0 (is valid weekday)
u: 1; wd: 1 (is valid weekday)
u: 6; wd: 6 (is valid weekday)
u: 7; wd: 0 (is valid weekday)
u: 8; wd: 8 (is not valid weekday)
u: 9; wd: 9 (is not valid weekday)
```


## See also


| cpp/chrono/weekday/dsc encoding | (see dedicated page) |

