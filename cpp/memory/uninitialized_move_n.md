---
title: std::uninitialized_move_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_move_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++17|constexpr=c++26|
template< class InputIt, class Size, class NoThrowForwardIt >
std::pair<InputIt, NoThrowForwardIt>
uninitialized_move_n( InputIt first, Size count,
NoThrowForwardIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt, class Size, class NoThrowForwardIt >
std::pair<ForwardIt, NoThrowForwardIt>
uninitialized_move_n( ExecutionPolicy&& policy, ForwardIt first,
Size count, NoThrowForwardIt d_first );
```

1. Constructs elements in the destination range beginning at `d_first` from the first `count` elements in the source range beginning at `first` as if by
box|
`for (; count > 0; ++d_first, (void) ++first, --count)`<br />
`::new (``(*d_first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type(``(*iter));`<br />
}
@@ If an exception is thrown during the initialization, some objects in  are left in a valid but unspecified state, and the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@
rrev|since=c++20|
.

## Parameters


### Parameters

- `first` - the beginning of the range of the elements to move
- `d_first` - the beginning of the destination range
- `count` - the number of elements to move
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

When the input iterator deferences to an rvalue, the behavior of `std::uninitialized_move_n` is same as `std::uninitialized_copy_n`.

## Possible implementation

eq fun|1=
template<class InputIt, class Size, class NoThrowForwardIt>
constexpr std::pair<InputIt, NoThrowForwardIt>
uninitialized_move_n(InputIt first, Size count, NoThrowForwardIt d_first)
{
using ValueType = typename std::iterator_traits<NoThrowForwardIt>::value_type;
NoThrowForwardIt current = d_first;
try
{
for (; count > 0; ++first, (void) ++current, --count) {
auto addr = static_cast<void*>(std::addressof(*current));
if constexpr (std::is_lvalue_reference_v<decltype(*first)>)
::new (addr) ValueType(std::move(*first));
else
::new (addr) ValueType(*first);
}
}
catch (...)
{
std::destroy(d_first, current);
throw;
}
return {first, current};
}

## Example


### Example

```cpp
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>

void print(auto rem, auto first, auto last)
{
    for (std::cout << rem; first != last; ++first)
        std::cout << std::quoted(*first) << ' ';
    std::cout << '\n';
}

int main()
{
    std::string in[]{"One", "Definition", "Rule"};
    print("initially, in: ", std::begin(in), std::end(in));

    if (constexpr auto sz = std::size(in);
        void* out = std::aligned_alloc(alignof(std::string), sizeof(std::string) * sz))
    {
        try
        {
            auto first{static_cast<std::string*>(out)};
            auto last{first + sz};
            std::uninitialized_move_n(std::begin(in), sz, first);

            print("after move, in: ", std::begin(in), std::end(in));
            print("after move, out: ", first, last);

            std::destroy(first, last);
        }
        catch (...)
        {
            std::cout << "Exception!\n";
        }
        std::free(out);
    }
}
```


**Output:**
```
initially, in: "One" "Definition" "Rule" 
after move, in: "" "" "" 
after move, out: "One" "Definition" "Rule"
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3918 | C++17 | move constuction is always performed even<br>if the input iterator deferences to a prvalue | no move construction<br>in this case |


## See also


| cpp/memory/dsc uninitialized_move | (see dedicated page) |
| cpp/memory/dsc uninitialized_copy_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_move_n | (see dedicated page) |

