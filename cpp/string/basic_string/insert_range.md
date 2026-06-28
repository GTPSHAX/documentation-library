---
title: std::basic_string::insert_range
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/insert_range
---

ddcl|since=c++23|1=
template< container-compatible-range<CharT> R >
constexpr iterator insert_range( const_iterator pos, R&& rg );
Inserts characters from the range `rg` before the element (if any) pointed by `pos`.
Equivalent to

```cpp
return insert(pos - begin(),
    std::basic_string(
        std::from_range,
        std​::​forward<R>(rg),
        get_allocator())
);
```

If `pos` is not a valid iterator on `*this`, the behavior is undefined.

## Parameters


### Parameters

- `pos` - iterator before which the characters will be inserted
- `rg` - a 

## Return value

An iterator which refers to the first inserted character, or `pos` if no characters were inserted because `rg` was empty.

## Complexity

Linear in size of `rg`.

## Exceptions

If `std::allocator_traits<Allocator>::allocate` throws an exception, it is rethrown.

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <iterator>
#include <string>

int main()
{
    const auto source = {'l', 'i', 'b', '_'};
    std::string target{"__cpp_containers_ranges"};
    //                        ^insertion will occur
    //                         before this position

    const auto pos = target.find("container");
    assert(pos != target.npos);
    auto iter = std::next(target.begin(), pos);

#ifdef __cpp_lib_containers_ranges
    target.insert_range(iter, source);
#else
    target.insert(iter, source.begin(), source.end());
#endif

    assert(target == "__cpp_lib_containers_ranges");
    //                      ^^^^
}
```


## See also


| cpp/string/basic_string/dsc insert | (see dedicated page) |

