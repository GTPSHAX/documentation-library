---
title: std::hash<std::coroutine_handle>
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/hash
---


# hashsmall|<std::coroutine_handle>

ddcl|header=coroutine|since=c++20|
template< class Promise >
struct hash<std::coroutine_handle<Promise>>;
The template specialization of `std::hash` for `std::coroutine_handle` allows users to obtain hashes of objects of type `std::coroutine_handle<P>`.
`operator()` of the specialization is noexcept.

## Example

