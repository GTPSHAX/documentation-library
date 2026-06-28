---
title: std::time_put
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_put
---

ddcl|header=locale|1=
template<
class CharT,
class OutputIt = std::ostreambuf_iterator<CharT>
> class time_put;
Class template `std::time_put` encapsulates date and time formatting rules. The I/O manipulator `std::put_time` uses the `std::time_put` facet of the I/O stream's locale to generate text representation of an `std::tm` object.
If a `std::time_put` specialization is not guaranteed to be provided by the standard library (see below), the behaviors of its `put()` and `do_put()` are not guaranteed as specified.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |

In addition, the standard library is also guaranteed to provide every specialization that satisfies the following type requirements:
* `CharT` is one of `char` and `wchar_t`, and
* `OutputIt` must meet the requirements of *OutputIterator*.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/time_put/dsc constructor | (see dedicated page) |
| cpp/locale/time_put/dsc destructor | (see dedicated page) |
| cpp/locale/time_put/dsc put | (see dedicated page) |


## Protected member functions


| cpp/locale/time_put/dsc do_put | (see dedicated page) |


## Example


### Example

```cpp
#include <codecvt>
#include <ctime>
#include <iomanip>
#include <iostream>

int main()
{
    std::time_t t = std::time(nullptr);
    std::wbuffer_convert<std::codecvt_utf8<wchar_t>> conv(std::cout.rdbuf());
    std::wostream out(&conv);
    out.imbue(std::locale("ja_JP.utf8"));

    // this I/O manipulator std::put_time uses std::time_put<wchar_t>
    out << std::put_time(std::localtime(&t), L"%A %c") << '\n';
}
```


**Output:**
```
水曜日 2011年11月09日 12時32分05秒
```


## See also


| cpp/locale/dsc time_put_byname | (see dedicated page) |
| cpp/locale/dsc time_get | (see dedicated page) |
| cpp/io/manip/dsc put_time | (see dedicated page) |

