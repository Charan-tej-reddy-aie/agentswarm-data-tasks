import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const task="count-inversions";
const helper=(await import(pathToFileURL(process.argv[2])))["countInversions"];
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
check([[-0,0]],0);
check([[0,-0]],0);
check([[1,-0]],1);
check([Array.from({length:1000},(_,i)=>1000-i)],499500);
rejects([[1e9+1]],RangeError);
rejects([[1.5]],RangeError);
rejects([[NaN]],RangeError);
rejects([[Infinity]],RangeError);
rejects([[-1e9-1]],RangeError);
rejects([Array(1001).fill(0)],RangeError);
rejects([['1']],TypeError);
rejects([[1n]],TypeError);
rejects([[new Number(1)]],TypeError);
rejects([[1.5,'x']],TypeError);
rejects([Array(1001).fill('x')],TypeError);
rejects([Array(1)],TypeError);
rejects([new Proxy([1],{})],TypeError);
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
if(task==='count-inversions') {
 for(const v of badArrays()) rejects([v],TypeError);
 for(const v of badNumbers) {rejects([[v]],TypeError);rejects([[1,v]],TypeError);rejects([[1.5,v,NaN]],TypeError);rejects([[...Array(1000).fill(0),v]],TypeError);}
 inheritedHole(7,()=>{rejects([[1,,3]],TypeError);});
 for(const v of [0.5,-0.5,NaN,Infinity,-Infinity,1e9+1,-1e9-1,1e12,2**53,Number.MAX_VALUE,Number.EPSILON]) {rejects([[v]],RangeError);rejects([[1,v]],RangeError);rejects([[0,v]],RangeError);}
 rejects([Array(1001).fill(0)],RangeError);rejects([Array.from({length:1001},(_,i)=>i)],RangeError);rejects([Array(2000).fill(1.5)],RangeError);
 check([Array(1000).fill(0)],0);check([Array.from({length:1000},(_,i)=>i)],0);check([Array.from({length:1000},(_,i)=>i%2)],124750);
 check([[1e9,-1e9]],1);check([[-1e9,1e9]],0);check([[1e9,1e9-1,1e9-2]],3);
 check([[2,1,3]],1);check([[1,3,2]],1);check([[3,2,1,4]],3);check([[1,1,1,0]],3);check([[0,1,1,1]],0);check([[9,1,9,1]],3);check([[5,4,3,2,1,0]],15);check([[2,4,1,3,5]],3);check([[6,1,2,3,4,5]],5);check([[1,2,3,4,5,0]],5);
 const values=shadow([3,9,1]);assert.equal(helper(values),2);unchangedShadow(values,[3,9,1]);
 assert.equal(helper(Object.freeze([4,2,7,1])),4);
} else {
 for(const v of badStrings) {rejects([v],TypeError);}
 for(const v of [Array(1001).fill('('),{length:5000},new String('('.repeat(1001))]) rejects([v],TypeError);
 rejects([],TypeError);
 for(const t of ['('.repeat(1001),'x'.repeat(1001),'\ud83d\ude80'.repeat(501),'()'.repeat(501)]) rejects([t],RangeError);
 check(['('.repeat(1000)],false);check(['('.repeat(500)+')'.repeat(499)+']'],false);check(['\ud83d\ude80'.repeat(500)],true);check(['[]'.repeat(500)],true);check(['{'.repeat(250)+'['.repeat(250)+']'.repeat(250)+'}'.repeat(250)],true);check(['{'.repeat(250)+'['.repeat(250)+'}'.repeat(250)+']'.repeat(250)],false);
 check(['[]'],true);check(['{}'],true);check(['[[]]'],true);check(['{{}}'],true);check(['(())'],true);check(['(()'],false);check(['()('],false);check(['[(])'],false);check(['{(})'],false);check(['(}'],false);check(['[}'],false);check(['{]'],false);check(['{)'],false);check(['[)'],false);
 check(['}'],false);check([')'],false);check(['()]'],false);check(['[()'],false);check(['({}[])'],true);check(['()()'],true);check(['(][)'],false);check(['][]['],false);check(['x)y(z'],false);
 check(['<(>)'],true);check(['<)'],false);check(['\uff08\uff09)'],false);check(['\uff3b'],true);check(['\u2768\u2769'],true);check(['(\ud800)'],true);check(['\u0028\u0301\u0029'],true);check(['  ( [ ] )  '],true);
}
console.log(`PASS ${task}: ${cases.length} fixtures plus specials, exact types, boxed and proxy values, limits and independence probes`);
