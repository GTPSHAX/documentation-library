---
title: cstdio
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/cstdio
---

This header is part of the C-style input/output library.


| cpp/io/c/dsc FILE | (see dedicated page) |
| cpp/io/c/dsc fpos_t | (see dedicated page) |
| cpp/types/dsc size_t | (see dedicated page) |
| cpp/types/dsc NULL | (see dedicated page) |
| cpp/io/c/dsc std streams | (see dedicated page) |

#### File access

| cpp/io/c/dsc fopen | (see dedicated page) |
| cpp/io/c/dsc freopen | (see dedicated page) |
| cpp/io/c/dsc fclose | (see dedicated page) |
| cpp/io/c/dsc fflush | (see dedicated page) |
| cpp/io/c/dsc setbuf | (see dedicated page) |
| cpp/io/c/dsc setvbuf | (see dedicated page) |

#### Direct input/output

| cpp/io/c/dsc fread | (see dedicated page) |
| cpp/io/c/dsc fwrite | (see dedicated page) |

#### Unformatted input/output


#### {{small|Narrow character

| cpp/io/c/dsc fgetc | (see dedicated page) |
| cpp/io/c/dsc fgets | (see dedicated page) |
| cpp/io/c/dsc fputc | (see dedicated page) |
| cpp/io/c/dsc fputs | (see dedicated page) |
| cpp/io/c/dsc getchar | (see dedicated page) |
| cpp/io/c/dsc gets | (see dedicated page) |
| cpp/io/c/dsc putchar | (see dedicated page) |
| cpp/io/c/dsc puts | (see dedicated page) |
| cpp/io/c/dsc ungetc | (see dedicated page) |

#### Formatted input/output


#### {{small|Narrow/multibyte character

| cpp/io/c/dsc fscanf | (see dedicated page) |
| cpp/io/c/dsc vfscanf | (see dedicated page) |
| cpp/io/c/dsc fprintf | (see dedicated page) |
| cpp/io/c/dsc vfprintf | (see dedicated page) |

#### File positioning

| cpp/io/c/dsc ftell | (see dedicated page) |
| cpp/io/c/dsc fgetpos | (see dedicated page) |
| cpp/io/c/dsc fseek | (see dedicated page) |
| cpp/io/c/dsc fsetpos | (see dedicated page) |
| cpp/io/c/dsc rewind | (see dedicated page) |

#### Error handling

| cpp/io/c/dsc clearerr | (see dedicated page) |
| cpp/io/c/dsc feof | (see dedicated page) |
| cpp/io/c/dsc ferror | (see dedicated page) |
| cpp/io/c/dsc perror | (see dedicated page) |

#### Operations on files

| cpp/io/c/dsc remove | (see dedicated page) |
| cpp/io/c/dsc rename | (see dedicated page) |
| cpp/io/c/dsc tmpfile | (see dedicated page) |
| cpp/io/c/dsc tmpnam | (see dedicated page) |


## Synopsis


```cpp
#define __STDC_VERSION_STDIO_H__ 202311L

namespace std {
  using size_t = /* see description */;
  using FILE = /* see description */;
  using fpos_t = /* see description */;
}

#define NULL         /* see description */
#define _IOFBF       /* see description */
#define _IOLBF       /* see description */
#define _IONBF       /* see description */
#define BUFSIZ       /* see description */
#define EOF          /* see description */
#define FOPEN_MAX    /* see description */
#define FILENAME_MAX /* see description */
#define L_tmpnam     /* see description */
#define SEEK_CUR     /* see description */
#define SEEK_END     /* see description */
#define SEEK_SET     /* see description */
#define TMP_MAX      /* see description */

#define stdin        /* see description */
#define stdout       /* see description */
#define stderr       /* see description */

#define _PRINTF_NAN_LEN_MAX /* see description */

namespace std {
  int remove(const char* filename);
  int rename(const char* old_p, const char* new_p);
  FILE* tmpfile();
  char* tmpnam(char* s);
  int fclose(FILE* stream);
  int fflush(FILE* stream);
  FILE* fopen(const char* filename, const char* mode);
  FILE* freopen(const char* filename, const char* mode, FILE* stream);
  void setbuf(FILE* stream, char* buf);
  int setvbuf(FILE* stream, char* buf, int mode, size_t size);
  int fprintf(FILE* stream, const char* format, ...);
  int fscanf(FILE* stream, const char* format, ...);
  int printf(const char* format, ...);
  int scanf(const char* format, ...);
  int snprintf(char* s, size_t n, const char* format, ...);
  int sprintf(char* s, const char* format, ...);
  int sscanf(const char* s, const char* format, ...);
  int vfprintf(FILE* stream, const char* format, va_list arg);
  int vfscanf(FILE* stream, const char* format, va_list arg);
  int vprintf(const char* format, va_list arg);
  int vscanf(const char* format, va_list arg);
  int vsnprintf(char* s, size_t n, const char* format, va_list arg);
  int vsprintf(char* s, const char* format, va_list arg);
  int vsscanf(const char* s, const char* format, va_list arg);
  int fgetc(FILE* stream);
  char* fgets(char* s, int n, FILE* stream);
  int fputc(int c, FILE* stream);
  int fputs(const char* s, FILE* stream);
  int getc(FILE* stream);
  int getchar();
  int putc(int c, FILE* stream);
  int putchar(int c);
  int puts(const char* s);
  int ungetc(int c, FILE* stream);
  size_t fread(void* ptr, size_t size, size_t nmemb, FILE* stream);
  size_t fwrite(const void* ptr, size_t size, size_t nmemb, FILE* stream);
  int fgetpos(FILE* stream, fpos_t* pos);
  int fseek(FILE* stream, long int offset, int whence);
  int fsetpos(FILE* stream, const fpos_t* pos);
  long int ftell(FILE* stream);
  void rewind(FILE* stream);
  void clearerr(FILE* stream);
  int feof(FILE* stream);
  int ferror(FILE* stream);
  void perror(const char* s);
}
```


## Notes

* `NULL` is also defined in the following headers:
**
**
**
**
**
**
* `std::size_t` is also defined in the following headers:
**
**
**
**
**  <sup>(C++17)</sup>
**
