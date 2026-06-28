---
title: cuchar
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/cuchar
---

This header is part of the null-terminated multibyte strings library.


| cpp/string/multibyte/dsc mbstate_t | (see dedicated page) |
| cpp/types/dsc size_t | (see dedicated page) |
| cpp/string/multibyte/dsc mbrtoc16 | (see dedicated page) |
| cpp/string/multibyte/dsc c16rtomb | (see dedicated page) |
| cpp/string/multibyte/dsc mbrtoc32 | (see dedicated page) |
| cpp/string/multibyte/dsc c32rtomb | (see dedicated page) |
| cpp/string/multibyte/dsc mbrtoc8 | (see dedicated page) |
| cpp/string/multibyte/dsc c8rtomb | (see dedicated page) |


## Synopsis


```cpp
#define __STDC_VERSION_UCHAR_H__ 202311L

namespace std {
  using mbstate_t = /* see description */;
  using size_t = /* see description */;

  size_t mbrtoc8(char8_t* pc8, const char* s, size_t n, mbstate_t* ps);
  size_t c8rtomb(char* s, char8_t c8, mbstate_t* ps);
  size_t mbrtoc16(char16_t* pc16, const char* s, size_t n, mbstate_t* ps);
  size_t c16rtomb(char* s, char16_t c16, mbstate_t* ps);
  size_t mbrtoc32(char32_t* pc32, const char* s, size_t n, mbstate_t* ps);
  size_t c32rtomb(char* s, char32_t c32, mbstate_t* ps);
}
```

