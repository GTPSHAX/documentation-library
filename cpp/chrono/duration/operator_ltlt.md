---
title: std::chrono::operator<<
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template<
class CharT,
class Traits,
class Rep,
class Period
> std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::duration<Rep, Period>& d );
Inserts a textual representation of `d` into `os`.
Behaves as if it was implemented as

```cpp
std::basic_ostringstream<CharT, Traits> s;
s.flags(os.flags());
s.imbue(os.getloc());
s.precision(os.precision());
s << d.count() << units_suffix; // see below
return os << s.str();
```

In other words, the stream flags, locale, and precision are determined by the stream, but any padding are determined using the entire output string.
The `units_suffix` is determined based on `Period::type` according to the following table.


| Item | Description |
|------|-------------|
| **{{tt** | Period::type |

For the last two rows of the table,  and  in the suffix are `Period::type::num` and `Period::type::den` formatted as a decimal number with no leading zeroes, respectively.

## Return value

A reference to the stream, i.e., `os`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono_literals;

int main()
{
    constexpr auto duration = 123ms;
    std::cout << duration << '\n';
}
```


**Output:**
```
123ms
```


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|duration | (see dedicated page) |
| cpp/string/basic_string/dsc operator ltltgtgt | (see dedicated page) |
| cpp/string/basic_string/dsc to_string | (see dedicated page) |
| cpp/string/basic_string/dsc to_wstring | (see dedicated page) |

