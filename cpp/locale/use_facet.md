---
title: std::use_facet
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/use_facet
---

ddcl|header=locale|
template< class Facet >
const Facet& use_facet( const std::locale& loc );
Obtains a reference to a facet implemented by `loc`.
The program is ill-formed if Facet is not a `facet` whose definition contains the public static member **`id`** or it is a volatile-qualified facet.

## Parameters


### Parameters

- `loc` - the locale object to query

## Return value

Returns a reference to the facet. The reference returned by this function is valid as long as any `std::locale` object refers to that facet.

## Exceptions

`std::bad_cast` if `1=std::has_facet<Facet>(loc) == false`.

## Notes

A `std::locale` object should not be a temporary if a reference to the `Facet` object obtained from `use_facet` is used after the end of statement:

```cpp
// BAD:
auto& f = std::use_facet<std::moneypunct<char, true>>(std::locale{"no_NO.UTF-8"});
foo(f.curr_symbol()); // Error: f internally uses a dangling reference
                      // to a std::locale object that no longer exists.
// GOOD:
auto loc = std::locale{"is_IS.UTF-8"}; // OK: a non-temporary object
auto& f = std::use_facet<std::moneypunct<char, true>>(loc);
foo(f.curr_symbol()); // OK: f internally uses a reference to existing locale object.
```


## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    for (const char* name: {"en_US.UTF-8", "de_DE.UTF-8", "en_GB.UTF-8"})
        std::cout << "Your currency string is "
                  << std::use_facet<std::moneypunct<char, true>>(std::locale{name}).
                     curr_symbol() << '\n';
}
```


**Output:**
```
Your currency string is USD
Your currency string is EUR
Your currency string is GBP
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-31 | C++98 | the returned reference remained usable<br>as long as the locale value itself exists | the returned reference remains usable as<br>long as some locale object refers to that facet |


## See also


| cpp/locale/dsc locale | (see dedicated page) |
| cpp/locale/dsc has_facet | (see dedicated page) |

