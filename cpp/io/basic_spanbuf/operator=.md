---
title: std::basic_spanbuf::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/operator=
---


```cpp
dcl|num=1|since=c++23|1=
basic_spanbuf& operator=( basic_spanbuf&& rhs );
dcl|num=2|since=c++23|1=
basic_spanbuf& operator( const basic_spanbuf& ) = delete;
```

1. Move assignment operator. Equivalent to }. After move assignment, `*this` holds the state `rhs` held before move assignment. It is implementation-defined whether `rhs` still hold the underlying buffer after move assignment.
2. The copy assignment operator is deleted; `basic_spanbuf` is not *CopyAssignable*.

## Parameters


### Parameters

- `rhs` - another `basic_spanbuf` that will be moved from

## Return value

`*this`

## Example

