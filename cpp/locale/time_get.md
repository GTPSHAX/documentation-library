---
title: std::time_get
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_get
---

ddcl|header=locale|1=
template<
class CharT,
class InputIt = std::istreambuf_iterator<CharT>
> class time_get;
Class template `std::time_get` encapsulates date and time parsing rules. The I/O manipulator `std::get_time` uses the `std::time_get` facet of the I/O stream's locale to convert text input to a `std::tm` object.
If a `std::time_get` specialization is not guaranteed to be provided by the standard library (see below), the behaviors of its member functions (except the constructor and destructor) are not guaranteed as specified.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |

In addition, the standard library is also guaranteed to provide every specialization that satisfies the following type requirements:
* `CharT` is one of `char` and `wchar_t`, and
* `InputIt` must meet the requirements of *InputIterator*.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/time_get/dsc date_order | (see dedicated page) |
| cpp/locale/time_get/dsc get_time | (see dedicated page) |
| cpp/locale/time_get/dsc get_date | (see dedicated page) |
| cpp/locale/time_get/dsc get_weekday | (see dedicated page) |
| cpp/locale/time_get/dsc get_monthname | (see dedicated page) |
| cpp/locale/time_get/dsc get_year | (see dedicated page) |
| cpp/locale/time_get/dsc get | (see dedicated page) |


## Protected member functions


| cpp/locale/time_get/dsc do_date_order | (see dedicated page) |
| cpp/locale/time_get/dsc do_get_time | (see dedicated page) |
| cpp/locale/time_get/dsc do_get_date | (see dedicated page) |
| cpp/locale/time_get/dsc do_get_weekday | (see dedicated page) |
| cpp/locale/time_get/dsc do_get_monthname | (see dedicated page) |
| cpp/locale/time_get/dsc do_get_year | (see dedicated page) |
| cpp/locale/time_get/dsc do_get | (see dedicated page) |


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>
#include <sstream>

int main()
{
    std::tm t = {};
    std::istringstream ss("2011-Februar-18 23:12:34");
    ss.imbue(std::locale("de_DE.utf-8"));

    ss >> std::get_time(&t, "%Y-%b-%d %H:%M:%S");
    if (ss.fail())
        std::cout << "Parse failed\n";
    else
        std::cout << std::put_time(&t, "%c") << '\n';
}
```


**Output:**
```
Sun Feb 18 23:12:34 2011
```


## See also


| cpp/locale/dsc time_put | (see dedicated page) |
| cpp/io/manip/dsc get_time | (see dedicated page) |

