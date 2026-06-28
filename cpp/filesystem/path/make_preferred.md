---
title: std::filesystem::path::make_preferred
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/make_preferred
---

ddcl | since=c++17 |
path& make_preferred();
Converts all directory separators in the generic-format view of the path to the preferred directory separator.
For example, on Windows, where `\` is the preferred separator, the path `foo/bar` will be converted to `foo\bar`.

## Parameters

(none)

## Return value

`*this`

## Example


## See also

