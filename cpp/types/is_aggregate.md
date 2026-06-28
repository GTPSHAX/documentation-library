---
title: std::is_aggregate
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_aggregate
---

cpp/types/traits/is|1=is_aggregate
|std=c++17
|description=If `T` is an aggregate type, provides the member constant `value` equal `true`. For any other type, `value` is `false`.
If `T` is an incomplete type other than an array type or (possibly cv-qualified) `void`, the behavior is undefined.
|inherit_desc=`T` is an aggregate type

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <cstddef>
#include <new>
#include <string_view>
#include <type_traits>
#include <utility>

// Constructs a T at the uninitialized memory pointed to by p using
// list-initialization for aggregates and non-list initialization otherwise.
template<class T, class... Args>
T* construct(T* p, Args&&... args)
{
    if constexpr (std::is_aggregate_v<T>)
        return ::new (static_cast<void*>(p)) T{std::forward<Args>(args)...};
    else
        return ::new (static_cast<void*>(p)) T(std::forward<Args>(args)...);
}

struct A { int x, y; };
static_assert(std::is_aggregate_v<A>);

struct B
{
    int i;
    std::string_view str;

    B(int i, std::string_view str) : i(i), str(str) {}
};
static_assert(not std::is_aggregate_v<B>);

template <typename... Ts>
using aligned_storage_t = alignas(Ts...) std::byte[std::max({sizeof(Ts)...})];

int main()
{
    aligned_storage_t<A, B> storage;

    A& a = *construct(reinterpret_cast<A*>(&storage), 1, 2);
    assert(a.x == 1 and a.y == 2);

    B& b = *construct(reinterpret_cast<B*>(&storage), 3, "4");
    assert(b.i == 3 and b.str == "4");
}
```


## Defect reports

