import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const task="is-isbn10";
const helper=(await import(pathToFileURL(process.argv[2])))["isIsbn10"];
const cases=JSON.parse(readFileSync(new URL('./fixtures/cases.json',import.meta.url)));
function check(args,expected) {
 const before=structuredClone(args);
 const a=helper(...args),b=helper(...args);
 assert.equal(typeof a,typeof expected);assert.equal(typeof b,typeof expected);
 assert.ok(Object.is(a,expected),String(a));assert.ok(Object.is(b,expected),String(b));
 assert.deepEqual(args,before,'input mutation');
}
const rejects=(args,ErrorType)=>assert.throws(()=>helper(...args),e=>e!==null && typeof e==='object' && e.constructor===ErrorType,String(args.length));
function inheritedHole(value,probe) {
 // A hole must be rejected even when Array.prototype supplies a value of the right type at that index.
 Object.defineProperty(Array.prototype,1,{value,configurable:true,writable:true});
 try {probe();} finally {delete Array.prototype[1];}
 assert.equal(Object.hasOwn(Array.prototype,1),false);
}
for(const row of cases) {if(Object.hasOwn(row,'error')) rejects(row.args,{TypeError,RangeError}[row.error]);else check(row.args,row.expected);}
check(['0306406152\n'],false);
check(['\u0660306406152'],false);
check(['03064061'+'5'+'2'],true);
check(['1'.repeat(1000)],false);
rejects([1],TypeError);
rejects([null],TypeError);
rejects([306406152],TypeError);
rejects([new String('0306406152')],TypeError);
rejects(['1'.repeat(1001)],RangeError);
class A extends Array {} class S extends String {} class N extends Number {}
const proxy=x=>new Proxy(x,{}),revoked=()=>{const p=Proxy.revocable([],{});p.revoke();return p.proxy;};
const badArrays=()=>[undefined,null,true,1,'ab',{},{length:0},new Set(),new A(),A.from(['a']),Object.setPrototypeOf([],null),Object.setPrototypeOf(['a'],Object.prototype),Array(1),['a',,'b'],proxy([]),proxy(['a']),revoked()];
const badStrings=[undefined,null,true,1,1n,Symbol('x'),[],['a'],{},new String('a'),new S('a'),proxy(new String('a'))];
const badNumbers=[undefined,null,true,'1',1n,Symbol('x'),[],[1],{},new Number(1),new N(1),proxy(new Number(1))];
const shadowed=['slice','concat','map','forEach','filter','reduce','push','at','entries','keys','values','join','indexOf','fill','flatMap','sort','constructor'];
function shadow(values) {
 const copy=[...values];for(const name of shadowed) copy[name]=null;copy[Symbol.iterator]=null;copy.extra='ignored';return copy;
}
function unchangedShadow(copy,values) {
 for(const name of shadowed) assert.equal(copy[name],null);assert.equal(copy[Symbol.iterator],null);assert.equal(copy.extra,'ignored');
 assert.equal(copy.length,values.length);for(let i=0;i<values.length;i++) assert.ok(Object.is(copy[i],values[i]));
}
for(const v of badStrings) rejects([v],TypeError);
for(const v of [Array(1001).fill('1'),{length:5000},new String('1'.repeat(1001)),1e10]) rejects([v],TypeError);
rejects([],TypeError);
for(const t of ['1'.repeat(1001),'_'.repeat(1001),'\ud83d\ude80'.repeat(501),'0306406152'.repeat(101)]) rejects([t],RangeError);
if(task==='is-isbn10') {
 check(['0306406152'.repeat(100)],false);check(['0'.repeat(1000)],false);
 check(['0123456789'],true);check(['0123456788'],false);check(['000000001X'],false);check(['000000010X'],false);check(['0000000019'],true);check(['000000002X'],false);
 check(['999999999X'],false);check(['9999999999'],true);check(['111111111X'],false);check(['1111111111'],true);check(['X'],false);check(['XXXXXXXXXX'],false);check(['00000000X0'],false);
 check(['0306406152x'],false);check(['0306-406152'],false);check(['030640615\u0032'],true);check(['0306406152\u0000'],false);check(['+306406152'],false);check(['O306406152'],false);
 check(['\t0306406152'],false);check(['0306406152\r'],false);check(['0 306406152'],false);check(['3-598-21508-8'],false);check(['3598215088'],true);check(['3598215089'],false);check(['359821507X'],true);check(['359821507x'],false);
} else {
 check(['a_b'.repeat(333)],'aB'.repeat(333));check(['_a'.repeat(500)],'A'.repeat(500));check(['a'.repeat(1000)],'a'.repeat(1000));
 check(['make_it_work'],'makeItWork');check(['Make_It'],'MakeIt');check(['a_z'],'aZ');check(['a_{'],'a{');check(['a_`'],'a`');check(['a_@'],'a@');check(['A_a'],'AA');check(['ab_cd_ef'],'abCdEf');
 check(['a__'],'a');check(['___x'],'X');check(['x___'],'x');check(['a-b'],'a-b');check(['a b'],'a b');check(['a_ b'],'a b');check(['a_\u00e0'],'a\u00e0');check(['a_\u017f'],'a\u017f');check(['a_\u0430'],'a\u0430');
 check(['\u00e9_\u00e9'],'\u00e9\u00e9');check(['a_\ud801\udc28'],'a\ud801\udc28');check(['ID_value'],'IDValue');check(['x1_y2_z3'],'x1Y2Z3');check(['__init__'],'Init');check(['a\u005fb'],'aB');check(['a\uff3fb'],'a\uff3fb');
}
console.log(`PASS ${task}: ${cases.length} fixtures plus specials, exact types, boxed and proxy values, limits and independence probes`);
