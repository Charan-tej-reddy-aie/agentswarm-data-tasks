package atbash
import "testing"
var _ func(string) string = Atbash
func TestSpec(t *testing.T) {
cases:=[]struct{in,want string}{
{"",""},
{"a","z"},
{"z","a"},
{"A","Z"},
{"Z","A"},
{"abc","zyx"},
{"xyz","cba"},
{"Hello, World!","Svool, Dliow!"},
{"Wizard","Draziw"},
{"123 abc XYZ","123 zyx CBA"},
{"\tTab\n","\tGzy\n"},
{"é","é"},
{"Éa","Éz"},
{"café","xzué"},
{"CAFÉ","XZUÉ"},
{"ß","ß"},
{"ǅx","ǅc"},
{"日本語abc","日本語zyx"},
{"🚀Go🚀","🚀Tl🚀"},
{"Σσς","Σσς"},
{"ＡＢｃ","ＡＢｃ"},
{"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxY","ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccB"},
{"The Quick Brown Fox","Gsv Jfrxp Yildm Ulc"},
{"@[`{","@[`{"},
{"mN nM","nM mN"},
{"ıİ","ıİ"},
}
for _,c:=range cases { if got:=Atbash(c.in);got!=c.want {t.Errorf("%q: got %q want %q",c.in,got,c.want)};if Atbash(c.want)!=c.in {t.Errorf("%q: not an involution",c.want)};if Atbash(c.in)!=c.want {t.Fatal("nondeterministic")}}
raw:=[]struct{in,want string}{
{"\xff","\xff"},
{"a\xffB","z\xffY"},
{"\xe6\x97z","\xe6\x97a"},
{"\xffé","\xffé"},
}
for _,c:=range raw { if got:=Atbash(c.in);got!=c.want {t.Errorf("%q: got %q want %q",c.in,got,c.want)} }
}
