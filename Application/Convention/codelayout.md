# Code Lay-out

## Indentation

_Sử dụng 4 dấu cách cho mỗi cấp của code_

-> Thật sự là mình cũng chỉ hiểu nó như thế này, mặc dù ở trong phần pep8 của python họ có đề xuất một số trường hợp khác nữa mà cần sử dụng dấu cách.

### Maximum Line Length

79 ký tự :). Mình đọc đúc kết được mỗi điều này, nhiều nhất 979 ký tự một dòng nhé.

### Should a Line Break Before or After a Binary Operator?

Trong một số trường hợp phép tính toán tử của bạn quá bị dài và phải break nó thành các dòng nhỏ hơn để.

Vậy mình nên break như thế nào? Câu trả lời là chia theo toán tử nhé. Có lẽ mình chỉ cần nhớ đến thế thôi nhé.

### Source File Encoding

Các chúng ta import một package ngoài thôi á, tách các import ra.

## Comment

### Block Comments

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

Paragraphs inside a block comment are separated by a line containing a single #.

### Inline Comments

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they state the obvious.

## Naming Convention
