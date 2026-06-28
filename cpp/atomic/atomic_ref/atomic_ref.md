---
title: std::atomic_ref::atomic_ref
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/atomic_ref
---


```cpp
dcla|num=1|constexpr=c++26|
explicit atomic_ref( T& obj );
dcla|num=2|constexpr=c++26|
atomic_ref( const atomic_ref& ref ) noexcept;
```

Constructs a new `atomic_ref` object.
1. Constructs an `atomic_ref` object referencing the object `obj`.
@@ If `obj` is not aligned to `required_alignment`, the behavior is undefined.
2. Constructs an `atomic_ref` object referencing the object referenced by `ref`.

## Parameters


### Parameters

- `obj` - object to reference
- `ref` - another `atomic_ref` object to copy from

## Example


### Example

```cpp
#include <atomic>
#include <iostream>
#include <numeric>
#include <thread>
#include <vector>

int main()
{
    using Data = std::vector<char>;

    auto inc_atomically = [](Data& data)
    {
        for (Data::value_type& x : data)
        {
            auto xx = std::atomic_ref<Data::value_type>(x);
            ++xx; // atomic read-modify-write
        }
    };

    auto inc_directly = [](Data& data)
    {
        for (Data::value_type& x : data)
            ++x;
    };

    auto test_run = [](const auto Fun)
    {
        Data data(10'000'000);
        {
            std::jthread j1{Fun, std::ref(data)};
            std::jthread j2{Fun, std::ref(data)};
            std::jthread j3{Fun, std::ref(data)};
            std::jthread j4{Fun, std::ref(data)};
        }
        std::cout << "sum = " << std::accumulate(cbegin(data), cend(data), 0) << '\n';
    };

    test_run(inc_atomically);
    test_run(inc_directly);
}
```


**Output:**
```
sum = 40000000
sum = 39994973
```

