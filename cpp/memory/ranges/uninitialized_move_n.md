---
title: std::ranges::uninitialized_move_n_result
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/uninitialized_move_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++20|constexpr=c++26|
template< std::input_iterator I,
/*nothrow-forward-iterator*/ O, /*nothrow-sentinel-for*/<O> S >
requires std::constructible_from<std::iter_value_t<O>,
std::iter_rvalue_reference_t<I>>
uninitialized_move_n_result<I, O>
uninitialized_move_n( I ifirst, std::iter_difference_t<I> count,
O ofirst, S olast );
dcl|num=2|since=c++26|
template< /*execution-policy*/ Ep, std::random_access_iterator I,
/*nothrow-random-access-iterator*/ O,
/*nothrow-sized-sentinel-for*/<O> S >
requires std::constructible_from<std::iter_value_t<O>,
std::iter_rvalue_reference_t<I>>
uninitialized_move_n_result<I, O>
uninitialized_move_n( Ep&& policy, I ifirst,
std::iter_difference_t<I> count,
O ofirst, S olast );
dcl|num=3|since=c++20|1=
template< class I, class O >
using uninitialized_move_n_result = ranges::in_out_result<I, O>;
```

For the definition of `/*execution-policy*/`, see this page; for the definition of other exposition-only concepts, see this page.
1. Constructs elements in the destination range [ofirst, olast) from elements in the source range  as if by
box|
`1=auto ret = ranges::uninitialized_move(std::counted_iterator(std::move(ifirst), count),`<br />
`std::default_sentinel, ofirst, olast);`<br />
}
@@ If an exception is thrown during the initialization then the objects that already constructed in [ofirst, olast) are destroyed in an unspecified order. Also, the objects in the input range beginning at `ifirst`, that were already moved, are left in a valid but unspecified state.
@@ .
2. Same as , but executed according to `policy`.

## Parameters


### Parameters

- `ifirst` - the beginning of the input range of elements to move from
- `[ofirst, olast)` - 
- `count` - the number of elements to move
- `policy` - execution policy

## Return value

As described above.

## Exceptions

Any exception thrown on construction of the elements in the destination range.
2.

## Notes

An implementation may improve the efficiency of the `ranges::uninitialized_move_n` (by using e.g. ) if the value type of the output range is *TrivialType*.

## Possible implementation

eq fun|1=
struct uninitialized_move_n_fn
{
template<std::input_iterator I,
/*nothrow-forward-iterator*/ O, /*nothrow-sentinel-for*/<O> S>
requires std::constructible_from<std::iter_value_t<O>,
std::iter_rvalue_reference_t<I>>
constexpr ranges::uninitialized_move_n_result<I, O>
operator()(I ifirst, std::iter_difference_t<I> count, O ofirst, S olast) const
{
auto iter = std::counted_iterator(std::move(ifirst), count);
auto ret = ranges::uninitialized_move(iter, std::default_sentinel, ofirst, olast);
return {std::move(ret.in).base(), ret.out};
}
};
inline constexpr uninitialized_move_n_fn uninitialized_move_n{};

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
    std::string in[]{ "No", "Diagnostic", "Required", };
    print("initially, in: ", std::begin(in), std::end(in));

    if (constexpr auto sz = std::size(in);
        void* out = std::aligned_alloc(alignof(std::string), sizeof(std::string) * sz)
    )
    {
        try
        {
            auto first{static_cast<std::string*>(out)};
            auto last{first + sz};
            std::ranges::uninitialized_move_n(std::begin(in), sz, first, last);

            print("after move, in: ", std::begin(in), std::end(in));
            print("after move, out: ", first, last);

            std::ranges::destroy(first, last);
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
initially, in: "No" "Diagnostic" "Required"
after move, in: "" "" ""
after move, out: "No" "Diagnostic" "Required"
```


## See also


| cpp/memory/ranges/dsc uninitialized_move | (see dedicated page) |
| cpp/memory/dsc uninitialized_move_n | (see dedicated page) |

