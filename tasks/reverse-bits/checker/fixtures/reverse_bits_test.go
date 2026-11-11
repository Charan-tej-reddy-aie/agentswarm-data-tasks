package reversebits
import "testing"
var _ func(uint32) uint32 = ReverseBits
func TestSpec(t *testing.T) {
cases:=[]struct{in uint32;want uint32}{
{0,0},
{1,2147483648},
{2,1073741824},
{3,3221225472},
{4,536870912},
{8,268435456},
{15,4026531840},
{255,4278190080},
{256,8388608},
{65280,16711680},
{252645135,4042322160},
{4042322160,252645135},
{43261596,964176192},
{4294967293,3221225471},
{4294967295,4294967295},
{4294967294,2147483647},
{2147483648,1},
{2147483649,2147483649},
{1431655765,2863311530},
{2863311530,1431655765},
{305419896,510274632},
{2147483649,2147483649},
{65536,32768},
{65535,4294901760},
{4294901760,65535},
{305419896,510274632},
{123456789,2830359264},
{987654321,2367060828},
{3000000000,7998285},
{3735928559,4152210811},
}
for _,c:=range cases { if got:=ReverseBits(c.in);got!=c.want {t.Errorf("%d (%032b): got %032b want %032b",c.in,c.in,got,c.want)};if ReverseBits(c.in)!=c.want {t.Fatal("nondeterministic")} }
for k:=uint(0);k<32;k++ { if got:=ReverseBits(uint32(1)<<k);got!=uint32(1)<<(31-k) {t.Errorf("1<<%d: got %032b",k,got)} }
for _,n:=range []uint32{0,1,7,43261596,0xdeadbeef,4294967295,2147483648} { if got:=ReverseBits(ReverseBits(n));got!=n {t.Errorf("not an involution at %d: %d",n,got)} }
}
