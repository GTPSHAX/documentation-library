---
title: std::basic_ios::bad
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/bad
---


```cpp
dcl|1=
bool bad() const;
```

Returns `true` if non-recoverable error has occurred on the associated stream. Specifically, returns `true` if `cpp/io/ios_base/iostate|badbit` is set in `rdstate()`.
See  for the list of conditions that set `badbit`.

## Parameters

(none)

## Return value

`true` if a non-recoverable error has occurred, `false` otherwise.

## Example

