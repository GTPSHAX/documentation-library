---
title: std::strcoll
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strcoll
---

ddcl|header=cstring|
int strcoll( const char* lhs, const char* rhs );
Compares two null-terminated byte strings according to the current locale as defined by the `LC_COLLATE` category.

## Parameters


### Parameters

- `lhs, rhs` - pointers to the null-terminated byte strings to compare

## Return value

* Negative value if `lhs` is ''less than'' (precedes) `rhs`.
* `0` if `lhs` is ''equal to'' `rhs`.
* Positive value if `lhs` is ''greater than'' (follows) `rhs`.

## Notes


## Example


### Example

```cpp
#include <clocale>
#include <cstring>
#include <iostream>

int main()
{
    std::setlocale(LC_COLLATE, "cs_CZ.utf8");
    // Alternatively, ISO-8859-2 (a.k.a. Latin-2)
    // may also work on some OS:
    // std::setlocale(LC_COLLATE, "cs_CZ.iso88592");

    const char* s1 = "hrnec";
    const char* s2 = "chrt";

    std::cout << "In the Czech locale: ";
    if (std::strcoll(s1, s2) < 0)
        std::cout << s1 << " before " << s2 << '\n';
    else
        std::cout << s2 << " before " << s1 << '\n';

    std::cout << "In lexicographical comparison: ";
    if (std::strcmp(s1, s2) < 0)
        std::cout << s1 << " before " << s2 << '\n';
    else
        std::cout << s2 << " before " << s1 << '\n';
}
```


**Output:**
```
In the Czech locale: hrnec before chrt
In lexicographical comparison: chrt before hrnec
```


## See also


| cpp/string/wide/dsc wcscoll | (see dedicated page) |
| cpp/locale/collate/dsc do_compare | (see dedicated page) |
| cpp/string/byte/dsc strxfrm | (see dedicated page) |

