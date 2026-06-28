---
title: std::basic_istream::gcount
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/gcount
---


```cpp
dcl |
std::streamsize gcount() const;
```

Returns the number of characters extracted by the last unformatted input operation, or the maximum representable value of `std::streamsize` if the number is not representable.
The following member functions of `basic_istream` change the value of subsequent `gcount()` calls:
* `move constructor`
* `swap()`
* `get()`
* `getline()`
* `ignore()`
* `read()`
* `readsome()`
* `operator>>|operator>>(basic_streambuf*)`
The following functions set `gcount()` to zero:
* `constructor`
* `putback()`
* `unget()`
* `peek()`

## Parameters

(none)

## Return value

The number of characters extracted by the last unformatted input operation, or the maximum representable value of `std::streamsize` if the number is not representable.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3464 | C++98 | the return value was unspecified when the result overflows | returns the maximum value |

