---
title: std::basic_ios::fail
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/fail
---


```cpp
dcl | 1=
bool fail() const;
```

Returns `true` if an error has occurred on the associated stream. Specifically, returns `true` if `badbit` or `failbit` is set in `rdstate()`.
See  for the list of conditions that set `failbit` or `badbit`.

## Parameters

(none)

## Return value

`true` if an error has occurred, `false` otherwise.

## Example

