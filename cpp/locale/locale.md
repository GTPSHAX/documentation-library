---
title: std::locale
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/locale
---

ddcl|header=locale|
class locale;
An object of class `std::locale` is an immutable indexed set of immutable facets. Each stream object of the C++ input/output library is associated with an `std::locale` object and uses its facets for parsing and formatting of all data. <sup>(since C++11)</sup> In addition, a locale object is associated with each `std::basic_regex` object. Locale objects can also be used as predicates that perform string collation with the standard containers and algorithms and can be accessed directly to obtain or modify the facets they hold.
Each locale constructed in a C++ program holds at least the following standard facets (i.e. `std::has_facet` returns `true` for all these facet types), but a program may define additional specializations or completely new facets and add them to any existing locale object.


| -style="text-align:center; font-size:16px; line-height:16px;" |
| colspan=2 | Supported facetsanchor | Supported_facets |
| - |
| c/core | std::ctype<char><br>c/core | std::ctype<wchar_t> |
| c/core | std::codecvt<char, char, std::mbstate_t><br>c/core | std::codecvt<wchar_t, char, std::mbstate_t> |
| - |
| c/core | std::num_get<char><br>c/core | std::num_get<wchar_t> |
| rowspan=2 | c/core | std::numpunct<char><br>c/core | std::numpunct<wchar_t> |
| - |
| c/core | std::num_put<char><br>c/core | std::num_put<wchar_t> |
| - |
| c/core | std::money_get<char><br>c/core | std::money_get<wchar_t> |
| rowspan=2 | c/core | std::moneypunct<char><br>c/core | std::moneypunct<char, true><br>c/core | std::moneypunct<wchar_t><br>c/core | std::moneypunct<wchar_t, true> |
| - |
| c/core | std::money_put<char><br>c/core | std::money_put<wchar_t> |
| - |
| c/core | std::time_get<char><br>c/core | std::time_get<wchar_t> |
| c/core | std::collate<char><br>c/core | std::collate<wchar_t> |
| - |
| c/core | std::time_put<char><br>c/core | std::time_put<wchar_t> |
| c/core | std::messages<char><br>c/core | std::messages<wchar_t> |
| -style="text-align:center" |
| colspan=2 | Deprecated facetsanchor | Deprecated facets |
| - |
| colspan=2 | c/core | std::codecvt<char16_t, char, std::mbstate_t> mark life | since=c++11 | deprecated=c++20<br>c/core | std::codecvt<char32_t, char, std::mbstate_t> mark life | since=c++11 | deprecated=c++20<br> |

Internally, a locale object is implemented as if it is a reference-counted pointer to an array (indexed by `std::locale::id`) of reference-counted pointers to facets: copying a locale only copies one pointer and increments several reference counts. To maintain the standard C++ library thread safety guarantees (operations on different objects are always thread-safe), both the locale reference count and each facet reference count are updated in a thread-safe manner, similar to `std::shared_ptr`.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Description |
| cpp/locale/locale/dsc id | (see dedicated page) |
| cpp/locale/locale/dsc facet | (see dedicated page) |
| nolink=true|category|`int` | |


## Member constants


| Item | Description |
|------|-------------|
| **Name** | Explanation |

`std::locale` member functions expecting a `category` argument require one of the category values defined above, or the union of two or more such values. The ``LC` constants` are not accepted.

## Member functions


| cpp/locale/locale/dsc locale | (see dedicated page) |
| cpp/locale/locale/dsc ~locale | (see dedicated page) |
| cpp/locale/locale/dsc operator{{= | (see dedicated page) |
| cpp/locale/locale/dsc combine | (see dedicated page) |
| cpp/locale/locale/dsc name | (see dedicated page) |
| cpp/locale/locale/dsc encoding | (see dedicated page) |
| cpp/locale/locale/dsc operator cmp | (see dedicated page) |
| cpp/locale/locale/dsc operator() | (see dedicated page) |
| cpp/locale/locale/dsc global | (see dedicated page) |
| cpp/locale/locale/dsc classic | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    std::wcout << L"User-preferred locale setting is "
               << std::locale("").name().c_str() << L'\n';
    // on startup, the global locale is the "C" locale
    std::wcout << 1000.01 << L'\n';

    // replace the C++ global locale and the "C" locale with the user-preferred locale
    std::locale::global(std::locale(""));
    // use the new global locale for future wide character output
    std::wcout.imbue(std::locale());

    // output the same number again
    std::wcout << 1000.01 << L'\n';
}
```


**Output:**
```
User-preferred locale setting is en_US.UTF8
1000.01
1,000.01
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-340 | C++98 | the set of standard facets that all locales need to hold was unclear | made clear |


## See also


| cpp/text/dsc text_encoding | (see dedicated page) |
| cpp/locale/dsc use_facet | (see dedicated page) |
| cpp/locale/dsc has_facet | (see dedicated page) |
| cpp/io/ios_base/dsc imbue | (see dedicated page) |
| cpp/io/ios_base/dsc getloc | (see dedicated page) |

