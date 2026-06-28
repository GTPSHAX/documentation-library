---
title: std::ctype<char>
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/ctype_char
---


# ctypesmall|<char>

ddcl|header=locale|
template<>
class ctype<char>;
This specialization of `std::ctype` encapsulates character classification features for type `char`. Unlike general-purpose `std::ctype`, which uses virtual functions, this specialization uses table lookup to classify characters (which is generally faster).
The base class `std::ctype``<char>` implements character classification equivalent to the minimal "C" locale. The classification rules can be extended or modified if constructed with a non-default classification table argument, if constructed as `std::ctype_byname<char>` or as a user-defined derived facet. All `std::istream` formatted input functions are required to use `std::ctype``<char>` for character classing during input parsing.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/locale/ctype_char/dsc constructor | (see dedicated page) |
| cpp/locale/ctype_char/dsc destructor | (see dedicated page) |
| cpp/locale/ctype_char/dsc table | (see dedicated page) |
| cpp/locale/ctype_char/dsc classic_table | (see dedicated page) |
| cpp/locale/ctype_char/dsc is | (see dedicated page) |
| cpp/locale/ctype_char/dsc scan_is | (see dedicated page) |
| cpp/locale/ctype_char/dsc scan_not | (see dedicated page) |
| cpp/locale/ctype/dsc toupper | (see dedicated page) |
| cpp/locale/ctype/dsc tolower | (see dedicated page) |
| cpp/locale/ctype/dsc widen | (see dedicated page) |
| cpp/locale/ctype/dsc narrow | (see dedicated page) |


## Protected member functions


| cpp/locale/ctype/dsc do_toupper | (see dedicated page) |
| cpp/locale/ctype/dsc do_tolower | (see dedicated page) |
| cpp/locale/ctype/dsc do_widen | (see dedicated page) |
| cpp/locale/ctype/dsc do_narrow | (see dedicated page) |


## Example


### Example

```cpp
#include <cstddef>
#include <iostream>
#include <locale>
#include <sstream>
#include <vector>

// This ctype facet classifies commas and endlines as whitespace
struct csv_whitespace : std::ctype<char>
{
    static const mask* make_table()
    {
        // make a copy of the "C" locale table
        static std::vector<mask> v(classic_table(), classic_table() + table_size);
        v[','] {{!
```

v[' '] &= ~space; // space will not be classified as whitespace
return &v[0];
}
csv_whitespace(std::size_t refs = 0) : ctype(make_table(), false, refs) {}
};
int main()
{
std::string in = "Column 1,Column 2,Column 3\n123,456,789";
std::string token;
std::cout << "Default locale:\n";
std::istringstream s1(in);
while (s1 >> token)
std::cout << "  " << token << '\n';
std::cout << "Locale with modified ctype:\n";
std::istringstream s2(in);
s2.imbue(std::locale(s2.getloc(), new csv_whitespace));
while (s2 >> token)
std::cout << "  " << token << '\n';
}
|output=
Default locale:
Column
1,Column
2,Column
3
123,456,789
Locale with modified ctype:
Column 1
Column 2
Column 3
123
456
789

## Defect reports


## See also


| cpp/locale/dsc ctype | (see dedicated page) |
| cpp/locale/dsc ctype_base | (see dedicated page) |
| cpp/locale/dsc ctype_byname | (see dedicated page) |

