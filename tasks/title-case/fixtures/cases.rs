use title_case::title_case;
#[test]
fn spec_cases() {
assert_eq!(title_case(""),"");
assert_eq!(title_case("a"),"A");
assert_eq!(title_case("hello world"),"Hello World");
assert_eq!(title_case("HELLO WORLD"),"Hello World");
assert_eq!(title_case("hELLO wORLD"),"Hello World");
assert_eq!(title_case("  two  spaces "),"  Two  Spaces ");
assert_eq!(title_case(" ")," ");
assert_eq!(title_case("   "),"   ");
assert_eq!(title_case("x y z"),"X Y Z");
assert_eq!(title_case("o'neil mc-donald"),"O'neil Mc-donald");
assert_eq!(title_case("123abc DEF"),"123abc Def");
assert_eq!(title_case("tab\tsep word"),"Tab\tsep Word");
assert_eq!(title_case("line\nbreak x"),"Line\nbreak X");
assert_eq!(title_case("a\u{a0}b c"),"A\u{a0}b C");
assert_eq!(title_case("élan vital"),"élan Vital");
assert_eq!(title_case("ß straße"),"ß Straße");
assert_eq!(title_case("aİ İa"),"Aİ İa");
assert_eq!(title_case("ǆemal x"),"ǆemal X");
assert_eq!(title_case("ÉCOLE ÉTÉ"),"École ÉtÉ");
assert_eq!(title_case("camelCase Words"),"Camelcase Words");
assert_eq!(title_case("__init__ main"),"__init__ Main");
assert_eq!(title_case("A"),"A");
assert_eq!(title_case("zZ Zz"),"Zz Zz");
assert_eq!(title_case("🚀rocket go"),"🚀rocket Go");
assert_eq!(title_case("e\u{301}té x"),"E\u{301}té X");
assert_eq!(title_case("\u{0}nul x"),"\u{0}nul X");
let long="ab ".repeat(300);assert_eq!(title_case(&long),"Ab ".repeat(300));
let mut first=title_case("aa bb");first.clear();assert_eq!(title_case("aa bb"),"Aa Bb");
}
