---
title: std::pointer_traits
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/pointer_traits
---


```cpp
**Header:** `<`memory`>`
dcl|since=c++11|num=1|1=
template< class Ptr >
struct pointer_traits;
dcl|since=c++11|num=2|1=
template< class T >
struct pointer_traits<T*>;
```

The `pointer_traits` class template provides the standardized way to access certain properties of pointer-like types (fancy pointers, such as [https://www.boost.org/doc/libs/release/doc/html/interprocess/offset_ptr.html `boost::interprocess::offset_ptr`]). The standard template `std::allocator_traits` relies on `pointer_traits` to determine the defaults for various typedefs required by *Allocator*.
1. The non-specialized `pointer_traits` conditionally declares the following members:
<div class="t-member">
Let `/*element-type-of*/<Ptr>` be
* `Ptr::element_type` if present;
* otherwise, `T` if `Ptr` is a class template specialization `Template<T, Args...>`, where `Args...` is zero or more type arguments;
* otherwise, not defined.
If `/*element-type-of*/<Ptr>` is not defined, the primary template has no members specified in this page.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member alias templates


| Item | Description |
|------|-------------|
| **Template** | Definition |


## Member functions


| cpp/memory/pointer_traits/dsc pointer_to | (see dedicated page) |

</div>
2. A specialization is provided for pointer types, `T*`, which declares the following members:
<div class="t-member">

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member alias templates


| Item | Description |
|------|-------------|
| **Template** | Definition |


## Member functions


| cpp/memory/pointer_traits/dsc pointer_to | (see dedicated page) |

</div>

## Optional member functions of program-defined specializations


| cpp/memory/pointer_traits/dsc to_address | (see dedicated page) |


## Notes

The rebind member template alias makes it possible, given a pointer-like type that points to `T`, to obtain the same pointer-like type that points to `U`. For example,

```cpp
using another_pointer = std::pointer_traits<std::shared_ptr<int>>::rebind<double>;
static_assert(std::is_same<another_pointer, std::shared_ptr<double>>::value);
```

rrev|since=c++20|
A specialization for user-defined fancy pointer types may provide an additional static member function `to_address` to customize the behavior of `std::to_address`.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

template<class Ptr>
struct BlockList
{
    // Predefine a memory block
    struct block;

    // Define a pointer to a memory block from the kind of pointer Ptr s
    // If Ptr is any kind of T*, block_ptr_t is block*
    // If Ptr is smart_ptr<T>, block_ptr_t is smart_ptr<block>
    using block_ptr_t = typename std::pointer_traits<Ptr>::template rebind<block>;

    struct block
    {
        std::size_t size{};
        block_ptr_t next_block{};
    };

    block_ptr_t free_blocks;
};

int main()
{
    [[maybe_unused]]
    BlockList<int*> bl1;
    // The type of bl1.free_blocks is BlockList<int*>:: block*

    BlockList<std::shared_ptr<char>> bl2;
    // The type of bl2.free_blocks is
    // std::shared_ptr<BlockList<std::shared_ptr<char>>::block>
    std::cout << bl2.free_blocks.use_count() << '\n';
}
```


**Output:**
```
0
```


## Defect reports


## See also


| cpp/memory/dsc allocator_traits | (see dedicated page) |
| cpp/memory/dsc addressof | (see dedicated page) |

