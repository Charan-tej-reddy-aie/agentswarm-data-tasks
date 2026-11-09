# Resolve a JSON Pointer against an offline document

Implement `json_pointer_get(document, pointer)` in `json_pointer.py` using Python
3.11+ standard library only. No files, network, packages or clock. Only edit this
implementation and optional task-local `IMPLEMENTATION.md`. This is a standalone
RFC 6901 string-pointer lookup helper; production integration is not claimed.

The document is guaranteed to be a finite, acyclic JSON tree: exact built-in dict
with string keys, list, str, int, float, bool or None; numbers are finite. Document
validation is outside this contract. Pointer must have exact built-in type str
(subclasses are rejected with TypeError). Error messages are unconstrained.

The empty pointer returns the document itself. Every other pointer must start
with ASCII `/`, otherwise raise ValueError. Split after that first slash at each
literal slash, preserving empty tokens. Decode each token left to right: `~0`
becomes `~` and `~1` becomes `/`. Every other tilde sequence, including a terminal
tilde, raises ValueError. Decode once only: `~01` becomes the literal `~1`, not
slash. Validate ALL pointer syntax before attempting traversal; invalid escape
syntax wins even if an earlier token would be missing. URI fragment notation
and percent-decoding are not supported: `#/a` is invalid; `%2F` is literal text.

Traverse one decoded token at a time. For a dict, use the exact case-sensitive
string key, including empty strings, Unicode, numeric-looking strings, `-`, and
prototype-looking names. For a list, the token must be ASCII `0` or a nonzero
ASCII digit followed by zero or more ASCII digits. Leading zeros, signs,
whitespace, Unicode digits, empty tokens and `-` do not identify array items.
An index must be strictly less than the list length. Arbitrarily long digit
tokens are valid syntax but still absent if out of bounds. Raise KeyError for
any absent key/index, invalid array index token, or attempt to descend through
a scalar. Do not expose IndexError, OverflowError or integer-conversion limits.

Return the resolved value without coercion, copying, normalization or mutation.
Containers may alias the original document: this is a read-only lookup. Examples:
`json_pointer_get({'a/b': {'~': 7}}, '/a~1b/~0') == 7`;
`json_pointer_get({'': [9]}, '//0') == 9`. Empty objects/lists are valid results.
Repeated calls must give equal values and leave the document unchanged.

Run `python3 tasks/json-pointer/check.py --solution "$PWD/tasks/json-pointer/json_pointer.py"`.
Acceptance includes at least 60 exact synthetic cases covering Unicode, escapes,
arrays, syntax precedence and malformed types. Public cases can be overfit;
source/scope review accompanies the check. Checks are not a security sandbox.
