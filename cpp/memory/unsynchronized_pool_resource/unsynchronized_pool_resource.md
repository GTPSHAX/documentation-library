---
title: std::pmr::unsynchronized_pool_resource::unsynchronized_pool_resource
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/unsynchronized_pool_resource/unsynchronized_pool_resource
---


```cpp
dcl|since=c++17|num=1|1=
unsynchronized_pool_resource();
dcl|since=c++17|num=2|1=
explicit unsynchronized_pool_resource( std::pmr::memory_resource* upstream );
dcl|since=c++17|num=3|1=
explicit unsynchronized_pool_resource( const std::pmr::pool_options& opts );
dcl|since=c++17|num=4|1=
unsynchronized_pool_resource( const std::pmr::pool_options& opts,
std::pmr::memory_resource* upstream );
dcl|since=c++17|num=5|1=
unsynchronized_pool_resource( const unsynchronized_pool_resource& ) = delete;
```

Constructs an `unsynchronized_pool_resource`.
@1-4@ Constructs an `unsynchronized_pool_resource` using the specified upstream memory resource and tuned according to the specified options. The resulting object holds a copy of `upstream` but does not own the resource to which `upstream` points.<br/>
The overloads not taking `opts` as a parameter uses a default constructed instance of `cpp/memory/pool_options` as the options. The overloads not taking `upstream` as a parameter use the return value of `std::pmr::get_default_resource()` as the upstream memory resource.
5. Copy constructor is deleted.

## Parameters


### Parameters

- `opts` - a `std::pmr::pool_options` struct containing the constructor options
- `upstream` - the upstream memory resource to use

## Exceptions

@1-4@ Throws only if a call to the `allocate()` function of the upstream resource throws. It is unspecified if or under what conditions such a call takes place.
