---
title: Freestanding and hosted implementations
type: Utilities
source: https://en.cppreference.com/w/cpp/freestanding
---


# Freestanding and hosted implementations

There are two kinds of implementations defined by the C++ standard: '''''hosted''''' and '''''freestanding''''' implementations. For ''hosted'' implementations, the set of standard library headers required by the C++ standard is much larger than for ''freestanding'' ones. In a ''freestanding'' implementation, execution may happen without an operating system.
The kind of the implementation is implementation-defined.<sup>(since C++11)</sup>  The predefined macro `__STDC_HOSTED__` is expanded to `1` for hosted implementations and `0` for freestanding implementations.
rrev|since=c++11|1=

## Requirements on multi-threaded executions and data races

cellpadding=8 |
! ''freestanding'' !! ''hosted''
|-
| Under a ''freestanding'' implementation, it is implementation-defined whether a program can have more than one thread of execution.
| Under a ''hosted'' implementation, a C++ program can have more than one  running concurrently.

## Requirements on the `cpp/language/main function|main` function


| - |
| ''freestanding'' !! ''hosted'' |
| - |
| In a ''freestanding'' implementation, it is implementation-defined whether a program is required to define a ltt | cpp/language/main function | main function. Start-up and termination is implementation-defined; start-up contains the execution of lt | cpp/language/constructors for objects of lsd | cpp/language/scope#Namespace scope with static storage duration; termination contains the execution of lt | cpp/language/destructors for objects with static lt | cpp/language/storage duration. |
| In a ''hosted'' implementation, a program must contain a global function called ltt | cpp/language/main function | main. Executing a program starts a main [[cpp/thread | thread of execution]] in which the tt | main function is invoked, and in which variables of static lt | cpp/language/storage duration might be initialized and destroyed. |


## Requirements on standard library headers

A ''freestanding'' implementation has an implementation-defined set of headers. This set includes at least the headers in the following table.
For partially freestanding headers, freestanding implementations only needs to provide part of the entities in the corresponding synopsis:
* If an entity is commented `// freestanding`, it is guaranteed to be provided.
rrev|since=c++26|
* If an entity (function or function template) is commented `// freestanding-deleted`, it is guaranteed to be either provided or deleted.
* If an entity is declared in a header whose synopsis begins with `all freestanding` or `// mostly freestanding`, it is guaranteed to be provided if the entity itself is not commented.

### Headers required for a freestanding implementation

<div style="max-height: 80vh; overflow-y: auto;">


| - |
| Library |
| Component |
| Headers |
| Freestanding |
| - |
| rowspan=13 | ls | cpp/utility#Language support |
| Common definitions |
| header | cstddef |
| yes | All |
| - |
| C standard library |
| header | cstdlib |
| maybe | Partial |
| - |
| Implementation properties |
| header | cfloat<br>header | climits <sup>(C++11)</sup><br>header | limits<br>header | version <sup>(C++20)</sup> |
| yes | All |
| - |
| Integer types |
| header | cstdint <sup>(C++11)</sup> |
| yes | All |
| - |
| Dynamic memory management |
| header | new |
| yes | All |
| - |
| Type identification |
| header | typeinfo |
| yes | All |
| - |
| Source location |
| header | source_location <sup>(C++20)</sup> |
| yes | All |
| - |
| Exception handling |
| header | exception |
| yes | All |
| - |
| Initializer lists |
| header | initializer_list <sup>(C++11)</sup> |
| yes | All |
| - |
| Comparisons |
| header | compare <sup>(C++20)</sup> |
| yes | All |
| - |
| Coroutines support |
| header | coroutine <sup>(C++20)</sup> |
| yes | All |
| - |
| Other runtime support |
| header | cstdarg |
| yes | All |
| - |
| Debugging support |
| header | debugging <sup>(C++26)</sup> |
| yes | All |
| - |
| colspan=2 | [[cpp/concepts | Concepts]] |
| header | concepts <sup>(C++20)</sup> |
| yes | All |
| - |
| rowspan=2 | [[cpp/error | Diagnostics]] |
| Error numbers |
| header | cerrno <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| System error support |
| header | system_error <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| [[cpp/memory | Memory management]] |
| Memory |
| header | memory <sup>(C++23)</sup> |
| maybe | Partial |
| - |
| rowspan=2 | [[cpp/meta | Metaprogramming]] |
| Type traits |
| header | type_traits <sup>(C++11)</sup> |
| yes | All |
| - |
| Compile-time rational arithmetic |
| header | ratio <sup>(C++23)</sup> |
| yes | All |
| - |
| rowspan=5 | [[cpp/utility#General-purpose utilities | General utilities]] |
| Utility components |
| header | utility <sup>(C++23)</sup> |
| yes | All |
| - |
| Tuples |
| header | tuple <sup>(C++23)</sup> |
| yes | All |
| - |
| Function objects |
| header | functional <sup>(C++20)</sup> |
| maybe | Partial |
| - |
| Primitive numeric conversions |
| header | charconv <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| Bit manipulation |
| header | bit <sup>(C++20)</sup> |
| yes | All |
| - |
| rowspan=2 | [[cpp/string | Strings]] |
| String classes |
| header | string <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| Null-terminated<br>sequence utilities |
| header | cstring <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| [[cpp/text | Text processing]] |
| Null-terminated<br>sequence utilities |
| header | cwchar <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| colspan=2 | [[cpp/iterator | Iterators]] |
| header | iterator <sup>(C++23)</sup> |
| maybe | Partial |
| - |
| colspan=2 | [[cpp/ranges | Ranges]] |
| header | ranges <sup>(C++23)</sup> |
| maybe | Partial |
| - |
| rowspan=2 | [[cpp/numeric | Numerics]] |
| Mathematical functions<br>for floating-point types |
| header | cmath <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| Random number generation |
| header | random <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| [[cpp/thread | Concurrency support]] |
| Atomics |
| header | atomic <sup>(C++11)</sup> |
| yes | nbsp | 4All<ref>rev inl | since=c++20 | Support for always lock-free integral atomic types and presence of type aliases lc | std::atomic_signed_lock_free and lc | std::atomic_unsigned_lock_free are implementation-defined in a freestanding implementation.</ref> |
| - |
| colspan=2 | [[cpp/execution | Execution control]] |
| header | execution <sup>(C++26)</sup> |
| maybe | Partial |
| - |
| colspan=2 | '''Deprecated''' headers |
| header | ciso646 <sup>(until C++20)</sup><br>header | cstdalign mark life | since=c++11 | until=c++20<br>header | cstdbool mark life | since=c++11 | until=c++20 |
| yes | All |

</div>

## Notes

Some compiler vendors may not fully support freestanding implementation. For example, GCC libstdc++ has had implementation and build issues before version 13, while LLVM libcxx and MSVC STL do not support freestanding.
In C++23, many features are made freestanding with partial headers. However, it is still up for discussion in WG21 whether some headers will be made freestanding in the future standards. Regardless, containers like `std::vector|vector`, `std::list|list`, `std::deque|deque`, and `std::map|map` will never be freestanding due to their dependencies on exceptions and heap.
GCC 13 provides more headers, such as , , , and , for freestanding, although these headers may not be portable or provide the same capabilities as a hosted implementation. It is better to avoid using them in a freestanding environment, even if the toolchain provides them.

## References


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1938 | C++98 | an implementation did not need<br>to document whether it is hosted | made the implementation kind implementation-<br>defined (thus requires a documentation) |


## See also

