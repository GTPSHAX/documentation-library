---
title: std::ranges::join_view::iterator<Const>::satisfy
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/iterator/satisfy
---

ddcl|since=c++20|notes=|
constexpr void satisfy();
Skips over empty inner ranges and initializes the underlying iterator .
Let the constant `/*ref-is-glvalue*/` be `std::is_reference_v<ranges::range_reference_t<Base>>`.
The function body is equivalent to

```cpp
auto update_inner = [this](const ranges::iterator_t<Base>& x) -> auto&&
{
    if constexpr (/*ref-is-glvalue*/)     // *x is a reference
        return *x;
    else
        return parent_->inner_./*emplace-deref*/(x);
};

for (; outer_ != ranges::end(parent_->base_); ++outer_)
{
    auto&& inner = update_inner(outer_);
    inner_ = ranges::begin(inner);
    if (inner_ != ranges::end(inner))
        return;
}

if constexpr (/*ref-is-glvalue*/)
    inner_ = InnerIter();
```


## Parameters

(none)

## Return value

(none)
