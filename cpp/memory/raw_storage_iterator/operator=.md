---
title: std::raw_storage_iterator::operator=
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/raw_storage_iterator/operator=
---


```cpp
dcl|num=1|1=
raw_storage_iterator& operator=( const T& el );
dcl|num=2|since=c++17|1=
raw_storage_iterator& operator=( T&& el );
```

1. Constructs a value at the location the iterator points to from `el`.
2. Constructs a value at the location the iterator points to from `std::move(el)`.

## Parameters


### Parameters

- `el` - the value to copy or move from

## Return value

`*this`
