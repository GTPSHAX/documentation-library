---
title: std::num_put
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/num_put
---


```cpp
**Header:** `<`locale`>`
dcl|1=
template<
class CharT,
class OutputIt = std::ostreambuf_iterator<CharT>
> class num_put;
```

Class `std::num_put` encapsulates the rules for formatting numeric values as strings. Specifically, the types `bool`, `long`, `unsigned long`<sup>(since C++11)</sup> , `long long`, `unsigned long long`, `double`, `long double`, `void*`, and of all types implicitly convertible to these (such as `int` or `float`) are supported. The standard formatting output operators (such as `cout << n;`) use the `std::num_put` facet of the I/O stream's locale to generate text representation of numbers.
If a `std::num_put` specialization is not guaranteed to be provided by the standard library (see below), the behaviors of its `put()` and `do_put()` are not guaranteed as specified.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |

In addition, the standard library is also guaranteed to provide every specialization that satisfies the following type requirements:
* `CharT` is one of
** `char`,
** `wchar_t`, and
** any other implementation-defined character container type that meets the requirements for a character on which any of the iostream components can be instantiated; and
* `OutputIt` must meet the requirements of *OutputIterator*.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


## Protected member functions


## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <locale>
#include <string>

int main()
{
    double n = 1234567.89;
    std::cout.imbue(std::locale("de_DE.UTF-8"));
    std::cout << "Direct conversion to string:\n"
              << std::to_string(n) << '\n'
              << "Output using a german locale:\n"
              << std::fixed << n << '\n'
              << "Output using an american locale:\n";

    // use the facet directly
    std::cout.imbue(std::locale("en_US.UTF-8"));
    auto& f = std::use_facet<std::num_put<char>>(std::cout.getloc());
    f.put(std::ostreambuf_iterator<char>(std::cout), std::cout, ' ', n);
    std::cout << '\n';
}
```


**Output:**
```
Direct conversion to string:
1234567.890000
Output using a german locale:
1.234.567,890000
Output using an american locale:
1,234,567.890000
```


## Defect reports


## See also


| cpp/locale/dsc numpunct | (see dedicated page) |
| cpp/locale/dsc num_get | (see dedicated page) |
| cpp/string/basic_string/dsc to_string | (see dedicated page) |
| cpp/string/basic_string/dsc to_wstring | (see dedicated page) |

