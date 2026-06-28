---
title: operators (﻿)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::slide_view::''iterator'', ranges::slide_view::''sentinel''sep

ddcl|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/<Const>& x, const /*sentinel*/& y );
Compares the underlying iterator of `x` with the underlying sentinel of `y`.
Let  denote the underlying iterator of `x` and  denote the underlying sentinel of `y`.
Equivalent to: `1=return x.last_ele_ == y.end_;`.

## Parameters


### Parameters

- `x` - an  to compare
- `y` - a `sentinel` to compare

## Return value

The result of comparison.

## Example

