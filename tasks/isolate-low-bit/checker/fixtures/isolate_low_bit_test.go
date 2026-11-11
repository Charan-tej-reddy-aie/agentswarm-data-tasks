package isolatelowbit
import "testing"
var _ func(uint32) uint32 = IsolateLowBit
func TestSpec(t *testing.T) {
cases:=[]struct{in uint32;want uint32}{
{0,0},
{1,1},
{2,2},
{3,1},
{4,4},
{5,1},
{6,2},
{7,1},
{8,8},
{12,4},
{15,1},
{16,16},
{40,8},
{96,32},
{255,1},
{256,256},
{65280,256},
{252645135,1},
{4042322160,16},
{43261596,4},
{4294967295,1},
{4294967294,2},
{2147483648,2147483648},
{2147483649,1},
{1431655765,1},
{2863311530,2},
{305419896,8},
{2147483649,1},
{65536,65536},
{4294901760,65536},
{123456789,1},
{3000000000,512},
{3735928559,1},
}
for _,c:=range cases { if got:=IsolateLowBit(c.in);got!=c.want {t.Errorf("%d (%032b): got %032b want %032b",c.in,c.in,got,c.want)};if IsolateLowBit(c.in)!=c.want {t.Fatal("nondeterministic")} }
for k:=uint(0);k<32;k++ { n:=uint32(1)<<k;if got:=IsolateLowBit(n);got!=n {t.Errorf("1<<%d: got %032b",k,got)};if got:=IsolateLowBit(^uint32(0)<<k);got!=n {t.Errorf("ones<<%d: got %032b",k,got)} }
}
