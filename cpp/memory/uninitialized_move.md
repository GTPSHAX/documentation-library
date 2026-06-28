---
title: std::uninitialized_move
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_move
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++17|constexpr=c++26|
template< class InputIt, class NoThrowForwardIt >
NoThrowForwardIt uninitialized_move( InputIt first, InputIt last,
NoThrowForwardIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt, class NoThrowForwardIt >
NoThrowForwardIt uninitialized_move( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
NoThrowForwardIt d_first );
```

1. Constructs elements in the destination range beginning at `d_first` from elements in the source range [first, last) as if by
box|
`1=for (; first != last; ++d_first, (void) ++first)`<br />
`::new (``(*d_first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type(``(*iter));`<br />
`return d_first;`
@@ If an exception is thrown during the initialization, some objects in [first, last) are left in a valid but unspecified state, and the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@
rrev|since=c++20|
.

## Parameters


### Parameters

- `d_first` - the beginning of the destination range
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`
- `NoThrowForwardIt`

## Return value

As described above.

## Exceptions

2.

## Notes

When the input iterator deferences to an rvalue, the behavior of `std::uninitialized_move` is same as `std::uninitialized_copy`.

## Possible implementation

eq fun|1=
template<class InputIt, class NoThrowForwardIt>
constexpr NoThrowForwardIt uninitialized_move(InputIt first, InputIt last,
NoThrowForwardIt d_first)
{
using ValueType = typename std::iterator_traits<NoThrowForwardIt>::value_type;
auto current = d_first;
try
{
for (; first != last; ++first, (void) ++current)
{
auto addr = static_cast<void*>(std::addressof(*current));
if constexpr (std::is_lvalue_reference_v<decltype(*first)>)
::new (addr) ValueType(std::move(*first));
else
::new (addr) ValueType(*first);
}
return current;
}
catch (...)
{
std::destroy(d_first, current);
throw;
}
}

## Example


### Example


**Output:**
```
initially, in: "Home" "Work!"
after move, in: "" ""
after move, out: "Home" "Work!"
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3918 | C++17 | move constuction is always performed even<br>if the input iterator deferences to a prvalue | no move construction<br>in this case |


## See also


| cpp/memory/dsc uninitialized_copy | (see dedicated page) |
| cpp/memory/dsc uninitialized_move_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_move | (see dedicated page) |

