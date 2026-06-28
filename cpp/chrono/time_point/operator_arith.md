---
title: std::chrono::time_point::operators (operator-=)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/operator_arith
---


```cpp
|1=
time_point& operator+=( const duration& d );
|1=
time_point& operator-=( const duration& d );
```

Modifies the time point by the given duration.
1. Applies the offset `d` to `pt`. Effectively, `d` is added to the internally stored duration  as `1=d_ += d`.
2. Applies the offset `d` to `pt` in negative direction. Effectively, `d` is subtracted from internally stored duration  as `1=d_ -= d`.

## Parameters


### Parameters

- `d` - a time offset to apply

## Return value

`*this`

## Example

