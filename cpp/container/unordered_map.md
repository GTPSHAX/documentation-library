---
title: std::unordered_map
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_map
---


```cpp
**Header:** `<`unordered_map`>`
dcl|num=1|since=c++11|1=
template<
class Key,
class T,
class Hash = std::hash<Key>,
class KeyEqual = std::equal_to<Key>,
class Allocator = std::allocator<std::pair<const Key, T>>
> class unordered_map;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class T,
class Hash = std::hash<Key>,
class KeyEqual = std::equal_to<Key>
> using unordered_map =
std::unordered_map<Key, T, Hash, KeyEqual,
std::pmr::polymorphic_allocator<std::pair<const Key, T>>>;
}
```

`std::unordered_map` is an associative container that contains key-value pairs with unique keys. Search, insertion, and removal of elements have average constant-time complexity.
Internally, the elements are not sorted in any particular order, but organized into buckets. Which bucket an element is placed into depends entirely on the hash of its key. Keys with the same hash code appear in the same bucket. This allows fast access to individual elements, since once the hash is computed, it refers to the bucket containing the element.
Two keys are considered ''equivalent'' if the map's key equality predicate returns true when passed those keys. If two keys are equivalent, the hash function must return the same value for both keys.
`std::unordered_map` meets the requirements of *Container*, *AllocatorAwareContainer*, *UnorderedAssociativeContainer*.

## Iterator invalidation


| Operations |
| Invalidated |
| - |
| All read only operations, lc | swap, lc | std::swap |
| Never |
| - |
| lc | clear, lc | rehash, lc | reserve, lc | 1=operator= |
| Always |
| - |
| lc | insert, lc | emplace, lc | emplace_hint, lc | operator[] |
| Only if causes rehash |
| - |
| lc | erase |
| Only to the element erased |


### Notes

* The swap functions do not invalidate any of the iterators inside the container, but they do invalidate the iterator marking the end of the swap region.
* References and pointers to either key or data stored in the container are only invalidated by erasing that element, even when the corresponding iterator is invalidated.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|unordered_map | (see dedicated page) |
| cpp/container/dsc mapped_type|unordered_map | (see dedicated page) |
| cpp/container/dsc value_type|unordered_map | (see dedicated page) |
| cpp/container/dsc size_type|unordered_map | (see dedicated page) |
| cpp/container/dsc difference_type|unordered_map | (see dedicated page) |
| cpp/container/dsc hasher|unordered_map | (see dedicated page) |
| cpp/container/dsc key_equal|unordered_map | (see dedicated page) |
| cpp/container/dsc allocator_type|unordered_map | (see dedicated page) |
| cpp/container/dsc reference|unordered_map | (see dedicated page) |
| cpp/container/dsc const_reference|unordered_map | (see dedicated page) |
| cpp/container/dsc pointer|unordered_map | (see dedicated page) |
| cpp/container/dsc const_pointer|unordered_map | (see dedicated page) |
| cpp/container/dsc iterator|unordered_map | (see dedicated page) |
| cpp/container/dsc const_iterator|unordered_map | (see dedicated page) |
| cpp/container/dsc local_iterator|unordered_map | (see dedicated page) |
| cpp/container/dsc const_local_iterator|unordered_map | (see dedicated page) |
| cpp/container/dsc node_type|unordered_map | (see dedicated page) |
| cpp/container/dsc insert_return_type|unordered_map | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|unordered_map | (see dedicated page) |
| cpp/container/dsc destructor|unordered_map | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|unordered_map | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|unordered_map | (see dedicated page) |
| cpp/container/dsc end|unordered_map | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|unordered_map | (see dedicated page) |
| cpp/container/dsc size|unordered_map | (see dedicated page) |
| cpp/container/dsc max_size|unordered_map | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|unordered_map | (see dedicated page) |
| cpp/container/dsc insert|unordered_map | (see dedicated page) |
| cpp/container/dsc insert_range|unordered_map | (see dedicated page) |
| cpp/container/dsc insert_or_assign|unordered_map | (see dedicated page) |
| cpp/container/dsc emplace|unordered_map | (see dedicated page) |
| cpp/container/dsc emplace_hint|unordered_map | (see dedicated page) |
| cpp/container/dsc try_emplace|unordered_map | (see dedicated page) |
| cpp/container/dsc erase|unordered_map | (see dedicated page) |
| cpp/container/dsc swap|unordered_map | (see dedicated page) |
| cpp/container/dsc extract|unordered_map | (see dedicated page) |
| cpp/container/dsc merge|unordered_map | (see dedicated page) |

