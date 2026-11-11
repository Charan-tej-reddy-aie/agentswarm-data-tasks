package graycode
import "testing"
var _ func(uint32) uint32 = GrayCode
func TestSpec(t *testing.T) {
cases:=[]struct{in uint32;want uint32}{
{0,0},
{1,1},
{2,3},
{3,2},
{4,6},
{5,7},
{6,5},
{7,4},
{8,12},
{12,10},
{15,8},
{16,24},
{40,60},
{96,80},
{255,128},
{256,384},
{65280,32896},
{252645135,143165576},
{4042322160,2290649224},
{43261596,64885202},
{4294967295,2147483648},
{4294967294,2147483649},
{2147483648,3221225472},
{2147483649,3221225473},
{1431655765,2147483647},
{2863311530,4294967295},
{305419896,456031556},
{2147483649,3221225473},
{65536,98304},
{4294901760,2147516416},
{123456789,83241887},
{3000000000,3954733312},
{3735928559,2986041752},
}
for _,c:=range cases { if got:=GrayCode(c.in);got!=c.want {t.Errorf("%d (%032b): got %032b want %032b",c.in,c.in,got,c.want)};if GrayCode(c.in)!=c.want {t.Fatal("nondeterministic")} }
for k:=uint(0);k<32;k++ { n:=uint32(1)<<k;want:=n|n>>1;if got:=GrayCode(n);got!=want {t.Errorf("1<<%d: got %032b",k,got)} }
for n:=uint32(0);n<4096;n++ { d:=GrayCode(n)^GrayCode(n+1);if d==0||d&(d-1)!=0 {t.Errorf("codes of %d and %d differ in %032b",n,n+1,d)} }
}
