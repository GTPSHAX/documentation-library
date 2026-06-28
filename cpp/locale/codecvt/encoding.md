---
title: std::codecvt::encoding
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt/encoding
---


```cpp
**Header:** `<`locale`>`
dcl rev multi|num=1|until1=c++11|dcl1=
public:
int encoding() const throw();
|dcl2=
public:
int encoding() const noexcept;
dcl rev multi|num=2|until1=c++11|dcl1=
protected:
virtual int do_encoding() const throw();
|dcl2=
protected:
virtual int do_encoding() const noexcept;
```

1. Public member function, calls the member function `do_encoding` of the most derived class.
2. If the encoding represented by this codecvt facet maps each internal character to the same, constant number of external characters, returns that number. If the encoding is variable-length (e.g. UTF-8 or UTF-16), returns `0`. If the encoding is state-dependent, returns `-1`.

## Return value

The exact number of `externT` characters that correspond to one `internT` character, if constant. `0` if the number varies, `-1` if the encoding is state-dependent.
The non-converting specialization `std::codecvt<char, char, std::mbstate_t>` returns `1`.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    std::cout << "en_US.utf8 is a variable-length encoding, encoding() returns "
              << std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(
                     std::locale("en_US.utf8")
                 ).encoding() << '\n';

    std::cout << "zh_CN.gb18030 is also variable-length, encoding() == "
              << std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(
                     std::locale("zh_CN.gb18030")
                 ).encoding() << '\n';

    std::cout << "ru_RU.koi8r is a single-byte encoding, encoding() == "
              << std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(
                     std::locale("ru_RU.koi8r")
                 ).encoding() << '\n';
}
```


**Output:**
```
en_US.utf8 is a variable-length encoding, encoding() returns 0
zh_CN.gb18030 is also variable-length, encoding() == 0
ru_RU.koi8r is a single-byte encoding, encoding() == 1
```


## See also


| cpp/string/multibyte/dsc MB_CUR_MAX | (see dedicated page) |
| cpp/locale/codecvt/dsc do_max_length | (see dedicated page) |

