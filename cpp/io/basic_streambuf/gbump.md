---
title: std::basic_streambuf::gbump
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/gbump
---

ddcl|1=
protected:
void gbump( int count );
Skips `count` characters in the get area. This is done by adding `count` to the ''get pointer''. No checks are done for underflow.

## Parameters


### Parameters

- `count` - number of characters to skip

## Return value

(none)

## Notes

Because this function takes an `int`, it cannot manipulate buffers larger than `std::numeric_limits<int>::max()` characters ().

## Example


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc pbump | (see dedicated page) |

