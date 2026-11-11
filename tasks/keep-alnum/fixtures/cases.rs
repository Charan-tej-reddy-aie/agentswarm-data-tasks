use keep_alnum::keep_alnum;
#[test]
fn spec_cases() {
assert_eq!(keep_alnum(""),"","''");
assert_eq!(keep_alnum("abc"),"abc","'abc'");
assert_eq!(keep_alnum("a b c"),"abc","'a b c'");
assert_eq!(keep_alnum("Hello, World!"),"HelloWorld","'Hello, World!'");
assert_eq!(keep_alnum("snake_case"),"snakecase","'snake_case'");
assert_eq!(keep_alnum("kebab-case"),"kebabcase","'kebab-case'");
assert_eq!(keep_alnum("0042"),"0042","'0042'");
assert_eq!(keep_alnum("v1.2.3"),"v123","'v1.2.3'");
assert_eq!(keep_alnum("été"),"t","'été'");
assert_eq!(keep_alnum("café"),"caf","'café'");
assert_eq!(keep_alnum("١٢"),"","'١٢'");
assert_eq!(keep_alnum("１ａ"),"","'１ａ'");
assert_eq!(keep_alnum("x🚀y"),"xy","'x🚀y'");
assert_eq!(keep_alnum("\t1\n2 "),"12","'\\t1\\n2 '");
assert_eq!(keep_alnum("ABCxyz09"),"ABCxyz09","'ABCxyz09'");
assert_eq!(keep_alnum("____"),"","'____'");
assert_eq!(keep_alnum("e\u{301}"),"e","'e\u{301}'");
assert_eq!(keep_alnum("!@#$%"),"","'!@#$%'");
assert_eq!(keep_alnum("Z9"),"Z9","'Z9'");
assert_eq!(keep_alnum("  "),"","'  '");
let long="a-1_".repeat(2500);assert_eq!(keep_alnum(&long),"a1".repeat(2500));
let rockets="\u{1F680}z".repeat(1000);assert_eq!(keep_alnum(&rockets),"z".repeat(1000));
for _ in 0..3 {assert_eq!(keep_alnum("x--yy__zz9"),"xyyzz9");}
}
