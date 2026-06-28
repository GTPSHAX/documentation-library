---
title: std::match_results::match_results
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/match_results
---


```cpp
dcl|num=1|
match_results() : match_results(Allocator()) {}
dcl|num=2|
explicit match_results( const Allocator& a );
dcl|num=3|
match_results( const match_results& rhs );
dcl|num=4|
match_results( const match_results& rhs, const Allocator& a );
dcl|num=5|
match_results( match_results&& rhs ) noexcept;
dcl|num=6|
match_results( match_results&& rhs, const Allocator& a );
```

@1,2@ Constructs a match result with no established result state.
:@1@ The default constructor.
:@2@ Constructs the match result using a copy of `a` as the allocator.
@@ When the construction finishes,  returns `false` and  returns `0`.
@3-6@ Constructs a match result from `rhs`.
:@3@ The copy constructor.
:@4@ Constructs the match result using a copy of `a` as the allocator.
:@5@ The move constructor. When the construction finishes, `rhs` is in a valid but unspecified state.
:@6@ Constructs the match result using a copy of `a` as the allocator. When the construction finishes, `rhs` is in a valid but unspecified state.
@@ Given the value of `rhs` before the construction as `m` and any integer in [0, m.size()) as `n`, when the construction finishes, the following member functions should return the specified values:


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

- `a` - allocator to use for all memory allocations of this container
- `rhs` - another `match_results` to use as source to initialize the `match_results` with

## Exceptions

@1-4@
6. Throws nothing if `1=a == rhs.get_allocator()` is `true`.

## Example


## Defect reports

