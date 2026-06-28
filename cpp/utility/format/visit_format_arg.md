---
title: std::visit_format_arg
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/visit_format_arg
---

ddcl| header=format | since=c++20 | deprecated=c++26 |1=
template< class Visitor, class Context >
/* see below */ visit_format_arg( Visitor&& vis, std::basic_format_arg<Context> arg );
Applies the visitor `vis` to the object contained in `arg`.
Equivalent to `std::visit(std::forward<Visitor>(vis), value)`, where `value` is the `std::variant` stored in `arg`.

## Parameters


### Parameters


## Return value

The value returned by the selected invocation of the visitor.

## Notes

As of C++26, `std::visit_format_arg` is deprecated in favor of the `visit` member functions of `std::basic_format_arg`.

## Example


## See also

