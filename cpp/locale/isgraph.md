---
title: std::isgraph(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/isgraph
---


# isgraphsmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool isgraph( CharT ch, const locale& loc );
Checks if the given character is classified as a graphic character (i.e. printable, excluding space) by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as graphic, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool isgraph(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::graph, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    const wchar_t c = L'\u2a0c'; // quadruple integral

    std::locale loc1("C");
    std::cout << "isgraph('⨌', C locale) returned "
              << std::boolalpha << std::isgraph(c, loc1) << '\n';

    std::locale loc2("en_US.UTF-8");
    std::cout << "isgraph('⨌', Unicode locale) returned "
              << std::boolalpha << std::isgraph(c, loc2) << '\n';
}
```


**Output:**
```
isgraph('⨌', C locale) returned false
isgraph('⨌', Unicode locale) returned true
```


## See also


| cpp/string/byte/dsc isgraph | (see dedicated page) |
| cpp/string/wide/dsc iswgraph | (see dedicated page) |

