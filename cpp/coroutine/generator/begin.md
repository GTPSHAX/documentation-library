---
title: std::generator::begin
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/begin
---

ddcl|since=c++23|1=
/*iterator*/ begin();
Pushes  into  stack, then evaluates `coroutine_.resume()`.
Before invocation of `begin()` the  must refer to a coroutine suspended at its .

## Return value

An iterator whose  member refers to the same coroutine as  does.

## Notes

It is an undefined behavior to call `begin()` more than once on the same `generator` object.

## Example

