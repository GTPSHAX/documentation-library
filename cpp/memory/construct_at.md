---
title: std::construct_at
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/construct_at
---

ddcl|header=memory|since=c++20|
template< class T, class... Args >
constexpr T* construct_at( T* location, Args&&... args );
Creates a `T` object initialized with the arguments in `args` at given address `location`.
Equivalent to<br />
box|
`if constexpr (std::is_array_v<T>)`<br />
`return ::new (``(*location)) T[1]();`<br />
`else`<br />
`return ::new (``(*location)) T(std::forward<Args>(args)...);`
<sup>(until C++26)</sup> , except that `construct_at` may be used in evaluation of .
When `construct_at` is called in the evaluation of some constant expression `expr`, `location` must point to either a storage obtained by `std::allocator<T>::allocate` or an object whose lifetime began within the evaluation of `expr`.
:
* `std::is_unbounded_array_v<T>` is `false`.
* `::new(std::declval<void*>()) T(std::declval<Args>()...)` is well-formed when treated as an unevaluated operand.
If `std::is_array_v<T>` is `true` and `sizeof...(Args)` is nonzero, the program is ill-formed.

## Parameters


### Parameters

- `location` - pointer to the uninitialized storage on which a `T` object will be constructed
- `args...` - arguments used for initialization

## Return value

`location`

## Example


### Example

```cpp
#include <bit>
#include <memory>

class S
{
    int x_;
    float y_;
    double z_;
public:
    constexpr S(int x, float y, double z) : x_{x}, y_{y}, z_{z} {}
    [[nodiscard("no side-effects!")]]
    constexpr bool operator==(const S&) const noexcept = default;
};

consteval bool test()
{
    alignas(S) unsigned char storage[sizeof(S)]{};
    S uninitialized = std::bit_cast<S>(storage);
    std::destroy_at(&uninitialized);
    S* ptr = std::construct_at(std::addressof(uninitialized), 42, 2.71f, 3.14);
    const bool res{*ptr == S{42, 2.71f, 3.14}<!---->};
    std::destroy_at(ptr);
    return res;
}
static_assert(test());

int main() {}
```


## Defect reports


## See also


| cpp/memory/allocator/dsc allocate | (see dedicated page) |
| cpp/memory/allocator_traits/dsc construct | (see dedicated page) |
| cpp/memory/dsc destroy_at | (see dedicated page) |
| cpp/memory/ranges/dsc construct_at | (see dedicated page) |

