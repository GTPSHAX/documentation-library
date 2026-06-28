---
title: synth-three-way
type: Standard
source: https://en.cppreference.com/w/cpp/standard_library/synth-three-way
---


# ''synth-three-way'', ''synth-three-way-result''


```cpp
dcla|num=1|since=c++20|expos=yes|1=
constexpr auto synth-three-way = /* see below */;
dcla|num=2|since=c++20|expos=yes|1=
template< class T, class U = T >
using synth-three-way-result =
decltype(synth-three-way(std::declval<T&>(), std::declval<U&>()));
```

1. A function object whose `operator()` behaves as the synthesized three-way comparison function. Equivalent to:

```cpp
constexpr auto synth-three-way =
    []<class T, class U>(const T& t, const U& u)
        requires requires
        {
            { t < u } -> boolean-testable;
            { u < t } -> boolean-testable;
        }
    {
        if constexpr (std::three_way_comparable_with<T, U>)
            return t <=> u;
        else
        {
            if (t < u)
                return std::weak_ordering::less;
            if (u < t)
                return std::weak_ordering::greater;
            return std::weak_ordering::equivalent;
        }
    };
```

2. The return type of the `operator()` of  ().

## Parameters


### Parameters

- `t, u` - the values to be compared

## Return value

The compare result.

## See also


| cpp/utility/pair/dsc operator cmp | (see dedicated page) |
| cpp/utility/tuple/dsc operator cmp | (see dedicated page) |
| cpp/container/dsc operator cmp|array | (see dedicated page) |
| cpp/container/dsc operator cmp|deque | (see dedicated page) |
| cpp/container/dsc operator cmp|forward_list | (see dedicated page) |
| cpp/container/dsc operator cmp|list | (see dedicated page) |
| cpp/container/dsc operator cmp|vector | (see dedicated page) |
| cpp/container/dsc operator cmp|map | (see dedicated page) |
| cpp/container/dsc operator cmp|multimap | (see dedicated page) |
| cpp/container/dsc operator cmp|set | (see dedicated page) |
| cpp/container/dsc operator cmp|multiset | (see dedicated page) |

