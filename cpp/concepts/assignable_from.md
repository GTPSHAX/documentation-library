---
title: std::assignable_from
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/assignable_from
---

ddcl|header=concepts|since=c++20|1=
template< class LHS, class RHS >
concept assignable_from =
std::is_lvalue_reference_v<LHS> &&
std::common_reference_with<
const std::remove_reference_t<LHS>&,
const std::remove_reference_t<RHS>&> &&
requires(LHS lhs, RHS&& rhs) {
{ lhs = std::forward<RHS>(rhs) } -> std::same_as<LHS>;
};
The concept `assignable_from<LHS, RHS>` specifies that an expression of the type and value category specified by `RHS` can be assigned to an lvalue expression whose type is specified by `LHS`.

## Semantic requirements

Given
* `lhs`, an lvalue that refers to an object `lcopy` such that `decltype((lhs))` is `LHS`,
* `rhs`, an expression such that `decltype((rhs))` is `RHS`,
* `rcopy`, a distinct object that is equal to `rhs`,
`assignable_from<LHS, RHS>` is modeled only if
* `1=std::addressof(lhs = rhs) == std::addressof(lcopy)` (i.e., the assignment expression yields an lvalue referring to the left operand);
* After evaluating `1=lhs = rhs`:
**  `lhs` is equal to `rcopy`, unless `rhs` is a non-const xvalue that refers to `lcopy` (i.e., the assignment is a self-move-assignment),
** if `rhs` is a glvalue:
*** If it is a non-const xvalue, the object to which it refers is in a valid but unspecified state;
*** Otherwise, the object it refers to is not modified;

## Notes

Assignment need not be a total function. In particular, if assigning to some object `x` can cause some other object `y` to be modified, then `1=x = y` is likely not in the domain of **`=`**. This typically happens if the right operand is owned directly or indirectly by the left operand (e.g., with smart pointers to nodes in a node-based data structure, or with something like `std::vector<std::any>`).

## Example


### Example

```cpp
#include <atomic>
#include <concepts>
#include <string>

int main()
{
    // Normal basic usage, checks lvalue reference assignment
    static_assert(std::is_assignable_v<int&, int>);
    static_assert(std::assignable_from<int&, int>);

    static_assert(std::is_assignable_v<std::string&, std::string>);
    static_assert(std::assignable_from<std::string&, std::string>);

    // Fundamental types don't support assignment to an rvalue
    static_assert(!std::is_assignable_v<int, int>);
    static_assert(!std::assignable_from<int, int>);

    // std::assignable_from doesn't accept all valid assignment expressions:

    // rvalue reference assignment
    static_assert(std::is_assignable_v<std::string&&, std::string>);
    static_assert(!std::assignable_from<std::string&&, std::string>);

    // rvalue assignment
    static_assert(std::is_assignable_v<std::string, std::string>);
    static_assert(!std::assignable_from<std::string, std::string>);

    // std::atomic::operator= returns by value
    static_assert(std::is_assignable_v<std::atomic<int>&, int>);
    static_assert(!std::assignable_from<std::atomic<int>&, int>);
}
```


## References


## See also


| cpp/types/dsc is_assignable | (see dedicated page) |

