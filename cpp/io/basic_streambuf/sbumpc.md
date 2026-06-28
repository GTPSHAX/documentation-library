---
title: std::basic_streambuf::stossc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/sbumpc
---


```cpp
dcl | num=1 |
int_type sbumpc();
dcl | num=2 | deprecated=c++98 | removed=c++17 |
void stossc();
```

Reads one character and advances the input sequence by one character.
1. If the input sequence read position is not available, returns `uflow()`. Otherwise returns `Traits::to_int_type(*gptr())`.
2. Same as , but discards the result.

## Parameters

(none)

## Return value

1. The value of the character pointed to by the ''get pointer'', or `Traits::eof()` if the read position is not available.

## Example


## See also

