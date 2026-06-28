---
title: std::basic_stacktrace::current
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/current
---


```cpp
dcl|num=1|since=c++23|1=
static basic_stacktrace current( const allocator_type& alloc =
allocator_type() ) noexcept;
dcl|num=2|since=c++23|1=
static basic_stacktrace current( size_type skip, const allocator_type& alloc =
allocator_type() ) noexcept;
dcl|num=3|since=c++23|1=
static basic_stacktrace current( size_type skip, size_type max_depth,
const allocator_type& alloc =
allocator_type() ) noexcept;
```

Let `s[i]` (0 ≤ `''i''` < `''n''`) denote the (`''i''+1`)-th stacktrace entry in the stacktrace of the current evaluation in the current thread of execution, where `''n''` is the count of the stacktrace entries in the stackentry.
1. Attempts to create a `basic_stacktrace` consisting of `s[0]`, `s[1]`, ..., `s[n - 1]`.
2. Attempts to create a `basic_stacktrace` consisting of `s[m]`, `s[m + 1]`, ..., `s[n - 1]`, where `''m''` is `min(skip, ''n'')`.
3. Attempts to create a `basic_stacktrace` consisting of `s[m]`, `s[m + 1]`, ..., `s[o - 1]`, where `''m''` is `min(skip, ''n'')` and `''o''` is `min(skip + max_depth, ''n'')`.
@@
In all cases, `alloc` is stored into the created `basic_stacktrace` and used to allocate the storage for stacktrace entries.

## Parameters


### Parameters

- `alloc` - allocator to use for all memory allocations of the constructed `basic_stacktrace` 
- `skip` - the number of stacktrace entries to skip
- `max_depth` - the maximum depth of the stacktrace entries

## Return value

If the allocation succeeds, the `basic_stacktrace` described above.
Otherwise, an empty `basic_stacktrace`.

## Example

