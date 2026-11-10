# Wrap words using Unicode code point widths
Implement export function wrapWords(text, width) in wrap_words.mjs.
Require primitive string text and primitive number width; reject every other
type, including boxed primitives/subclasses, with exact TypeError. Validate both
types first. Then width must be a positive safe integer, otherwise exact
RangeError. Next reject any lone high or low surrogate in text with exact
RangeError (even when there are no words); valid surrogate pairs count as ONE
code point. No normalization or grapheme clustering.
Tokenize ONLY on U+0020 ASCII space, discard empty tokens. Tabs, newlines,
nonbreaking spaces and all other characters are literal parts of words.
Greedily append words to the current line with one ASCII space if the resulting
code point count is <=width; otherwise start a new line. An overlong word stays
whole on its own line; never split words. Return a fresh normal dense Array of
primitive strings; no words returns []. No trailing/leading ASCII spaces.
Examples: ('',3) -> []; ('  a  bb c ',4) -> ['a bb','c'];
('abcd e',2) -> ['abcd','e']; ('😀 a',3) -> ['😀 a'];
('a\tb c',3) -> ['a\tb','c']; ('a\nb c',3) -> ['a\nb','c'];
('a\u00a0b c',3) -> ['a\u00a0b','c']; ('a',0) -> RangeError;
('\ud800',3) -> RangeError; (new String('a'),3) -> TypeError.

Use standard library only. Inputs use ordinary data properties, no accessors or
shadowed Array methods/iterators; extra named Array properties are outside the
contract. Frozen inputs are supported in JS. Exception messages are unconstrained.
Only edit the implementation file and optional IMPLEMENTATION.md in this task.
Every spec example is checked. No README-dependent checks. Public checks need
independent source/scope review. This is a standalone unpaid exercise.

Runtime: Node 22. Quick run from repository root:
`node tasks/wrap-words/check.mjs --solution "$PWD/tasks/wrap-words/wrap_words.mjs"`
The issue provides a separate trusted checker pin and offline Docker command.
Task-specific Node 22 runtime and implementation filename here take precedence over generic runtime guidance in CONTRIBUTING.md.
