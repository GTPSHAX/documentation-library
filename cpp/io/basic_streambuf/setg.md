---
title: std::basic_streambuf::setg
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/setg
---

ddcl|1=
protected:
void setg( char_type* gbeg, char_type* gcurr, char_type* gend );
Sets the values of the pointers defining the get area.
After the call, `1=eback() == gbeg`, `1=gptr() == gcurr` and `1=egptr() == gend` are all `true`.
If any of [gbeg, gend), [gbeg, gcurr) and [gcurr, gend) is not a valid range, the behavior is undefined.

## Parameters


### Parameters

- `gbeg` - pointer to the new beginning of the get area
- `gcurr` - pointer to the new current character (''get pointer'') in the get area
- `gend` - pointer to the new end of the get area

## Example


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc setp | (see dedicated page) |

