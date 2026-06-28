---
title: std::copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/copy
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt >
OutputIt copy( InputIt first, InputIt last,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2 >
ForwardIt2 copy( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first );
dcla|num=3|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt, class UnaryPred >
OutputIt copy_if( InputIt first, InputIt last,
OutputIt d_first, UnaryPred pred );
dcl|num=4|since=c++17|1=
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class UnaryPred >
ForwardIt2 copy_if( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, UnaryPred pred );
```

Copies the elements in the range, defined by [first, last), to another range beginning at `d_first` (copy destination range).
1. Copies all elements in the range [first, last) starting from `first` and proceeding to `last`.
@@ If `d_first` is in [first, last), the behavior is undefined. In this case, `std::copy_backward` may be used instead.
2. Copies the elements, but executed according to `policy`.
@@
@@ If [first, last) and the copy destination range overlaps, the behavior is undefined.
3. Only copies the elements for which the predicate `pred` returns `true`. This copy algorithm is stable: the relative order of the elements that are copied is preserved.
@@ If [first, last) and the copy destination range overlaps, the behavior is undefined.
4. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[3=to copy, range=source}})` - 
- `d_first` - the beginning of the destination range
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`
- `UnaryPred`

## Return value

Output iterator to the element in the destination range, one past the last element copied.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  assignments.
@3,4@ Exactly  applications of the predicate `pred`, and at most  assignments.
For the overloads with an `ExecutionPolicy`, there may be a performance cost if `ForwardIt1`'s value type is not *MoveConstructible*.

## Exceptions


## Possible implementation

eq impl
|title1=copy (1)|ver1=1|1=
template<class InputIt, class OutputIt>
OutputIt copy(InputIt first, InputIt last,
OutputIt d_first)
{
for (; first != last; (void)++first, (void)++d_first)
*d_first = *first;
return d_first;
}
|title2=copy_if (3)|ver2=3|2=
template<class InputIt, class OutputIt, class UnaryPred>
OutputIt copy_if(InputIt first, InputIt last,
OutputIt d_first, UnaryPred pred)
{
for (; first != last; ++first)
if (pred(*first))
{
*d_first = *first;
++d_first;
}
return d_first;
}

## Notes

In practice, implementations of `std::copy` avoid multiple assignments and use bulk copy functions such as `std::memmove` if the value type is *TriviallyCopyable* and the iterator types satisfy *ContiguousIterator*.
When copying overlapping ranges, `std::copy` is appropriate when copying to the left (beginning of the destination range is outside the source range) while `std::copy_backward` is appropriate when copying to the right (end of the destination range is outside the source range).

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

int main()
{
    std::vector<int> from_vector(10);
    std::iota(from_vector.begin(), from_vector.end(), 0);    
    std::vector<int> to_vector;
    std::copy(from_vector.begin(), from_vector.end(), std::back_inserter(to_vector));

// or, alternatively,
//  std::vector<int> to_vector(from_vector.size());
//  std::copy(from_vector.begin(), from_vector.end(), to_vector.begin());
// either way is equivalent to
//  std::vector<int> to_vector = from_vector;

    std::cout << "to_vector contains: ";
    std::copy(to_vector.begin(), to_vector.end(),
              std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    std::cout << "odd numbers in to_vector are: ";
    std::copy_if(to_vector.begin(), to_vector.end(),
                 std::ostream_iterator<int>(std::cout, " "),
                 [](int x) { return x % 2 != 0; });
    std::cout << '\n';

    std::cout << "to_vector contains these multiples of 3: ";
    to_vector.clear();
    std::copy_if(from_vector.begin(), from_vector.end(),
                 std::back_inserter(to_vector),
                 [](int x) { return x % 3 == 0; });

    for (const int x : to_vector)
        std::cout << x << ' ';
    std::cout << '\n';
}
```


**Output:**
```
to_vector contains: 0 1 2 3 4 5 6 7 8 9
odd numbers in to_vector are: 1 3 5 7 9
to_vector contains these multiples of 3: 0 3 6 9
```


## Defect reports


## See also


| cpp/algorithm/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/dsc copy_n | (see dedicated page) |
| cpp/algorithm/dsc fill | (see dedicated page) |
| cpp/algorithm/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |

