---
title: std::unique_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/unique_copy
---


```cpp
**Header:** `<`algorithm`>`
|
template< class InputIt, class OutputIt >
OutputIt unique_copy( InputIt first, InputIt last, OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
ForwardIt2 unique_copy( ExecutionPolicy&& policy, ForwardIt1 first,
ForwardIt1 last, ForwardIt2 d_first );
|
template< class InputIt, class OutputIt, class BinaryPred >
OutputIt unique_copy( InputIt first, InputIt last,
OutputIt d_first, BinaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt1,
class ForwardIt2, class BinaryPred >
ForwardIt2 unique_copy( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, BinaryPred p );
```

Copies the elements from the range [first, last), to another range beginning at `d_first` in such a way that there are no consecutive equal elements. Only the first element of each group of equal elements is copied.
1. Elements are compared using `1=operator==`.
@@ If `1=operator==` does not establish an [equivalence relation](https://en.wikipedia.org/wiki/equivalence relation), the behavior is undefined.
3. Elements are compared using the given binary predicate `p`.
@@ If `p` does not establish an equivalence relation, the behavior is undefined.
@2,4@ Same as , but executed according to `policy`.
@@
If <sup>(until C++20)</sup> `1=*d_first = *first` is invalid<sup>(since C++20)</sup> `*first` is not writable to `d_first`, the program is ill-formed.
If source and destination ranges overlap, the behavior is undefined.
Given `T` as the value type of `InputIt`, if overload  or  does '''not''' satisfy all of the following conditions, the behavior is undefined:
rev|until=c++20|
* `InputIt` meets the requirements of *ForwardIterator*.
rev|since=c++20|
* `InputIt` models .
* `T` is both *CopyConstructible* and *CopyAssignable*.
* All following conditions are satisfied:
:* `OutputIt` meets the requirements of *ForwardIterator*.
:* The value type of `OutputIt` is also `T`.
:* `T` is *CopyAssignable*.

## Parameters


### Parameters

- `[3=to process, range=source}})` - 
- `d_first` - the beginning of the destination range
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`

## Return value

Output iterator to the element past the last written element.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons using `1=operator==`.
@3,4@ Exactly  applications of the predicate `p`.
For overloads , there may be a performance cost if the value type of `ForwardIt1` is not both *CopyConstructible* and *CopyAssignable*.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1046 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L2177 libc++].

## Notes

If `InputIt` satisfies *ForwardIterator*, this function rereads the input in order to detect duplicates.
Otherwise, if `OutputIt` satisfies *ForwardIterator*, and the value type of `InputIt` is the same as that of `OutputIt`, this function compare `*d_first` to `*first`.
Otherwise, this function compares `*first` to a local element copy.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    std::string s1 {"A string with mmmany letters!"};
    std::cout << "Before: " << s1 << '\n';

    std::string s2;
    std::unique_copy(s1.begin(), s1.end(), std::back_inserter(s2),
                     [](char c1, char c2) { return c1 == 'm' && 'm' == c2; });

    std::cout << "After:  " << s2 << '\n';
}
```


**Output:**
```
Before: A string with mmmany letters!
After:  A string with many letters!
```


## Defect reports


## See also


| cpp/algorithm/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/dsc unique | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique_copy | (see dedicated page) |

