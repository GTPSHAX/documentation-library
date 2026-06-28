---
title: clocale
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/clocale
---

This header is part of the text processing library.


| cpp/locale/dsc lconv | (see dedicated page) |
| cpp/types/dsc NULL | (see dedicated page) |
| cpp/locale/dsc LC_categories | (see dedicated page) |
| cpp/locale/dsc setlocale | (see dedicated page) |
| cpp/locale/dsc localeconv | (see dedicated page) |


## Synopsis


```cpp
namespace std {
  struct lconv;

  char* setlocale(int category, const char* locale);
  lconv* localeconv();
}

#define NULL        /* see description */
#define LC_ALL      /* see description */
#define LC_COLLATE  /* see description */
#define LC_CTYPE    /* see description */
#define LC_MONETARY /* see description */
#define LC_NUMERIC  /* see description */
#define LC_TIME     /* see description */
```


## Notes

* `NULL` is also defined in the following headers:
**
**
**
**
**
