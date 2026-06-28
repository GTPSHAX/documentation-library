---
title: std::get(std::array)
type: Containers
source: https://en.cppreference.com/w/cpp/container/array/get
---


# getpetty|(std::array)


```cpp
**Header:** `<`array`>`
|
template< std::size_t I, class T, std::size_t N >
T& get( std::array<T,N>& a ) noexcept;
|
template< std::size_t I, class T, std::size_t N >
T&& get( std::array<T,N>&& a ) noexcept;
|
template< std::size_t I, class T, std::size_t N >
const T& get( const std::array<T,N>& a ) noexcept;
|
template< std::size_t I, class T, std::size_t N >
const T&& get( const std::array<T,N>&& a ) noexcept;
```

Extracts the `I` element from the array using  interface.
`I` must be an integer value in range . This is enforced at compile time as opposed to `at()` or `operator[]`.

## Parameters


### Parameters

- `a` - array whose contents to extract

## Return value

A reference to the `I` element of `a`.

## Complexity

Constant.

## Example


### Example

```cpp
#include <array>
#include <iostream>

constexpr std::array v{1, 2, 3};
static_assert(get<0>(v) == 1 && get<1>(v) == 2 && get<2>(v) == 3);

int main()
{
    std::array<int, 3> a;

    // set values:
    get<0>(a) = 1, get<1>(a) = 2, get<2>(a) = 3;

    // get values:
    std::cout << '(' << get<0>(a) << ',' << get<1>(a) << ',' << get<2>(a) << ")\n";
}
```


**Output:**
```
(1,2,3)
```


## Defect reports


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/container/dsc operator_at|array | (see dedicated page) |
| cpp/container/dsc at|array | (see dedicated page) |
| cpp/utility/tuple/dsc get | (see dedicated page) |
| cpp/utility/pair/dsc get | (see dedicated page) |
| cpp/utility/variant/dsc get | (see dedicated page) |
| cpp/ranges/subrange/dsc get | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |

