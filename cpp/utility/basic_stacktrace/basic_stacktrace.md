---
title: std::basic_stacktrace::basic_stacktrace
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/basic_stacktrace
---


```cpp
dcl|num=1|since=c++23|
basic_stacktrace() noexcept(/* see below */);
dcl|num=2|since=c++23|
explicit basic_stacktrace( const allocator_type& alloc ) noexcept;
dcl|num=3|since=c++23|
basic_stacktrace( const basic_stacktrace& other );
dcla|num=4|since=c++23|
basic_stacktrace( basic_stacktrace&& other ) noexcept;
dcl|num=5|since=c++23|
basic_stacktrace( const basic_stacktrace& other,
const allocator_type& alloc );
dcl|num=6|since=c++23|
basic_stacktrace( basic_stacktrace&& other, const allocator_type& alloc );
```

Constructs an empty `basic_stacktrace`, or copy/move from `other`.
1. Default constructor. Constructs an empty `basic_stacktrace` with a default-constructed allocator.
2. Constructs an empty `basic_stacktrace` using `alloc` as the allocator.
3. Copy constructor. Constructs a `basic_stacktrace` with the copy of the contents of `other`, the allocator is obtained as if by calling `std::allocator_traits<allocator_type>::select_on_container_copy_construction(other.get_allocator())`.
4. Move constructor. Constructs a `basic_stacktrace` with the contents of `other` using move semantics. Allocator is move-constructed from that of `other`. After construction, `other` is left in a valid but unspecified state.
5. Same as the copy constructor, except that `alloc` is used as the allocator.
6. Behaves same as the move constructor if `1=alloc == other.get_allocator()`. Otherwise, allocates memory with `alloc` and performs element-wise move. `alloc` is used as the allocator.
may throw an exception or construct an empty `basic_stacktrace` on allocation failure.

## Parameters


### Parameters

- `alloc` - allocator to use for all memory allocations of the constructed `basic_stacktrace`
- `other` - another `basic_stacktrace` to copy/move from

## Exceptions

1.
@3,5,6@ May propagate the exception thrown on allocation failure.

## Complexity

@1,2@ Constant.
3. Linear in size of `other`.
4. Constant.
5. Linear in size of `other`.
6. Linear in size of `other` if `1=alloc != other.get_allocator()`, otherwise constant.

## Notes


## Example

