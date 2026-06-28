---
title: std::match_results::operator=
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/operator=
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|1=
match_results& operator=( const match_results& other );
dcl|num=2|1=
match_results& operator=( match_results&& other ) noexcept;
```

Assigns the contents.
1. Copy assignment operator. Assigns the contents of `other`.
2. Move assignment operator. Assigns the contents of `other` using move semantics. `other` is in a valid, but unspecified state after the operation.
Given the value of `other` before the assignment as `m` and any integer in [0, m.size()) as `n`, when the assignment finishes, the following member functions should return the specified values:


| Member function |
| Value |
| - |
| rlpf | ready |
| c | m.ready() |
| - |
| rlpf | size |
| c | m.size() |
| - |
| rlpf | str | args=n |
| c | m.str(n) |
| - |
| rlpf | prefix |
| c | m.prefix() |
| - |
| rlpf | suffix |
| c | m.suffix() |
| - |
| rlpf | operator at | operator[] | args=n |
| c | m[n] |
| - |
| rlpf | length | args=n |
| c | m.length(n) |
| - |
| rlpf | position | args=n |
| c | m.position(n) |


## Parameters


### Parameters

- `other` - another match results object

## Return value

`*this`

## Exceptions

1.

## Defect reports

