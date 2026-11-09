package durationformat
import "testing"
var _ func(int64) string = FormatSeconds
func TestSpec(t *testing.T) {
cases:=[]struct{seconds int64;want string}{
{-9223372036854775808,"invalid"},
{-86400,"invalid"},
{-1,"invalid"},
{0,"0s"},
{1,"1s"},
{59,"59s"},
{60,"1m"},
{61,"1m 1s"},
{3599,"59m 59s"},
{3600,"1h"},
{3601,"1h 1s"},
{3661,"1h 1m 1s"},
{86399,"23h 59m 59s"},
{86400,"1d"},
{90061,"1d 1h 1m 1s"},
{172801,"2d 1s"},
{9223372036854775807,"106751991167300d 15h 30m 7s"},
{2,"2s"},
{9,"9s"},
{16,"16s"},
{23,"23s"},
{30,"30s"},
{37,"37s"},
{44,"44s"},
{51,"51s"},
{58,"58s"},
{65,"1m 5s"},
{72,"1m 12s"},
{79,"1m 19s"},
{86,"1m 26s"},
{93,"1m 33s"},
{100,"1m 40s"},
{107,"1m 47s"},
{114,"1m 54s"},
}
for _,c:=range cases { if got:=FormatSeconds(c.seconds);got!=c.want {t.Errorf("%d: got %q want %q",c.seconds,got,c.want)};if FormatSeconds(c.seconds)!=c.want {t.Fatal("nondeterministic")}}
}
