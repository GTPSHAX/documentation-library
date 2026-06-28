---
title: std::raw_storage_iterator::operators (int)
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/raw_storage_iterator/operator_arith
---


```cpp
dcl|1=
raw_storage_iterator& operator++();
dcl|1=
raw_storage_iterator operator++( int );
```

Advances the iterator.
1. Pre-increment. Returns the updated iterator.
2. Post-increment. Returns the old value of the iterator.

## Parameters

(none)

## Return value

1. `*this`
2. The old value of the iterator.