#### Lookup

| cpp/container/dsc at|unordered_map | (see dedicated page) |
| cpp/container/dsc operator_at|unordered_map | (see dedicated page) |
| cpp/container/dsc count|unordered_map | (see dedicated page) |
| cpp/container/dsc find|unordered_map | (see dedicated page) |
| cpp/container/dsc contains|unordered_map | (see dedicated page) |
| cpp/container/dsc equal_range|unordered_map | (see dedicated page) |

#### Bucket interface

| cpp/container/dsc begin(int)|unordered_map | (see dedicated page) |
| cpp/container/dsc end(int)|unordered_map | (see dedicated page) |
| cpp/container/dsc bucket_count|unordered_map | (see dedicated page) |
| cpp/container/dsc max_bucket_count|unordered_map | (see dedicated page) |
| cpp/container/dsc bucket_size|unordered_map | (see dedicated page) |
| cpp/container/dsc bucket|unordered_map | (see dedicated page) |

#### Hash policy

| cpp/container/dsc load_factor|unordered_map | (see dedicated page) |
| cpp/container/dsc max_load_factor|unordered_map | (see dedicated page) |
| cpp/container/dsc rehash|unordered_map | (see dedicated page) |
| cpp/container/dsc reserve|unordered_map | (see dedicated page) |

#### Observers

| cpp/container/dsc hash_function|unordered_map | (see dedicated page) |
| cpp/container/dsc key_eq|unordered_map | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp_unord|unordered_map | (see dedicated page) |
| cpp/container/dsc swap2|unordered_map | (see dedicated page) |
| cpp/container/dsc erase_if|unordered_map | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_unordered_map` | 202502L | C++26 | Constexpr `std::unordered_map` |


## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int main()
{
    // Create an unordered_map of three strings (that map to strings)
    std::unordered_map<std::string, std::string> u =
    {
        {"RED", "#FF0000"},
        {"GREEN", "#00FF00"},
        {"BLUE", "#0000FF"}
    };

    // Helper lambda function to print key-value pairs
    auto print_key_value = [](const auto& key, const auto& value)
    {
        std::cout << "Key:[" << key << "] Value:[" << value << "]\n";
    };

    std::cout << "Iterate and print key-value pairs of unordered_map, being\n"
                 "explicit with their types:\n";
    for (const std::pair<const std::string, std::string>& n : u)
        print_key_value(n.first, n.second);

    std::cout << "\nIterate and print key-value pairs using C++17 structured binding:\n";
    for (const auto& [key, value] : u)
        print_key_value(key, value);

    // Add two new entries to the unordered_map
    u["BLACK"] = "#000000";
    u["WHITE"] = "#FFFFFF";

    std::cout << "\nOutput values by key:\n"
                 "The HEX of color RED is:[" << u["RED"] << "]\n"
                 "The HEX of color BLACK is:[" << u["BLACK"] << "]\n\n";

    std::cout << "Use operator[] with non-existent key to insert a new key-value pair:\n";
    print_key_value("new_key", u["new_key"]);

    std::cout << "\nIterate and print key-value pairs, using `auto`;\n"
                 "new_key is now one of the keys in the map:\n";
    for (const auto& n : u)
        print_key_value(n.first, n.second);
}
```


**Output:**
```
Iterate and print key-value pairs of unordered_map, being
explicit with their types:
Key:[BLUE] Value:[#0000FF]
Key:[GREEN] Value:[#00FF00]
Key:[RED] Value:[#FF0000]

Iterate and print key-value pairs using C++17 structured binding:
Key:[BLUE] Value:[#0000FF]
Key:[GREEN] Value:[#00FF00]
Key:[RED] Value:[#FF0000]

Output values by key:
The HEX of color RED is:[#FF0000]
The HEX of color BLACK is:[#000000]

Use operator[] with non-existent key to insert a new key-value pair:
Key:[new_key] Value:[]

Iterate and print key-value pairs, using `auto`;
new_key is now one of the keys in the map:
Key:[new_key] Value:[]
Key:[WHITE] Value:[#FFFFFF]
Key:[BLACK] Value:[#000000]
Key:[BLUE] Value:[#0000FF]
Key:[GREEN] Value:[#00FF00]
Key:[RED] Value:[#FF0000]
```


## Defect reports


## See also


| cpp/container/dsc unordered_multimap | (see dedicated page) |
| cpp/container/dsc map | (see dedicated page) |
| cpp/container/dsc flat_map | (see dedicated page) |

