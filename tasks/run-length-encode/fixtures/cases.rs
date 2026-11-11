use run_length_encode::run_length_encode;
#[test]
fn spec_cases() {
assert_eq!(run_length_encode(""),"","''");
assert_eq!(run_length_encode("a"),"1a","'a'");
assert_eq!(run_length_encode("aa"),"2a","'aa'");
assert_eq!(run_length_encode("aaab"),"3a1b","'aaab'");
assert_eq!(run_length_encode("abc"),"1a1b1c","'abc'");
assert_eq!(run_length_encode("aabbbcccc"),"2a3b4c","'aabbbcccc'");
assert_eq!(run_length_encode("aaaaaaaaaa"),"10a","'aaaaaaaaaa'");
assert_eq!(run_length_encode("aaaaaaaaaaaab"),"12a1b","'aaaaaaaaaaaab'");
assert_eq!(run_length_encode("AaA"),"1A1a1A","'AaA'");
assert_eq!(run_length_encode("aA"),"1a1A","'aA'");
assert_eq!(run_length_encode("112"),"2112","'112'");
assert_eq!(run_length_encode("  x  "),"2 1x2 ","'  x  '");
assert_eq!(run_length_encode("\t\t\n"),"2\t1\n","'\\t\\t\\n'");
assert_eq!(run_length_encode("ééé"),"3é","'ééé'");
assert_eq!(run_length_encode("e\u{301}e\u{301}"),"1e1\u{301}1e1\u{301}","'e\u{301}e\u{301}'");
assert_eq!(run_length_encode("🚀🚀x"),"2🚀1x","'🚀🚀x'");
assert_eq!(run_length_encode("ßß"),"2ß","'ßß'");
assert_eq!(run_length_encode("a b"),"1a1 1b","'a b'");
assert_eq!(run_length_encode("xyyzzz"),"1x2y3z","'xyyzzz'");
assert_eq!(run_length_encode("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"),"36z","'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'");
assert_eq!(run_length_encode("日日本"),"2日1本","'日日本'");
assert_eq!(run_length_encode("abba"),"1a2b1a","'abba'");
assert_eq!(run_length_encode("\u{0}\u{0}a"),"2\u{0}1a","'\\x00\\x00a'");
assert_eq!(run_length_encode("\r\n\r\n"),"1\r1\n1\r1\n","'\\r\\n\\r\\n'");
assert_eq!(run_length_encode("11111"),"51","'11111'");
assert_eq!(run_length_encode("\u{a0}\u{a0}"),"2\u{a0}","'\\xa0\\xa0'");
let long="x".repeat(5000);assert_eq!(run_length_encode(&long),"5000x");
let alt="ab".repeat(3000);assert_eq!(run_length_encode(&alt),"1a1b".repeat(3000));
let mixed=format!("{}{}{}","q".repeat(123)," ".repeat(10),"\u{1F680}".repeat(1000));assert_eq!(run_length_encode(&mixed),"123q10 1000\u{1F680}");
for _ in 0..3 {assert_eq!(run_length_encode("wwwwaaadexxxxxx"),"4w3a1d1e6x");}
}
