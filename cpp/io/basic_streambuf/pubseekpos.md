---
title: std::basic_streambuf::seekpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/pubseekpos
---


```cpp
dcl|num=1|1=
pos_type pubseekpos( pos_type pos,
std::ios_base::openmode which = std::ios_base::in | std::ios_base::out );
dcl|num=2|1=
protected:
virtual pos_type seekpos( pos_type pos,
std::ios_base::openmode which = std::ios_base::in | std::ios_base::out );
```

Sets the position indicator of the input and/or output sequence to an absolute position.
1. Calls `seekpos(pos, which)` of the most derived class.
2. The base class version of this function has no effect. The derived classes may override this function to allow absolute positioning of the position indicator.

## Parameters


### Parameters

- `pos` - absolute position to set the position indicator to
- `which` - defines which of the input and/or output sequences to affect. It can be one or a combination of the following constants:

## Return value

1. The return value of `seekpos(pos, which)`.
2. The resulting absolute position as defined by the position indicator. The base class version returns `pos_type(off_type(-1))`.

## Example


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc pubseekoff | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekpos | (see dedicated page) |
| cpp/io/strstreambuf/dsc seekpos | (see dedicated page) |

