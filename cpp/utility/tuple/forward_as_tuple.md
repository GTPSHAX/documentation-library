---
title: std::forward_as_tuple
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/forward_as_tuple
---

ddcla|header=tuple|since=c++11|constexpr=c++14|
template< class... Types >
std::tuple<Types&&...> forward_as_tuple( Types&&... args ) noexcept;
Constructs a tuple of references to the arguments in `args` suitable for forwarding as an argument to a function. The tuple has rvalue reference data members when rvalues are used as arguments, and otherwise has lvalue reference data members.

## Parameters


### Parameters

- `args` - zero or more arguments to construct the tuple from

## Return value

A `std::tuple` object created as if by `std::tuple<Types&&...>(std::forward<Types>(args)...)`

## Notes

If the arguments are temporaries, `forward_as_tuple` does not extend their lifetime; they have to be used before the end of the full expression.

## Example


### Example

```cpp
#include <iostream>
#include <map>
#include <string>
#include <tuple>

int main()
{
    std::map<int, std::string> m;

    m.emplace(std::piecewise_construct,
              std::forward_as_tuple(6),
              std::forward_as_tuple(9, 'g'));
    std::cout << "m[6] = " << m[6] << '\n';

    // The following is an error: it produces a
    // std::tuple<int&&, char&&> holding two dangling references.
    //
    // auto t = std::forward_as_tuple(20, 'a');
    // m.emplace(std::piecewise_construct, std::forward_as_tuple(10), t);
}
```


**Output:**
```
m[6] = ggggggggg
```


## See also


| cpp/utility/tuple/dsc make_tuple | (see dedicated page) |
| cpp/utility/tuple/dsc tie | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_cat | (see dedicated page) |
| cpp/utility/dsc apply | (see dedicated page) |

