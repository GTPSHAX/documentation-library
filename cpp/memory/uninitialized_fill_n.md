---
title: std::uninitialized_fill_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_fill_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|constexpr=c++26|
template< class NoThrowForwardIt, class Size, class T >
NoThrowForwardIt uninitialized_fill_n( NoThrowForwardIt first,
Size count, const T& value );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class NoThrowForwardIt, class Size, class T >
NoThrowForwardIt uninitialized_fill_n( ExecutionPolicy&& policy,
NoThrowForwardIt first,
Size count, const T& value );
```

1. Constructs the first `count` elements in the destination range beginning at `first` with the given value `value` as if by
box|
`for (; count--; ++first)`<br />
`::new (``(*first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type(value);`<br />
`return first;`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `first` - the beginning of the range of the elements to initialize
- `count` - number of elements to construct
- `value` - the value to construct the elements with

**Type requirements:**

- `NoThrowForwardIt`

## Return value

As described above.

## Exceptions

2.

## Notes


## Possible implementation

eq fun|1=
template<class NoThrowForwardIt, class Size, class T>
constexpr NoThrowForwardIt uninitialized_fill_n(NoThrowForwardIt first,
Size count, const T& value)
{
using V = typename std::iterator_traits<NoThrowForwardIt>::value_type;
NoThrowForwardIt current = first;
try
{
for (; count > 0; ++current, (void) --count)
::new (static_cast<void*>(std::addressof(*current))) V(value);
return current;
}
catch (...)
{
for (; first != current; ++first)
first->~V();
throw;
}
return current;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <string>
#include <tuple>

int main()
{
    std::string* p;
    std::size_t sz;
    std::tie(p, sz) = std::get_temporary_buffer<std::string>(4);
    std::uninitialized_fill_n(p, sz, "Example");

    for (std::string* i = p; i != p + sz; ++i)
    {
        std::cout << *i << '\n';
        i->~basic_string<char>();
    }
    std::return_temporary_buffer(p);
}
```


**Output:**
```
Example
Example
Example
Example
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1339 | C++98 | the location of the first element following<br>the filling range was not returned | returned |


## See also


| cpp/memory/dsc uninitialized_fill | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_fill_n | (see dedicated page) |

