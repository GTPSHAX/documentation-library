---
title: std::suspend_always
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/suspend_always
---

ddcl|header=coroutine|since=c++20|
struct suspend_always;
`suspend_always` is an empty class which can be used to indicate that an await expression always suspends and does not produce a value.

## Member functions

member|await_ready|2=
ddcl|
constexpr bool await_ready() const noexcept { return false; }
Always returns `false`, indicating that an await expression always suspends.
member|await_suspend|2=
ddcl|
constexpr void await_suspend( std::coroutine_handle<> ) const noexcept {}
Does nothing.
member|await_resume|2=
ddcl|
constexpr void await_resume() const noexcept {}
Does nothing. An await expression does not produce a value if `suspend_always` is used.

## Example

