---
title: std::codecvt::unshift
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt/unshift
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
result unshift( StateT& state, ExternT* to, ExternT* to_end,
ExternT*& to_next ) const;
dcl|num=2|1=
protected:
virtual result do_unshift( StateT& state, ExternT* to, ExternT* to_end,
ExternT*& to_next ) const;
```

1. Public member function, calls the member function `do_unshift` of the most derived class.
2. If the encoding represented by this `codecvt` facet is state-dependent, and `state` represents a conversion state that is not the initial shift state, writes the characters necessary to return to the initial shift state. The characters are written to a character array whose first element is pointed to by `to`. No more than `to_end - to` characters are written. The parameter `to_next` is updated to point one past the last character written.

## Return value

A value of type `std::codecvt_base::result`, indicating the success status as follows:

## Notes

This function is called by `std::basic_filebuf::close()` and in other situations when finalizing a state-dependent multibyte character sequence.

## Example


## Defect reports


## See also


| cpp/string/multibyte/dsc wcrtomb | (see dedicated page) |
| cpp/locale/codecvt/dsc do_out | (see dedicated page) |

