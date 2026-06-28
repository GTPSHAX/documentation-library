---
title: cinttypes
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/cinttypes
---



| cpp/header/dsc cstdint | (see dedicated page) |
| cpp/numeric/math/dsc imaxdiv_t | (see dedicated page) |
| cpp/numeric/math/dsc imaxabs | (see dedicated page) |
| cpp/numeric/math/dsc imaxdiv | (see dedicated page) |
| cpp/string/byte/dsc strtoimax | (see dedicated page) |
| cpp/string/wide/dsc wcstoimax | (see dedicated page) |

#### Format constants for the {{lc|std::fprintf


#### Format constants for the {{lc|std::fscanf


## Synopsis


```cpp
#include <cstdint>

#define __STDC_VERSION_INTTYPES_H__ 202311L

namespace std
{
    using imaxdiv_t = /* see description */;

    constexpr intmax_t imaxabs(intmax_t j);
    constexpr imaxdiv_t imaxdiv(intmax_t numer, intmax_t denom);
    intmax_t strtoimax(const char* nptr, char** endptr, int base);
    uintmax_t strtoumax(const char* nptr, char** endptr, int base);
    intmax_t wcstoimax(const wchar_t* nptr, wchar_t** endptr, int base);
    uintmax_t wcstoumax(const wchar_t* nptr, wchar_t** endptr, int base);

    constexpr intmax_t abs(intmax_t);            // optional, see description
    constexpr imaxdiv_t div(intmax_t, intmax_t); // optional, see description
}

#define PRIdN /* see description */
#define PRIiN /* see description */
#define PRIoN /* see description */
#define PRIuN /* see description */
#define PRIxN /* see description */
#define PRIXN /* see description */
#define PRIbN /* see description */
#define PRIBN /* see description */
#define SCNdN /* see description */
#define SCNiN /* see description */
#define SCNoN /* see description */
#define SCNuN /* see description */
#define SCNxN /* see description */
#define SCNbN /* see description */
#define PRIdLEASTN /* see description */
#define PRIiLEASTN /* see description */
#define PRIoLEASTN /* see description */
#define PRIuLEASTN /* see description */
#define PRIxLEASTN /* see description */
#define PRIXLEASTN /* see description */
#define PRIbLEASTN /* see description */
#define PRIBLEASTN /* see description */
#define SCNdLEASTN /* see description */
#define SCNiLEASTN /* see description */
#define SCNoLEASTN /* see description */
#define SCNuLEASTN /* see description */
#define SCNxLEASTN /* see description */
#define SCNbLEASTN /* see description */
#define PRIdFASTN /* see description */
#define PRIiFASTN /* see description */
#define PRIoFASTN /* see description */
#define PRIuFASTN /* see description */
#define PRIxFASTN /* see description */
#define PRIXFASTN /* see description */
#define PRIbFASTN /* see description */
#define PRIBFASTN /* see description */
#define SCNdFASTN /* see description */
#define SCNiFASTN /* see description */
#define SCNoFASTN /* see description */
#define SCNuFASTN /* see description */
#define SCNxFASTN /* see description */
#define SCNbFASTN /* see description */
#define PRIdMAX /* see description */
#define PRIiMAX /* see description */
#define PRIoMAX /* see description */
#define PRIuMAX /* see description */
#define PRIxMAX /* see description */
#define PRIXMAX /* see description */
#define PRIbMAX /* see description */
#define PRIBMAX /* see description */
#define SCNdMAX /* see description */
#define SCNiMAX /* see description */
#define SCNoMAX /* see description */
#define SCNuMAX /* see description */
#define SCNxMAX /* see description */
#define SCNbMAX /* see description */
#define PRIdPTR /* see description */
#define PRIiPTR /* see description */
#define PRIoPTR /* see description */
#define PRIuPTR /* see description */
#define PRIxPTR /* see description */
#define PRIXPTR /* see description */
#define PRIbPTR /* see description */
#define PRIBPTR /* see description */
#define SCNdPTR /* see description */
#define SCNiPTR /* see description */
#define SCNoPTR /* see description */
#define SCNuPTR /* see description */
#define SCNxPTR /* see description */
#define SCNbPTR /* see description */
```

