package binarygap
import "testing"
var _ func(uint32) int = BinaryGap
func TestSpec(t *testing.T) {
cases:=[]struct{in uint32;want int}{
{0,0},
{1,0},
{2,0},
{3,0},
{4,0},
{5,1},
{6,0},
{7,0},
{8,0},
{9,2},
{15,0},
{16,0},
{17,3},
{20,1},
{32,0},
{33,4},
{328,2},
{529,4},
{561,3},
{1041,5},
{1162,3},
{2147483647,0},
{2147483648,0},
{2147483649,30},
{2147483650,29},
{4294967295,0},
{4294967294,0},
{1073741825,29},
{2863311530,1},
{1431655765,1},
{2147516417,15},
{2147483651,29},
{1073741825,29},
{2321,3},
{1073741825,29},
{641,6},
{517,6},
}
for _,c:=range cases { if got:=BinaryGap(c.in);got!=c.want {t.Errorf("%d (%b): got %d want %d",c.in,c.in,got,c.want)};if BinaryGap(c.in)!=c.want {t.Fatal("nondeterministic")}}
for k:=uint(1);k<=30;k++ { n:=uint32(1)|uint32(1)<<(k+1); if got:=BinaryGap(n);got!=int(k) {t.Errorf("1<<%d|1: got %d want %d",k+1,got,k)}; if got:=BinaryGap(n<<(31-(k+1)));got!=int(k) {t.Errorf("shifted gap %d: got %d",k,got)} }
for k:=uint(0);k<32;k++ { if got:=BinaryGap(uint32(1)<<k);got!=0 {t.Errorf("power of two 1<<%d: got %d want 0",k,got)} }
}
