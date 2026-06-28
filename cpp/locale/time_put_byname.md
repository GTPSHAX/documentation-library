---
title: std::time_put_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_put_byname
---

ddcl|header=locale|1=
template<
class CharT,
class OutputIt = std::ostreambuf_iterator<CharT>
> class time_put_byname : public std::time_put<CharT, OutputIt>
`std::time_put_byname` is a `std::time_put` facet which encapsulates time and date formatting rules of the locale specified at its construction.

## Specializations

The standard library is guaranteed to provide every specialization that satisfies the following type requirements:
* `CharT` is one of `char` and `wchar_t`, and
* `OutputIt` must meet the requirements of *OutputIterator*.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/byname/dsc constructor|time_put_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|time_put_byname | (see dedicated page) |


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

    out.imbue(std::locale(out.getloc(),
                          new std::time_put_byname<wchar_t>("ja_JP.utf8")));
    out << std::put_time(std::localtime(&t), L"%A %c") << '\n';

    out.imbue(std::locale(out.getloc(),
                          new std::time_put_byname<wchar_t>("ru_RU.utf8")));
    out << std::put_time(std::localtime(&t), L"%A %c") << '\n';

    out.imbue(std::locale(out.getloc(),
                          new std::time_put_byname<wchar_t>("sv_SE.utf8")));
    out << std::put_time(std::localtime(&t), L"%A %c") << '\n';
}
```


**Output:**
```
木曜日 2023年10月05日 19時44分51秒
Четверг Чт 05 окт 2023 19:44:51
torsdag tor  5 okt 2023 19:44:51
```


## See also


| cpp/locale/dsc time_put | (see dedicated page) |

