---
title: keyword: alignas
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/alignas
---


## Usage

* `alignas` specifier

## Example


```cpp
struct s1 final {};
struct alignas(2) s2 final {};

static_assert(alignof(s1) == 1);
static_assert(alignof(s2) == 2);
```


## See also

* `alignof`
