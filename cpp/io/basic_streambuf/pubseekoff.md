---
title: std::basic_streambuf::seekoff
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/pubseekoff
---


```cpp
dcl|num=1|1=
pos_type pubseekoff( off_type off, std::ios_base::seekdir dir,
std::ios_base::openmode which = ios_base::in | ios_base::out );
dcl|num=2|1=
protected:
virtual pos_type seekoff( off_type off, std::ios_base::seekdir dir,
std::ios_base::openmode which = ios_base::in | ios_base::out );
```

Sets the position indicator of the input and/or output sequence relative to some other position.
1. Calls `seekoff(off, dir, which)` of the most derived class.
2. The base class version of this function has no effect. The derived classes may override this function to allow relative positioning of the position indicator.

## Parameters


### Parameters

- `off` - relative position to set the position indicator to.
- `dir` - defines base position to apply the relative offset to. It can be one of the following constants:
- `which` - defines which of the input and/or output sequences to affect. It can be one or a combination of the following constants:

## Note

Not all combinations of parameters may be valid, see the derived versions of `seekoff` for details.

## Return value

1. The return value of `seekoff(off, dir, which)`
2. The resulting absolute position as defined by the position indicator. The base class version returns `pos_type(off_type(-1))`.

## Example


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc pubseekpos | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekoff | (see dedicated page) |
| cpp/io/strstreambuf/dsc seekoff | (see dedicated page) |

