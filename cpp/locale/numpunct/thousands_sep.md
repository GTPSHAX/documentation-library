---
title: std::numpunct::thousands_sep
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/numpunct/thousands_sep
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
char_type thousands_sep() const;
dcl|num=2|1=
protected:
virtual char_type do_thousands_sep() const;
```

1. Public member function, calls the member function `do_thousands_sep` of the most derived class.
2. Returns the character to be used as the separator between digit groups when parsing or formatting integers and integral parts of floating-point values.

## Return value

The object of type `char_type` to use as the thousands separator. The standard specializations of `std::numpunct` return `','` and `L','`.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

struct space_out : std::numpunct<char>
{
    char do_thousands_sep()   const { return ' '; }  // separate with spaces
    std::string do_grouping() const { return "\1"; } // groups of 1 digit
};

int main()
{
    std::cout << "default locale: " << 12345678 << '\n';
    std::cout.imbue(std::locale(std::cout.getloc(), new space_out));
    std::cout << "locale with modified numpunct: " << 12345678 << '\n';
}
```


**Output:**
```
default locale: 12345678
locale with modified numpunct: 1 2 3 4 5 6 7 8
```


## Defect reports


## See also


| cpp/locale/numpunct/dsc do_grouping | (see dedicated page) |

