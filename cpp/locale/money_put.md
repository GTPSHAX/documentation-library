---
title: std::money_put
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/money_put
---

ddcl|header=locale|1=
template<
class CharT,
class OutputIt = std::ostreambuf_iterator<CharT>
> class money_put;
Class `std::money_put` encapsulates the rules for formatting monetary values as strings. The standard I/O manipulator `std::put_money` uses the `std::money_put` facet of the I/O stream's locale.
If a `std::money_put` specialization is not guaranteed to be provided by the standard library (see below), the behaviors of its `put()` and `do_put()` are not guaranteed as specified.

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


| cpp/locale/money_put/dsc do_put | (see dedicated page) |


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <iterator>
#include <locale>

int main()
{
    // using the I/O manipulator
    std::cout.imbue(std::locale("en_US.UTF-8"));
    std::cout << "American locale: "
              << std::showbase << std::put_money(12345678.9) << '\n';

    // using the facet directly
    std::cout.imbue(std::locale("de_DE.UTF-8"));
    std::cout << "German locale: ";
    auto& f = std::use_facet<std::money_put<char>>(std::cout.getloc());
    f.put({std::cout}, false, std::cout, std::cout.fill(), 12345678.9);
    std::cout << '\n';
}
```


**Output:**
```
American locale: $123,456.79
German locale: 123.456,79 €
```


## Defect reports


## See also


| cpp/locale/dsc moneypunct | (see dedicated page) |
| cpp/locale/dsc money_get | (see dedicated page) |
| cpp/io/manip/dsc put_money | (see dedicated page) |

