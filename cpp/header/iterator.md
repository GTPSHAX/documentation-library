---
title: iterator
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/iterator
---

This header is part of the iterator library.
rrev|since=c++23|
This header is a partial freestanding header. Everything inside this header is freestanding beside stream iterators.


#### Iterator concepts

| cpp/iterator/dsc indirectly_readable | (see dedicated page) |
| cpp/iterator/dsc indirectly_writable | (see dedicated page) |
| cpp/iterator/dsc weakly_incrementable | (see dedicated page) |
| cpp/iterator/dsc incrementable | (see dedicated page) |
| cpp/iterator/dsc input_or_output_iterator | (see dedicated page) |
| cpp/iterator/dsc sentinel_for | (see dedicated page) |
| cpp/iterator/dsc sized_sentinel_for | (see dedicated page) |
| cpp/iterator/dsc input_iterator | (see dedicated page) |
| cpp/iterator/dsc output_iterator | (see dedicated page) |
| cpp/iterator/dsc forward_iterator | (see dedicated page) |
| cpp/iterator/dsc bidirectional_iterator | (see dedicated page) |
| cpp/iterator/dsc random_access_iterator | (see dedicated page) |
| cpp/iterator/dsc contiguous_iterator | (see dedicated page) |

#### Indirect callable concepts

| cpp/iterator/dsc indirectly_unary_invocable | (see dedicated page) |
| cpp/iterator/dsc indirect_unary_predicate | (see dedicated page) |
| cpp/iterator/dsc indirect_binary_predicate | (see dedicated page) |
| cpp/iterator/dsc indirect_equivalence_relation | (see dedicated page) |
| cpp/iterator/dsc indirect_strict_weak_order | (see dedicated page) |

#### Common algorithm requirements

| cpp/iterator/dsc indirectly_movable | (see dedicated page) |
| cpp/iterator/dsc indirectly_movable_storable | (see dedicated page) |
| cpp/iterator/dsc indirectly_copyable | (see dedicated page) |
| cpp/iterator/dsc indirectly_copyable_storable | (see dedicated page) |
| cpp/iterator/dsc indirectly_swappable | (see dedicated page) |
| cpp/iterator/dsc indirectly_comparable | (see dedicated page) |
| cpp/iterator/dsc permutable | (see dedicated page) |
| cpp/iterator/dsc mergeable | (see dedicated page) |
| cpp/iterator/dsc sortable | (see dedicated page) |

#### Algorithm utilities

| cpp/iterator/dsc indirect_result_t | (see dedicated page) |
| cpp/iterator/dsc projected | (see dedicated page) |
| cpp/iterator/dsc projected_value_t | (see dedicated page) |

#### Associated types

| cpp/iterator/dsc incrementable_traits | (see dedicated page) |
| cpp/iterator/dsc indirectly_readable_traits | (see dedicated page) |
| cpp/iterator/dsc iter_t | (see dedicated page) |

#### Primitives

| cpp/iterator/dsc iterator_traits | (see dedicated page) |
| cpp/iterator/dsc iterator_tags | (see dedicated page) |
| cpp/iterator/dsc iterator | (see dedicated page) |

#### Adaptors

| cpp/iterator/dsc reverse_iterator | (see dedicated page) |
| cpp/iterator/dsc move_iterator | (see dedicated page) |
| cpp/iterator/dsc move_sentinel | (see dedicated page) |
| cpp/iterator/dsc basic_const_iterator | (see dedicated page) |
| cpp/iterator/dsc const_iterator | (see dedicated page) |
| cpp/iterator/dsc const_sentinel | (see dedicated page) |
| cpp/iterator/dsc common_iterator | (see dedicated page) |
| cpp/iterator/dsc default_sentinel_t | (see dedicated page) |
| cpp/iterator/dsc counted_iterator | (see dedicated page) |
| cpp/iterator/dsc unreachable_sentinel_t | (see dedicated page) |
| cpp/iterator/dsc back_insert_iterator | (see dedicated page) |
| cpp/iterator/dsc front_insert_iterator | (see dedicated page) |
| cpp/iterator/dsc insert_iterator | (see dedicated page) |

#### Stream Iterators

| cpp/iterator/dsc istream_iterator | (see dedicated page) |
| cpp/iterator/dsc ostream_iterator | (see dedicated page) |
| cpp/iterator/dsc istreambuf_iterator | (see dedicated page) |
| cpp/iterator/dsc ostreambuf_iterator | (see dedicated page) |
| std::ranges | |
| cpp/iterator/ranges/dsc iter_move | (see dedicated page) |
| cpp/iterator/ranges/dsc iter_swap | (see dedicated page) |
| cpp/iterator/dsc unreachable_sentinel | (see dedicated page) |
| cpp/iterator/dsc default_sentinel | (see dedicated page) |

#### Adaptors

| cpp/iterator/dsc make_reverse_iterator | (see dedicated page) |
| cpp/iterator/dsc make_move_iterator | (see dedicated page) |
| cpp/iterator/dsc make_const_iterator | (see dedicated page) |
| cpp/iterator/dsc make_const_sentinel | (see dedicated page) |
| cpp/iterator/dsc front_inserter | (see dedicated page) |
| cpp/iterator/dsc back_inserter | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |

#### Non-member operators

| cpp/iterator/adaptor/dsc operator cmp|move_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator+|move_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator-|move_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator cmp|reverse_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator+|reverse_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator-|reverse_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator cmp|counted_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator+|counted_iterator | (see dedicated page) |
| cpp/iterator/adaptor/dsc operator-|counted_iterator | (see dedicated page) |
| cpp/iterator/istream_iterator/dsc operator cmp | (see dedicated page) |
| cpp/iterator/istreambuf_iterator/dsc operator cmp | (see dedicated page) |

#### Operations

| cpp/iterator/dsc advance | (see dedicated page) |
| cpp/iterator/dsc distance | (see dedicated page) |
| cpp/iterator/dsc next | (see dedicated page) |
| cpp/iterator/dsc prev | (see dedicated page) |
| cpp/iterator/ranges/dsc advance | (see dedicated page) |
| cpp/iterator/ranges/dsc distance | (see dedicated page) |
| cpp/iterator/ranges/dsc next | (see dedicated page) |
| cpp/iterator/ranges/dsc prev | (see dedicated page) |

#### Range access

| cpp/iterator/dsc begin | (see dedicated page) |
| cpp/iterator/dsc end | (see dedicated page) |
| cpp/iterator/dsc rbegin | (see dedicated page) |
| cpp/iterator/dsc rend | (see dedicated page) |
| cpp/iterator/dsc size | (see dedicated page) |
| cpp/iterator/dsc empty | (see dedicated page) |
| cpp/iterator/dsc data | (see dedicated page) |


## Synopsis


## Defect reports

