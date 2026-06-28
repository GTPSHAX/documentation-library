---
title: std::basic_stacktrace
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace
---


```cpp
**Header:** `<`stacktrace`>`
dcl|num=1|since=c++23|
template< class Allocator >
class basic_stacktrace;
dcl|num=2|since=c++23|1=
using stacktrace =
std::basic_stacktrace<std::allocator<std::stacktrace_entry>>;
dcl|num=3|since=c++23|1=
namespace pmr {
using stacktrace =
std::basic_stacktrace<std::pmr::polymorphic_allocator<std::stacktrace_entry>>;
}
```

1. The `basic_stacktrace` class template represents a snapshot of the whole stacktrace or its given part. It satisfies the requirement of *AllocatorAwareContainer*, *SequenceContainer*, and *ReversibleContainer*, except that only move, assignment, swap, and operations for const-qualified sequence containers are supported, and the semantics of comparison functions are different from those required for a container.
2. Convenience type alias for the `basic_stacktrace` using the default `std::allocator`.
3. Convenience type alias for the `basic_stacktrace` using the .
The ''invocation sequence'' of the current evaluation mathjax-or|\(\small{ {x}_{0} }\)|x<sub>0</sub> in the current thread of execution is a sequence mathjax-or|\(\small{ ({x}_{0}, \dots, {x}_{n})}\)|(x<sub>0</sub>, ..., x<sub>n</sub>) of evaluations such that, for }, mathjax-or|\(\small{ {x}_{i} }\)|x<sub>i</sub> is within the function invocation mathjax-or|\(\small{ {x}_{i+1} }\)|x<sub>i+1</sub>.
A ''stacktrace'' is an approximate representation of an invocation sequence and consists of stacktrace entries.
A ''stacktrace entry'' represents an evaluation in a stacktrace. It is represented by `std::stacktrace_entry` in the C++ standard library.

## Template parameters


### Parameters

- `Allocator` - An allocator that is used to acquire/release memory and to construct/destroy the elements in that memory. The type must meet the requirements of *Allocator*. The program is ill-formed if `Allocator::value_type` is not `std::stacktrace_entry`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/utility/basic_stacktrace/dsc constructor | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc destructor | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc operator{{= | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc current | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc get_allocator | (see dedicated page) |

#### Iterators

| cpp/utility/basic_stacktrace/dsc begin | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc end | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc rbegin | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc rend | (see dedicated page) |

#### Capacity

| cpp/utility/basic_stacktrace/dsc empty | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc size | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc max_size | (see dedicated page) |

#### Element access

| cpp/utility/basic_stacktrace/dsc operator at | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc at | (see dedicated page) |

#### Modifiers

| cpp/utility/basic_stacktrace/dsc swap | (see dedicated page) |


## Non-member functions


| cpp/utility/basic_stacktrace/operator cmp|title=operator==<br>operator<=>|notes= | |
| cpp/utility/basic_stacktrace/dsc swap2 | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc to_string | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/utility/basic_stacktrace/dsc hash | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc formatter | (see dedicated page) |


## Notes

Support for custom allocators is provided for using `basic_stacktrace` on a hot path or in embedded environments. Users can allocate `stacktrace_entry` objects on the stack or in some other place, where appropriate.
The sequence of `std::stacktrace_entry` objects owned by a `std::basic_stacktrace` is immutable, and either is empty or represents a contiguous interval of the whole stacktrace.
(available in [https://www.boost.org/doc/libs/release/doc/html/stacktrace.html Boost.Stacktrace]) can be used instead when `std::basic_stacktrace` is not available.

## Example


### Example

```cpp
#include <iostream>
#include <stacktrace>

int nested_func(int c)
{
    std::cout << std::stacktrace::current() << '\n';
    return c + 1;
}

int func(int b)
{
    return nested_func(b + 1);
}

int main()
{
    std::cout << func(777);
}
```


**Output:**
```
// msvc output (the lines ending with '⤶' arrows are split to fit the width):
0> C:\Users\ContainerAdministrator\AppData\Local\Temp\compiler-explorer-compiler20221122-⤶
31624-2ja1sf.8ytzw\example.cpp(6): output_s!nested_func+0x1F
1> C:\Users\ContainerAdministrator\AppData\Local\Temp\compiler-explorer-compiler20221122-⤶
31624-2ja1sf.8ytzw\example.cpp(12): output_s!func+0x15
2> C:\Users\ContainerAdministrator\AppData\Local\Temp\compiler-explorer-compiler20221122-⤶
31624-2ja1sf.8ytzw\example.cpp(15): output_s!main+0xE
3> D:\a\_work\1\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl(288): output_s!⤶
__scrt_common_main_seh+0x10C
4> KERNEL32!BaseThreadInitThunk+0x14
5> ntdll!RtlUserThreadStart+0x21
779

gcc output:
   0# nested_func(int) at /app/example.cpp:7
   1# func(int) at /app/example.cpp:13
   2#      at /app/example.cpp:18
   3#      at :0
   4#      at :0
   5# 

779
```


## See also


| cpp/utility/dsc stacktrace_entry | (see dedicated page) |

