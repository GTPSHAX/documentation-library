---
title: std::ctype::is
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/ctype_char/is
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
bool is( mask m, char c ) const;
dcl|num=2|1=
const char* is( const char* low, const char* high, mask* vec ) const;
```

1. Checks if the character `c` is classified by the mask `m` according to the classification table returned by the member function `table()`. Effectively calculates `table()[(unsigned char)c] & m`.
2. For every character in the character array [low, high), reads its full classification mask from the classification table returned by the member function `table()` (that is, evaluates `table()[(unsigned char)*p]` and stores it in the corresponding element of the array pointed to by `vec`.
If `(unsigned char)c >, then an implementation-defined value is substituted instead of `table()[(unsigned char)c]`, possibly different for different values of `c`.

## Parameters


### Parameters

- `c` - character to classify
- `m` - mask to use for classifying a single character
- `low` - pointer to the first character in an array of characters to classify
- `high` - one past the end pointer for the array of characters to classify
- `vec` - pointer to the first element of the array of masks to fill

## Return value

1. `true` if `c` is classified by `m` in `table()`, `false` otherwise.
2. `high`

## Notes

Unlike the primary template `std::ctype`, this specialization does not perform a virtual function call when classifying characters. To customize the behavior, a derived class may provide a non-default classification table to the base class constructor.

## Example


## See also


| cpp/locale/ctype/dsc do_is | (see dedicated page) |

