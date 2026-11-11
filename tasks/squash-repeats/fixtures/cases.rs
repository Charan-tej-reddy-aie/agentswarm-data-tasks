use squash_repeats::squash_repeats;
#[test]
fn spec_cases() {
assert_eq!(squash_repeats(""),"","''");
assert_eq!(squash_repeats("a"),"a","'a'");
assert_eq!(squash_repeats("aa"),"a","'aa'");
assert_eq!(squash_repeats("aaa"),"a","'aaa'");
assert_eq!(squash_repeats("aab"),"ab","'aab'");
assert_eq!(squash_repeats("abba"),"aba","'abba'");
assert_eq!(squash_repeats("aabbcc"),"abc","'aabbcc'");
assert_eq!(squash_repeats("aaabbbaaa"),"aba","'aaabbbaaa'");
assert_eq!(squash_repeats("Aa"),"Aa","'Aa'");
assert_eq!(squash_repeats("AAaa"),"Aa","'AAaa'");
assert_eq!(squash_repeats("hello  world"),"helo world","'hello  world'");
assert_eq!(squash_repeats("  x  ")," x ","'  x  '");
assert_eq!(squash_repeats("\t\t\n\n"),"\t\n","'\\t\\t\\n\\n'");
assert_eq!(squash_repeats("1122"),"12","'1122'");
assert_eq!(squash_repeats("éée"),"ée","'éée'");
assert_eq!(squash_repeats("e\u{301}\u{301}"),"e\u{301}","'e\u{301}\u{301}'");
assert_eq!(squash_repeats("🚀🚀x"),"🚀x","'🚀🚀x'");
assert_eq!(squash_repeats("🚀🚁"),"🚀🚁","'🚀🚁'");
assert_eq!(squash_repeats("日日本"),"日本","'日日本'");
assert_eq!(squash_repeats("mississippi"),"misisipi","'mississippi'");
assert_eq!(squash_repeats("__--__"),"_-_","'__--__'");
assert_eq!(squash_repeats("0000"),"0","'0000'");
assert_eq!(squash_repeats("\u{0}\u{0}a"),"\u{0}a","'\\x00\\x00a'");
assert_eq!(squash_repeats("ab"),"ab","'ab'");
let long="7".repeat(5000);assert_eq!(squash_repeats(&long),"7");
let alt="ab".repeat(2500);assert_eq!(squash_repeats(&alt),alt);
let rockets="\u{1F680}\u{1F680}x".repeat(1000);assert_eq!(squash_repeats(&rockets),"\u{1F680}x".repeat(1000));
for _ in 0..3 {assert_eq!(squash_repeats("x--yy__zz9"),"x-y_z9");}
}
