---
title: std::map
type: Containers
source: https://en.cppreference.com/w/cpp/container/map
---


```cpp
**Header:** `<`map`>`
dcl|num=1|1=
template<
class Key,
class T,
class Compare = std::less<Key>,
class Allocator = std::allocator<std::pair<const Key, T>>
> class map;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class T,
class Compare = std::less<Key>
> using map = std::map<Key, T, Compare,
std::pmr::polymorphic_allocator<std::pair<const Key, T>>>;
}
```

`std::map` is a sorted associative container that contains key-value pairs with unique keys. Keys are sorted by using the comparison function `Compare`. Search, removal, and insertion operations have logarithmic complexity. Maps are usually implemented as [Red–black tree](https://en.wikipedia.org/wiki/Red–black tree)s.
Iterators of `std::map` iterate in ascending order of keys, where ascending is defined by the comparison that was used for construction. That is, given
* `m`, a `std::map`
* `it_l` and `it_r`, dereferenceable iterators to `m`, with `it_l < it_r`.
`1=m.value_comp()(*it_l, *it_r) == true` (least to greatest if using the default comparison).
Everywhere the standard library uses the *Compare* requirements, uniqueness is determined by using the equivalence relation. In imprecise terms, two objects `a` and `b` are considered equivalent (not unique) if neither compares less than the other: `!comp(a, b) && !comp(b, a)`.
`std::map` meets the requirements of *Container*, *AllocatorAwareContainer*, *AssociativeContainer* and *ReversibleContainer*.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|map | (see dedicated page) |
| cpp/container/dsc mapped_type|map | (see dedicated page) |
| cpp/container/dsc value_type|map | (see dedicated page) |
| cpp/container/dsc size_type|map | (see dedicated page) |
| cpp/container/dsc difference_type|map | (see dedicated page) |
| cpp/container/dsc key_compare|map | (see dedicated page) |
| cpp/container/dsc allocator_type|map | (see dedicated page) |
| cpp/container/dsc reference|map | (see dedicated page) |
| cpp/container/dsc const_reference|map | (see dedicated page) |
| cpp/container/dsc pointer|map | (see dedicated page) |
| cpp/container/dsc const_pointer|map | (see dedicated page) |
| cpp/container/dsc iterator|map | (see dedicated page) |
| cpp/container/dsc const_iterator|map | (see dedicated page) |
| cpp/container/dsc reverse_iterator|map | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|map | (see dedicated page) |
| cpp/container/dsc node_type|map | (see dedicated page) |
| cpp/container/dsc insert_return_type|map | (see dedicated page) |


## Member classes


| cpp/container/dsc value_compare|map | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|map | (see dedicated page) |
| cpp/container/dsc destructor|map | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|map | (see dedicated page) |

#### Element access

| cpp/container/dsc at|map | (see dedicated page) |
| cpp/container/dsc operator_at|map | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|map | (see dedicated page) |
| cpp/container/dsc end|map | (see dedicated page) |
| cpp/container/dsc rbegin|map | (see dedicated page) |
| cpp/container/dsc rend|map | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|map | (see dedicated page) |
| cpp/container/dsc size|map | (see dedicated page) |
| cpp/container/dsc max_size|map | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|map | (see dedicated page) |
| cpp/container/dsc insert|map | (see dedicated page) |
| cpp/container/dsc insert_range|map | (see dedicated page) |
| cpp/container/dsc insert_or_assign|map | (see dedicated page) |
| cpp/container/dsc emplace|map | (see dedicated page) |
| cpp/container/dsc emplace_hint|map | (see dedicated page) |
| cpp/container/dsc try_emplace|map | (see dedicated page) |
| cpp/container/dsc erase|map | (see dedicated page) |
| cpp/container/dsc swap|map | (see dedicated page) |
| cpp/container/dsc extract|map | (see dedicated page) |
| cpp/container/dsc merge|map | (see dedicated page) |

#### Lookup

| cpp/container/dsc count|map | (see dedicated page) |
| cpp/container/dsc find|map | (see dedicated page) |
| cpp/container/dsc contains|map | (see dedicated page) |
| cpp/container/dsc equal_range|map | (see dedicated page) |
| cpp/container/dsc lower_bound|map | (see dedicated page) |
| cpp/container/dsc upper_bound|map | (see dedicated page) |

#### Observers

| cpp/container/dsc key_comp|map | (see dedicated page) |
| cpp/container/dsc value_comp|map | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|map | (see dedicated page) |
| cpp/container/dsc swap2|map | (see dedicated page) |
| cpp/container/dsc erase_if|map | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_map` | 202502L | C++26 | Constexpr `std::map` |


## Example


### Example

```cpp
#include <iostream>
#include <map>
#include <string>
#include <string_view>

void print_map(std::string_view comment, const std::map<std::string, int>& m)
{
    std::cout << comment;
    // Iterate using C++17 facilities
    for (const auto& [key, value] : m)
        std::cout << '[' << key << "] = " << value << "; ";

// C++11 alternative:
//  for (const auto& n : m)
//      std::cout << n.first << " = " << n.second << "; ";
//
// C++98 alternative:
//  for (std::map<std::string, int>::const_iterator it = m.begin(); it != m.end(); ++it)
//      std::cout << it->first << " = " << it->second << "; ";

    std::cout << '\n';
}

int main()
{
    // Create a map of three (string, int) pairs
    std::map<std::string, int> m{<!---->{"CPU", 10}, {"GPU", 15}, {"RAM", 20}<!---->};

    print_map("1) Initial map: ", m);

    m["CPU"] = 25; // update an existing value
    m["SSD"] = 30; // insert a new value
    print_map("2) Updated map: ", m);

    // Using operator[] with non-existent key always performs an insert
    std::cout << "3) m[UPS] = " << m["UPS"] << '\n';
    print_map("4) Updated map: ", m);

    m.erase("GPU");
    print_map("5) After erase: ", m);

    std::erase_if(m, [](const auto& pair){ return pair.second > 25; });
    print_map("6) After erase: ", m);
    std::cout << "7) m.size() = " << m.size() << '\n';

    m.clear();
    std::cout << std::boolalpha << "8) Map is empty: " << m.empty() << '\n';
}
```


**Output:**
```
1) Initial map: [CPU] = 10; [GPU] = 15; [RAM] = 20;
2) Updated map: [CPU] = 25; [GPU] = 15; [RAM] = 20; [SSD] = 30;
3) m[UPS] = 0
4) Updated map: [CPU] = 25; [GPU] = 15; [RAM] = 20; [SSD] = 30; [UPS] = 0;
5) After erase: [CPU] = 25; [RAM] = 20; [SSD] = 30; [UPS] = 0;
6) After erase: [CPU] = 25; [RAM] = 20; [UPS] = 0;
7) m.size() = 3
8) Map is empty: true
```


## Defect reports


## See also


| cpp/container/dsc multimap | (see dedicated page) |
| cpp/container/dsc unordered_map | (see dedicated page) |
| cpp/container/dsc flat_map | (see dedicated page) |

