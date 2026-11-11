package main
import ("flag"; "fmt"; "os"; "os/exec"; "path/filepath"; "runtime")
func main() {
    source := flag.String("solution", "", "candidate gray_code.go"); flag.Parse()
    if *source == "" { panic("--solution required") }
    _, own, _, _ := runtime.Caller(0)
    root, err := os.MkdirTemp("", "gray-code-check-"); if err != nil { panic(err) }; defer os.RemoveAll(root)
    for name, src := range map[string]string{"gray_code.go":*source,"gray_code_test.go":filepath.Join(filepath.Dir(own),"fixtures","gray_code_test.go")} {
        data, err := os.ReadFile(src); if err != nil { panic(err) }
        if err=os.WriteFile(filepath.Join(root,name),data,0600); err != nil { panic(err) }
    }
    if err=os.WriteFile(filepath.Join(root,"go.mod"),[]byte("module graycode\n\ngo 1.23\n"),0600); err != nil { panic(err) }
    cmd:=exec.Command("go","test","-count=1","-timeout=10s","-v",".");cmd.Dir=root;cmd.Stdout=os.Stdout;cmd.Stderr=os.Stderr
    if err=cmd.Run();err!=nil { panic(err) }
    fmt.Println("PASS gray-code: trusted compiled cases and single-bit probes")
}
