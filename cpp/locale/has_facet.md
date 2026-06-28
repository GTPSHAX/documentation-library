---
title: std::has_facet
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/has_facet
---


```cpp
**Header:** `<`locale`>`
dcl rev multi|until1=c++11
|dcl1=
template< class Facet >
bool has_facet( const locale& loc ) throw();
|dcl2=
template< class Facet >
bool has_facet( const locale& loc ) noexcept;
```

Checks if the locale `loc` implements the facet `Facet`.
The program is ill-formed if Facet is not a `facet` or it is a volatile-qualified facet.

## Parameters


### Parameters

- `loc` - the locale object to query

## Return value

Returns `true` if the facet `Facet` was installed in the locale `loc`, `false` otherwise.

## Notes

`std::has_facet` must return `true` for all locales `loc` if `Facet` is one of the standard facets given `here`.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

// minimal custom facet
struct myfacet : public std::locale::facet
{
    static std::locale::id id;
};

std::locale::id myfacet::id;

int main()
{
    // loc is a "C" locale with myfacet added
    std::locale loc(std::locale::classic(), new myfacet);
    std::cout << std::boolalpha
              << "Can loc classify chars? "
              << std::has_facet<std::ctype<char>>(loc) << '\n'
              << "Can loc classify char32_t? "
              << std::has_facet<std::ctype<char32_t>>(loc) << '\n'
              << "Does loc implement myfacet? "
              << std::has_facet<myfacet>(loc) << '\n';
}
```


**Output:**
```
Can loc classify chars? true
Can loc classify char32_t? false
Does loc implement myfacet? true
```


## Defect reports


## See also


| cpp/locale/dsc locale | (see dedicated page) |
| cpp/locale/dsc use_facet | (see dedicated page) |

