use reverse_words::reverse_words;
#[test]
fn spec_cases() {
assert_eq!(reverse_words(""),"","''");
assert_eq!(reverse_words("   "),"","'   '");
assert_eq!(reverse_words("one"),"one","'one'");
assert_eq!(reverse_words("one two"),"two one","'one two'");
assert_eq!(reverse_words("one two three"),"three two one","'one two three'");
assert_eq!(reverse_words("  lead and trail  "),"trail and lead","'  lead and trail  '");
assert_eq!(reverse_words("a\tb\nc"),"c b a","'a\\tb\\nc'");
assert_eq!(reverse_words("a\r\nb"),"b a","'a\\r\\nb'");
assert_eq!(reverse_words("x\u{a0}y"),"y x","'x\\xa0y'");
assert_eq!(reverse_words("x　y"),"y x","'x\\u3000y'");
assert_eq!(reverse_words("x y"),"y x","'x\\u2003y'");
assert_eq!(reverse_words("tab\t\tgap"),"gap tab","'tab\\t\\tgap'");
assert_eq!(reverse_words("Hello, world!"),"world! Hello,","'Hello, world!'");
assert_eq!(reverse_words("don't stop me"),"me stop don't","\"don't stop me\"");
assert_eq!(reverse_words("é ß Σ"),"Σ ß é","'é ß Σ'");
assert_eq!(reverse_words("🚀 go 🚀"),"🚀 go 🚀","'🚀 go 🚀'");
assert_eq!(reverse_words("a b a b"),"b a b a","'a b a b'");
assert_eq!(reverse_words("same same"),"same same","'same same'");
assert_eq!(reverse_words("12 34 56"),"56 34 12","'12 34 56'");
assert_eq!(reverse_words("word​joined"),"word​joined","'word\\u200bjoined'");
assert_eq!(reverse_words("a  b   c"),"c b a","'a  b   c'");
assert_eq!(reverse_words("\nnew\nlines\n"),"lines new","'\\nnew\\nlines\\n'");
assert_eq!(reverse_words("single-word"),"single-word","'single-word'");
assert_eq!(reverse_words("xy"),"y x","'x\\x85y'");
assert_eq!(reverse_words("e\u{301} x"),"x e\u{301}","'e\u{301} x'");
assert_eq!(reverse_words("x\u{1f}y"),"x\u{1f}y","'x\\x1fy'");
let long="ab ".repeat(5000);assert_eq!(reverse_words(&long),["ab"; 5000].join(" "));
let words:Vec<String>=(0..3000).map(|i| format!("w{}",i)).collect();let rev:Vec<String>=words.iter().rev().cloned().collect();assert_eq!(reverse_words(&words.join("\t")),rev.join(" "));
for _ in 0..3 {assert_eq!(reverse_words("the sky is blue"),"blue is sky the");}
}
