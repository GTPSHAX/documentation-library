---
title: std::raw_storage_iterator
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/raw_storage_iterator
---


```cpp
**Header:** `<`memory`>`
dcl rev multi|until1=c++17|dcl1=
template< class OutputIt, class T >
class raw_storage_iterator
: public std::iterator<std::output_iterator_tag, void, void, void, void>;
|notes2=|dcl2=
template< class OutputIt, class T >
class raw_storage_iterator;
```

The output iterator `std::raw_storage_iterator` makes it possible for standard algorithms to store results in uninitialized memory. Whenever the algorithm writes an object of type `T` to the dereferenced iterator, the object is copy-constructed into the location in the uninitialized storage pointed to by the iterator. The template parameter `OutputIt` is any type that meets the requirements of *OutputIterator* and has `operator*` defined to return an object, for which `operator&` returns an object of type `T*`. Usually, the type `T*` is used as `OutputIt`.

## Type requirements


### Parameters

- `OutputIt`

## Member functions


| cpp/memory/raw_storage_iterator/dsc constructor | (see dedicated page) |
| cpp/memory/raw_storage_iterator/dsc operator{{= | (see dedicated page) |
| cpp/memory/raw_storage_iterator/dsc operator* | (see dedicated page) |
| cpp/memory/raw_storage_iterator/dsc operator_arith | (see dedicated page) |
| cpp/memory/raw_storage_iterator/dsc base | (see dedicated page) |


## Note

`std::raw_storage_iterator` was deprecated primarily because of its exception-unsafe behavior. Unlike `std::uninitialized_copy`, it doesn't handle exceptions during operations like `std::copy` safely, potentially leading to resource leaks due to a lack of tracking the number of successfully constructed objects and their proper destruction in the presence of exceptions.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <string>

int main()
{
    const std::string s[] = {"This", "is", "a", "test", "."};
    std::string* p = std::allocator<std::string>().allocate(5);

    std::copy(std::begin(s), std::end(s),
              std::raw_storage_iterator<std::string*, std::string>(p));

    for (std::string* i = p; i != p + 5; ++i)
    {
        std::cout << *i << '\n';
        i->~basic_string<char>();
    }
    std::allocator<std::string>().deallocate(p, 5);
}
```


**Output:**
```
This
is
a
test
.
```


## See also


| cpp/memory/dsc allocator_traits | (see dedicated page) |
| cpp/memory/dsc scoped_allocator_adaptor | (see dedicated page) |
| cpp/memory/dsc uses_allocator | (see dedicated page) |
| cpp/memory/dsc uninitialized_copy | (see dedicated page) |

