---
title: std::set
type: Containers
source: https://en.cppreference.com/w/cpp/container/set
---


```cpp
**Header:** `<`set`>`
dcl|num=1|1=
template<
class Key,
class Compare = std::less<Key>,
class Allocator = std::allocator<Key>
> class set;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class Compare = std::less<Key>
> using set = std::set<Key, Compare, std::pmr::polymorphic_allocator<Key>>;
}
```

`std::set` is an associative container that contains a sorted set of unique objects of type `Key`. Sorting is done using the key comparison function *Compare*. Search, removal, and insertion operations have logarithmic complexity. Sets are usually implemented as [Red–black tree](https://en.wikipedia.org/wiki/Red–black tree)s.
Everywhere the standard library uses the *Compare* requirements, uniqueness is determined by using the equivalence relation. In imprecise terms, two objects `a` and `b` are considered equivalent if neither compares less than the other: `!comp(a, b) && !comp(b, a)`.
`std::set` meets the requirements of *Container*, *AllocatorAwareContainer*, *AssociativeContainer* and *ReversibleContainer*.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|set | (see dedicated page) |
| cpp/container/dsc value_type|set | (see dedicated page) |
| cpp/container/dsc size_type|set | (see dedicated page) |
| cpp/container/dsc difference_type|set | (see dedicated page) |
| cpp/container/dsc key_compare|set | (see dedicated page) |
| cpp/container/dsc value_compare2|set | (see dedicated page) |
| cpp/container/dsc allocator_type|set | (see dedicated page) |
| cpp/container/dsc reference|set | (see dedicated page) |
| cpp/container/dsc const_reference|set | (see dedicated page) |
| cpp/container/dsc pointer|set | (see dedicated page) |
| cpp/container/dsc const_pointer|set | (see dedicated page) |
| cpp/container/dsc iterator|set | (see dedicated page) |
| cpp/container/dsc const_iterator|set | (see dedicated page) |
| cpp/container/dsc reverse_iterator|set | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|set | (see dedicated page) |
| cpp/container/dsc node_type|set | (see dedicated page) |
| cpp/container/dsc insert_return_type|set | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|set | (see dedicated page) |
| cpp/container/dsc destructor|set | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|set | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|set | (see dedicated page) |
| cpp/container/dsc end|set | (see dedicated page) |
| cpp/container/dsc rbegin|set | (see dedicated page) |
| cpp/container/dsc rend|set | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|set | (see dedicated page) |
| cpp/container/dsc size|set | (see dedicated page) |
| cpp/container/dsc max_size|set | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|set | (see dedicated page) |
| cpp/container/dsc insert|set | (see dedicated page) |
| cpp/container/dsc insert_range|set | (see dedicated page) |
| cpp/container/dsc emplace|set | (see dedicated page) |
| cpp/container/dsc emplace_hint|set | (see dedicated page) |
| cpp/container/dsc erase|set | (see dedicated page) |
| cpp/container/dsc swap|set | (see dedicated page) |
| cpp/container/dsc extract|set | (see dedicated page) |
| cpp/container/dsc merge|set | (see dedicated page) |

#### Lookup

| cpp/container/dsc count|set | (see dedicated page) |
| cpp/container/dsc find|set | (see dedicated page) |
| cpp/container/dsc contains|set | (see dedicated page) |
| cpp/container/dsc equal_range|set | (see dedicated page) |
| cpp/container/dsc lower_bound|set | (see dedicated page) |
| cpp/container/dsc upper_bound|set | (see dedicated page) |

#### Observers

| cpp/container/dsc key_comp|set | (see dedicated page) |
| cpp/container/dsc value_comp|set | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|set | (see dedicated page) |
| cpp/container/dsc swap2|set | (see dedicated page) |
| cpp/container/dsc erase_if|set | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <set>
#include <string_view>

template<typename T>
std::ostream& operator<<(std::ostream& out, const std::set<T>& set)
{
    if (set.empty())
        return out << "{}";
    out << "{ " << *set.begin();
    std::for_each(std::next(set.begin()), set.end(), [&out](const T& element)
    {
        out << ", " << element;
    });
    return out << " }";
}

int main()
{
    std::set<int> set{1, 5, 3};
    std::cout << set << '\n';

    set.insert(2);
    std::cout << set << '\n';

    set.erase(1);
    std::cout << set << "\n\n";

    std::set<int> keys{3, 4};
    for (int key : keys)
    {
        if (set.contains(key))
            std::cout << set << " does contain " << key << '\n';
        else
            std::cout << set << " doesn't contain " << key << '\n';
    }
    std::cout << '\n';

    std::string_view word = "element";
    std::set<char> characters(word.begin(), word.end());
    std::cout << "There are " << characters.size() << " unique characters in "
              << std::quoted(word) << ":\n" << characters << '\n';
}
```


**Output:**
```
{ 1, 3, 5 }
{ 1, 2, 3, 5 }
{ 2, 3, 5 }

{ 2, 3, 5 } does contain 3
{ 2, 3, 5 } doesn't contain 4

There are 5 unique characters in "element":
{ e, l, m, n, t }
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-103 | C++98 | iterator allows modification of keys | iterator made constant |


## See also


| cpp/container/dsc multiset | (see dedicated page) |
| cpp/container/dsc unordered_set | (see dedicated page) |
| cpp/container/dsc flat_set | (see dedicated page) |

