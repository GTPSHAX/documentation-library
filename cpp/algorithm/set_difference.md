---
title: std::set_difference
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/set_difference
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class OutputIt >
OutputIt set_difference( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class ForwardIt3 >
ForwardIt3 set_difference( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2,
class OutputIt, class Compare >
OutputIt set_difference( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class ForwardIt3, class Compare >
ForwardIt3 set_difference( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first, Compare comp );
```

Copies the elements from the sorted range [first1, last1) which are not found in the sorted range [first2, last2) to the range beginning at `d_first`. The output range is also sorted.
If [first1, last1) contains `m` elements that are equivalent to each other and [first2, last2) contains `n` elements that are equivalent to them, the final `std::max(m - n, 0)` elements will be copied from [first1, last1) to the output range, preserving order.
1. If [first1, last1) or [first2, last2) is not `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}, the behavior is undefined.
3. If [first1, last1) or [first2, last2) is not sorted with respect to `comp`, the behavior is undefined.
@2,4@ Same as , but executed according to `policy`.
@@
If the output range overlaps with [first1, last1) or [first2, last2), the behavior is undefined.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `d_first` - the beginning of the output range
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `InputIt1, InputIt2`
- `OutputIt`
- `ForwardIt1, ForwardIt2, ForwardIt3`
- `Compare`

## Return value

Iterator past the end of the constructed range.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
@1,2@ At most +N)-1 comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@ At most +N)-1 applications of the comparison function `comp`.

## Exceptions


## Possible implementation

eq impl
|title1=set_difference (1)|ver1=1|1=
template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_difference(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, OutputIt d_first)
{
while (first1 != last1)
{
if (first2 == last2)
return std::copy(first1, last1, d_first);
if (*first1 < *first2)
*d_first++ = *first1++;
else
{
if (! (*first2 < *first1))
++first1;
++first2;
}
}
return d_first;
}
|title2=set_difference (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class OutputIt, class Compare>
OutputIt set_difference(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, OutputIt d_first, Compare comp)
{
while (first1 != last1)
{
if (first2 == last2)
return std::copy(first1, last1, d_first);
if (comp(*first1, *first2))
*d_first++ = *first1++;
else
{
if (!comp(*first2, *first1))
++first1;
++first2;
}
}
return d_first;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

template<typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& v)
{
    os << '{';
    for (auto n{v.size()}; const auto& e : v)
        os << e << (--n ? ", " : "");
    return os << '}';
}

struct Order // a struct with very interesting data
{
    int order_id{};

    friend std::ostream& operator<<(std::ostream& os, const Order& ord)
    {
        return os << ord.order_id;
    }
};

int main()
{
    const std::vector<int> v1{1, 2, 5, 5, 5, 9};
    const std::vector<int> v2{2, 5, 7};
    std::vector<int> diff;

    std::set_difference(v1.begin(), v1.end(), v2.begin(), v2.end(),
                        std::inserter(diff, diff.begin()));

    std::cout << v1 << " ∖ " << v2 << " == " << diff << "\n\n";

    // we want to know which orders "cut" between old and new states:
    std::vector<Order> old_orders{<!---->{1}, {2}, {5}, {9}<!---->};
    std::vector<Order> new_orders{<!---->{2}, {5}, {7}<!---->};
    std::vector<Order> cut_orders;

    std::set_difference(old_orders.begin(), old_orders.end(),
                        new_orders.begin(), new_orders.end(),
                        std::back_inserter(cut_orders),
                        [](auto& a, auto& b) { return a.order_id < b.order_id; });

    std::cout << "old orders: " << old_orders << '\n'
              << "new orders: " << new_orders << '\n'
              << "cut orders: " << cut_orders << '\n';
}
```


**Output:**
```
{1, 2, 5, 5, 5, 9} ∖ {2, 5, 7} == {1, 5, 5, 9}

old orders: {1, 2, 5, 9}
new orders: {2, 5, 7}
cut orders: {1, 9}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-291 | C++98 | it was unspecified how to handle equivalent elements in the input ranges | specified |


## See also


| cpp/algorithm/dsc includes | (see dedicated page) |
| cpp/algorithm/dsc set_symmetric_difference | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_difference | (see dedicated page) |

