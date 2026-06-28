---
title: std::uninitialized_value_construct_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_value_construct_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++17|constexpr=c++26|
template< class NoThrowForwardIt, class Size >
NoThrowForwardIt uninitialized_value_construct_n
( NoThrowForwardIt first, Size count );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class NoThrowForwardIt, class Size >
NoThrowForwardIt uninitialized_value_construct_n
( ExecutionPolicy&& policy, NoThrowForwardIt first, Size count );
```

1. Constructs elements in the destination range  by value-initialization as if by
box|
`1=for (; count > 0; (void)++first, --count)`<br />
`::new (``(*first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type();`<br />
`return first;`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `first` - the beginning of the range of elements to initialize
- `count` - the number of elements to initialize
- `policy` - execution policy

**Type requirements:**

- `NoThrowForwardIt`

## Return value

As described above.

## Exceptions

2.

## Notes


## Possible implementation

eq fun|1=
template<class NoThrowForwardIt, class Size>
constexpr ForwardIt uninitialized_value_construct_n(NoThrowForwardIt first, Size count)
{
using T = typename std::iterator_traits<NoThrowForwardIt>::value_type;
NoThrowForwardIt current = first;
try
{
for (; countn > 0; (void) ++current, --count)
::new (static_cast<void*>(std::addressof(*current))) T();
return current;
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


| cpp/memory/dsc uninitialized_value_construct | (see dedicated page) |
| cpp/memory/dsc uninitialized_default_construct_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_value_construct_n | (see dedicated page) |

