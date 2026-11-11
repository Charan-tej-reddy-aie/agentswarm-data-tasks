use pangram::is_pangram;
#[test]
fn spec_cases() {
assert_eq!(is_pangram(""),false,"''");
assert_eq!(is_pangram("a"),false,"'a'");
assert_eq!(is_pangram("abcdefghijklmnopqrstuvwxyz"),true,"'abcdefghijklmnopqrstuvwxyz'");
assert_eq!(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),true,"'ABCDEFGHIJKLMNOPQRSTUVWXYZ'");
assert_eq!(is_pangram("The quick brown fox jumps over the lazy dog"),true,"'The quick brown fox jumps over the lazy dog'");
assert_eq!(is_pangram("The quick brown fox jumps over the lay dog"),false,"'The quick brown fox jumps over the lay dog'");
assert_eq!(is_pangram("abcdefghijklmnopqrstuvwxy"),false,"'abcdefghijklmnopqrstuvwxy'");
assert_eq!(is_pangram("bcdefghijklmnopqrstuvwxyz"),false,"'bcdefghijklmnopqrstuvwxyz'");
assert_eq!(is_pangram("Pack my box with five dozen liquor jugs"),true,"'Pack my box with five dozen liquor jugs'");
assert_eq!(is_pangram("a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z"),true,"'a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z'");
assert_eq!(is_pangram("aBcDeFgHiJkLmNoPqRsTuVwXyZ"),true,"'aBcDeFgHiJkLmNoPqRsTuVwXyZ'");
assert_eq!(is_pangram("abcdefghijklmnopqrstuvwxyé"),false,"'abcdefghijklmnopqrstuvwxyé'");
assert_eq!(is_pangram("ÀBCDEFGHIJKLMNOPQRSTUVWXYZ"),false,"'ÀBCDEFGHIJKLMNOPQRSTUVWXYZ'");
assert_eq!(is_pangram("abcdefghijklm\nnopqrstuvwxyz"),true,"'abcdefghijklm\\nnopqrstuvwxyz'");
assert_eq!(is_pangram("012345678901234567890123456789"),false,"'012345678901234567890123456789'");
assert_eq!(is_pangram("zyxwvutsrqponmlkjihgfedcba!"),true,"'zyxwvutsrqponmlkjihgfedcba!'");
assert_eq!(is_pangram("abcdefghijklmnopqrstuvwxy\tz"),true,"'abcdefghijklmnopqrstuvwxy\\tz'");
assert_eq!(is_pangram("abcdefghijklmnopqrstuvwxyź"),false,"'abcdefghijklmnopqrstuvwxyź'");
assert_eq!(is_pangram("                              "),false,"'                              '");
assert_eq!(is_pangram("abababababababababababababababababababab"),false,"'abababababababababababababababababababab'");
assert_eq!(is_pangram("Sphinx of black quartz, judge my vow"),true,"'Sphinx of black quartz, judge my vow'");
assert_eq!(is_pangram("How vexingly quick daft zebras jump!"),true,"'How vexingly quick daft zebras jump!'");
assert_eq!(is_pangram("abcdefghijklnopqrstuvwxyz"),false,"'abcdefghijklnopqrstuvwxyz'");
assert_eq!(is_pangram("éabcdefghijklmnopqrstuvwxyz"),true,"'éabcdefghijklmnopqrstuvwxyz'");
assert_eq!(is_pangram("Ⅹabcdefghijklmnopqrstuvwxy"),false,"'Ⅹabcdefghijklmnopqrstuvwxy'");
assert_eq!(is_pangram("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"),true,"'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'");
let long=format!("{}{}", "é".repeat(5000), "abcdefghijklmnopqrstuvwxyz");assert!(is_pangram(&long));
let missing=format!("{}{}", "abcdefghijklmnopqrstuvwxy-".repeat(500), "Ź");assert!(!is_pangram(&missing));
let late=format!("{}Z", "abcdefghijklmnopqrstuvwxy ".repeat(400));assert!(is_pangram(&late));
for _ in 0..3 {assert!(is_pangram("Sphinx of black quartz, judge my vow"));assert!(!is_pangram("Sphinx of black quarts, judge my vow"));}
}
