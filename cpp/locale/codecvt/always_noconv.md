---
title: std::codecvt::always_noconv
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt/always_noconv
---


```cpp
**Header:** `<`locale`>`
dcl rev multi|num=1|until1=c++11|dcl1=
public:
bool always_noconv() const throw();
|dcl2=
public:
bool always_noconv() const noexcept;
dcl rev multi|num=2|until1=c++11|dcl1=
protected:
virtual bool do_always_noconv() const throw();
|dcl2=
protected:
virtual bool do_always_noconv() const noexcept;
```

1. Public member function, calls the member function `do_always_noconv` of the most derived class.
2. Returns `true` if both `do_in()` and `do_out()` return `std::codecvt_base::noconv` for all valid inputs.

## Return value

`true` if this conversion facet performs no conversions, `false` otherwise.
The non-converting specialization `std::codecvt<char, char, std::mbstate_t>` returns `true`.

## Notes

This function may be used e.g. in the implementation of `std::basic_filebuf::underflow` and `std::basic_filebuf::overflow` to use bulk character copy instead of calling `std::codecvt::in` or `std::codecvt::out` if it is known that the locale imbued in the `std::basic_filebuf` does not perform any conversions.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    std::cout << "The non-converting char<->char codecvt::always_noconv() returns " 
              << std::boolalpha
              << std::use_facet<std::codecvt<char, char, std::mbstate_t>>(
                    std::locale()
                 ).always_noconv() << '\n'
              << "while wchar_t<->char codecvt::always_noconv() returns "
              << std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(
                    std::locale()
                 ).always_noconv() << '\n';
}
```


**Output:**
```
The non-converting char<->char codecvt::always_noconv() returns true
while wchar_t<->char codecvt::always_noconv() returns false
```

