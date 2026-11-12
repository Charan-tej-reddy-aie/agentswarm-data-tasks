use mask_card::mask_card;
#[test]
fn spec_cases() {
assert_eq!(mask_card(""),"","''");
assert_eq!(mask_card("a"),"a","'a'");
assert_eq!(mask_card("abcd"),"abcd","'abcd'");
assert_eq!(mask_card("abcde"),"#bcde","'abcde'");
assert_eq!(mask_card("4556364607935616"),"############5616","'4556364607935616'");
assert_eq!(mask_card("64607935616"),"#######5616","'64607935616'");
assert_eq!(mask_card("1"),"1","'1'");
assert_eq!(mask_card("12345"),"#2345","'12345'");
assert_eq!(mask_card("Skippy"),"##ippy","'Skippy'");
assert_eq!(mask_card("Nananananananananananananananana Batman!"),"####################################man!","'Nananananananananananananananana Batman!'");
assert_eq!(mask_card("  x  "),"# x  ","'  x  '");
assert_eq!(mask_card("1234 5678 9012 3456"),"###############3456","'1234 5678 9012 3456'");
assert_eq!(mask_card("ééééé"),"#éééé","'ééééé'");
assert_eq!(mask_card("e\u{301}e\u{301}e\u{301}"),"##e\u{301}e\u{301}","'e\u{301}e\u{301}e\u{301}'");
assert_eq!(mask_card("🚀🚀🚀🚀🚀"),"#🚀🚀🚀🚀","'🚀🚀🚀🚀🚀'");
assert_eq!(mask_card("🚀🚀🚀🚀🚀🚀"),"##🚀🚀🚀🚀","'🚀🚀🚀🚀🚀🚀'");
assert_eq!(mask_card("日本語の文字"),"##語の文字","'日本語の文字'");
assert_eq!(mask_card("####"),"####","'####'");
assert_eq!(mask_card("\t\n\r\n\t"),"#\n\r\n\t","'\\t\\n\\r\\n\\t'");
assert_eq!(mask_card("abc\u{0}def"),"###\u{0}def","'abc\\x00def'");
assert_eq!(mask_card("1234-5678"),"#####5678","'1234-5678'");
assert_eq!(mask_card("\u{a0}\u{a0}\u{a0}\u{a0}\u{a0}"),"#\u{a0}\u{a0}\u{a0}\u{a0}","'\\xa0\\xa0\\xa0\\xa0\\xa0'");
let long="7".repeat(5000);assert_eq!(mask_card(&long),format!("{}7777","#".repeat(4996)));
let rockets="\u{1F680}".repeat(1000);assert_eq!(mask_card(&rockets),format!("{}{}","#".repeat(996),"\u{1F680}".repeat(4)));
for _ in 0..3 {assert_eq!(mask_card("secret-pin-0042"),"###########0042");}
}
