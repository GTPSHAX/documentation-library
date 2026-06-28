---
title: std::regex_traits::isctype
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_traits/isctype
---

ddcl|
bool isctype( CharT c, char_class_type f ) const;
Determines whether the character `c` belongs to the character class identified by `f`, which, in turn, is a value returned by `lookup_classname()` or a bitwise OR of several such values.
The version of this function provided in the standard library specializations of `std::regex_traits` does the following:
1. First converts `f` to a value `m` of type `std::ctype_base::mask`.
@@ For each `std::ctype` category listed in the table in the page `lookup_classname()`, if the bits in `f` corresponding to the category are set, the corresponding bits in `m` will also be set.
2. Then attempts to classify the character in the imbued locale by calling `std::use_facet<std::ctype<CharT>>(getloc()).is(m, c)`.
* If that returns `true`, `isctype()` will also return `true`.
* Otherwise, if `c` equals `'_'`, and `f` includes the result of calling `lookup_classname()` for the character class `[:w:]`, `true` is returned, otherwise `false` is returned.

## Parameters


### Parameters

- `c` - the character to classify
- `f` - the bitmask obtained from one or several calls to `lookup_classname()`

## Return value

`true` if `c` is classified by `f`, `false` otherwise.

## Example


### Example

```cpp
#include <iostream>
#include <regex>
#include <string>

int main()
{
    std::regex_traits<char> t;
    std::string str_alnum = "alnum";
    auto a = t.lookup_classname(str_alnum.begin(), str_alnum.end());
    std::string str_w = "w"; // [:w:] is [:alnum:] plus '_'
    auto w = t.lookup_classname(str_w.begin(), str_w.end());
    std::cout << std::boolalpha
              << t.isctype('A', w) << ' ' << t.isctype('A', a) << '\n'
              << t.isctype('_', w) << ' ' << t.isctype('_', a) << '\n'
              << t.isctype(' ', w) << ' ' << t.isctype(' ', a) << '\n';
}
```


**Output:**
```
true true
true false
false false
```


## Defect reports


## See also


| cpp/regex/regex_traits/dsc lookup_classname | (see dedicated page) |
| cpp/locale/ctype/dsc do_is | (see dedicated page) |
| cpp/string/wide/dsc iswctype | (see dedicated page) |

