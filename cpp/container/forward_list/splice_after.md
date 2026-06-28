---
title: std::forward_list::splice_after
type: Containers
source: https://en.cppreference.com/w/cpp/container/forward_list/splice_after
---


```cpp
dcl|num=1|since=c++11|
void splice_after( const_iterator pos, forward_list& other );
dcl|num=2|since=c++11|
void splice_after( const_iterator pos, forward_list&& other );
dcl|num=3|since=c++11|
void splice_after( const_iterator pos, forward_list& other,
const_iterator it );
dcl|num=4|since=c++11|
void splice_after( const_iterator pos, forward_list&& other,
const_iterator it );
dcl|num=5|since=c++11|
void splice_after( const_iterator pos, forward_list& other,
const_iterator first, const_iterator last );
dcl|num=6|since=c++11|
void splice_after( const_iterator pos, forward_list&& other,
const_iterator first, const_iterator last );
```

Moves elements from another `forward_list` to `*this`. The elements are inserted after the element pointed to by `pos`.
No elements are copied. No iterators or references become invalidated. The iterators to the moved elements now refer into `*this`, not into `other`.
@1,2@ Moves all elements from `other` into `*this`. The container `other` becomes empty after the operation.
@3,4@ Moves the element pointed to by the iterator following `it` from `other` into `*this`. Has no effect if `1=pos == it` or if `1=pos == ++it`.
@5,6@ Moves the elements in the range  from `other` into `*this`. The element pointed-to by `first` is not moved.
The behavior is undefined if
* `1=get_allocator() != other.get_allocator()`,
* `pos` is neither `before_begin()` nor a dereferenceable iterator in [begin(), end()),
* for overloads , `*this` and `other` refer to the same object,
* for overloads , the iterator following `it` is not a dereferenceable iterator into `other`, or
* for overloads ,
:*  is not a valid range in `other`,
:* some iterators in  are not dereferenceable, or
:* `pos` is in .

## Parameters


### Parameters

- `pos` - element after which the content will be inserted
- `other` - another container to move the content from
- `it` - iterator preceding the iterator to the element to move from `other` to `*this`
- `[3=to move from {{c, other}} to {{c)` - 

## Exceptions

Throws nothing.

## Complexity

@1,2@ Linear in the size of `other`.
@3,4@ Constant.
@5,6@ Linear in `std::distance(first, last)`.

## Example


### Example

```cpp
#include <cassert>
#include <forward_list>

int main()
{
    using F = std::forward_list<int>;

    // Demonstrate the meaning of open range (first, last)
    // in overload (5): the first element of l1 is not moved.
    F l1 = {1, 2, 3, 4, 5};
    F l2 = {10, 11, 12};

    l2.splice_after(l2.cbegin(), l1, l1.cbegin(), l1.cend());
    // Not equivalent to l2.splice_after(l2.cbegin(), l1);
    // which is equivalent to
    // l2.splice_after(l2.cbegin(), l1, l1.cbefore_begin(), l1.end());

    assert((l1 == F{1}));
    assert((l2 == F{10, 2, 3, 4, 5, 11, 12}));

    // Overload (1)
    F x = {1, 2, 3, 4, 5};
    F y = {10, 11, 12};
    x.splice_after(x.cbegin(), y);
    assert((x == F{1, 10, 11, 12, 2, 3, 4, 5}));
    assert((y == F{}));

    // Overload (3)
    x = {1, 2, 3, 4, 5};
    y = {10, 11, 12};
    x.splice_after(x.cbegin(), y, y.cbegin());
    assert((x == F{1, 11, 2, 3, 4, 5}));
    assert((y == F{10, 12}));

    // Overload (5)
    x = {1, 2, 3, 4, 5};
    y = {10, 11, 12};
    x.splice_after(x.cbegin(), y, y.cbegin(), y.cend());
    assert((x == F{1, 11, 12, 2, 3, 4, 5}));
    assert((y == F{10}));
}
```


## Defect reports


## See also


| cpp/container/dsc merge|forward_list | (see dedicated page) |
| cpp/container/dsc remove|forward_list | (see dedicated page) |
| cpp/container/dsc before_begin|forward_list | (see dedicated page) |

