---
title: std::uninitialized_value_construct
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_value_construct
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++17|constexpr=c++26|
template< class NoThrowForwardIt >
void uninitialized_value_construct( NoThrowForwardIt first,
NoThrowForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class NoThrowForwardIt >
void uninitialized_value_construct( ExecutionPolicy&& policy,
NoThrowForwardIt first,
NoThrowForwardIt last );
```

1. Constructs elements in the destination range [first, last) by value-initialization as if by
box|
`1=for (; first != last; ++first)`<br />
`::new (``(*first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type();`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `NoThrowForwardIt`

## Exceptions

2.

## Notes


## Possible implementation

eq fun|1=
template<class NoThrowForwardIt>
constexpr void uninitialized_value_construct(NoThrowForwardIt first,
NoThrowForwardIt last)
{
using Value = typename std::iterator_traits<NoThrowForwardIt>::value_type;
NoThrowForwardIt current = first;
try
{
for (; current != last; ++current)
{
::new (static_cast<void*>(std::addressof(*current))) Value();
}
}
catch (...)
{
std::destroy(first, current);
throw;
}
}

## Example


### Example


**Output:**
```
Default value
Default value
Default value
1 2 3 4
0 0 0 0
```


## See also


| cpp/memory/dsc uninitialized_value_construct_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_default_construct | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_value_construct | (see dedicated page) |

