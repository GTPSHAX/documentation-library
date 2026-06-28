---
title: std::basic_format_arg::handle
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/basic_format_arg/handle
---

ddcl|header=format|since=c++20|
template< class Context >
class basic_format_arg<Context>::handle;
A type-erased wrapper that allows formatting an object of a user-defined type.
`handle` objects are typically created by `std::make_format_args` and accessed through `std::visit_format_arg`<sup>(since C++26)</sup>  or the `visit` member functions of `std::basic_format_arg`.

## Data members

A typical implementation of `handle` is *TriviallyCopyable* and only stores two non-static data members:
* a `const void*` pointer to the object to be formatted, and
* a `void (*)(std::basic_format_parse_context<Context::char_type>&, Context&, const void*)` function pointer to the function performing needed operations in the `format` member function (see below).

## Member functions

member|format|2=
ddcl|since=c++20|
void format( std::basic_format_parse_context<Context::char_type>& parse_ctx,
Context& format_ctx ) const;
Let
* `T` be the type of the formatting argument,
* `TD` be `std::remove_const_t<T>`,
* `TQ` be `const TD` if `const TD` satisfies `<Context>` or `TD` otherwise, and
* `ref` be a reference to the formatting argument.
Equivalent to:
cc|
typename Context::template formatter_type<TD> f;
parse_ctx.advance_to(f.parse(parse_ctx));
format_ctx.advance_to(f.format(const_cast<TQ&>(static_cast<const TD&>(ref)), format_ctx));

## Notes

A `handle` has reference semantics for the formatted argument and does not extend its lifetime. It is the programmer's responsibility to ensure that the argument outlives the `handle`. Usually, a `handle` is only used within formatting functions.

## See also

