---
title: std::codecvt::max_length
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt/max_length
---


```cpp
**Header:** `<`locale`>`
dcl rev multi|num=1|until1=c++11|dcl1=
public:
int max_length() const throw();
|dcl2=
public:
int max_length() const noexcept;
dcl rev multi|num=2|until1=c++11|dcl1=
protected:
virtual int do_max_length() const throw();
|dcl2=
protected:
virtual int do_max_length() const noexcept;
```

1. Public member function, calls the member function `do_max_length` of the most derived class.
2. Returns the maximum value that `do_length(state, from, from_end, 1)` can return for any valid range [from, from_end) and any valid `state`.

## Return value

The maximum number of `ExternT` characters that could be consumed if converted by `in()` to produce one `InternT` character.
The non-converting specialization `std::codecvt<char, char, std::mbstate_t>` returns `1`.

## Notes

If the encoding is state-dependent (`1=encoding() == -1`), then more than `max_length()` external characters may be consumed to produce one internal character.

## Example


### Example

```cpp
#include <codecvt>
#include <iostream>
#include <locale>

int main()
{
    std::cout << "In codecvt_utf8, the longest multibyte character is "
              << std::codecvt_utf8<wchar_t>().max_length() << " bytes long\n";

    std::cout << "In header-consuming codecvt_utf8, the longest multibyte character is "
              << std::codecvt_utf8<wchar_t,
                                   0x10ffff,
                                   std::consume_header>().max_length() << " bytes long\n";

    std::cout << "In this system's en_US.utf8, the longest multibyte character is "
              << std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(
                     std::locale("en_US.utf8")
                 ).max_length() << " bytes long\n";

    std::cout << "In this system's zh_CN.gb18030, the longest multibyte character is "
              << std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(
                     std::locale("zh_CN.gb18030")
                 ).max_length() << " bytes long\n";
}
```


**Output:**
```
In codecvt_utf8, the longest multibyte character is 4 bytes long
In header-consuming codecvt_utf8, the longest multibyte character is 7 bytes long
In this system's en_US.utf8, the longest multibyte character is 6 bytes long
In this system's zh_CN.gb18030, the longest multibyte character is 4 bytes long
```


## See also


| cpp/string/multibyte/dsc MB_CUR_MAX | (see dedicated page) |
| cpp/locale/codecvt/dsc do_encoding | (see dedicated page) |

