import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const task="max-adjacent-gap";
const helper=(await import(pathToFileURL(process.argv[2])))["maxAdjacentGap"];
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
check([[-0]],0);
check([[-0,0]],0);
check([[0,-0,0]],0);
check([[2**20,-(2**20)]],2**21);
rejects([[1e9+1]],RangeError);
rejects([[1.5]],RangeError);
rejects([[NaN]],RangeError);
rejects([[Infinity]],RangeError);
rejects([[-1e9-1]],RangeError);
rejects([['1']],TypeError);
rejects([[1n]],TypeError);
rejects([[new Number(1)]],TypeError);
rejects([[1.5,'x']],TypeError);
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
if(task==='max-adjacent-gap') {
 for(const v of badArrays()) rejects([v],TypeError);
 for(const v of badNumbers) {rejects([[v]],TypeError);rejects([[1,v]],TypeError);rejects([[1.5,v,NaN]],TypeError);}
 inheritedHole(7,()=>{rejects([[1,,3]],TypeError);});
 for(const v of [0.5,-0.5,NaN,Infinity,-Infinity,1e9+1,-1e9-1,1e12,2**53,Number.MAX_VALUE,Number.EPSILON]) {rejects([[v]],RangeError);rejects([[1,v]],RangeError);rejects([[0,v]],RangeError);}
 check([[1e9,-1e9]],2e9);check([[-1e9,1e9,-1e9]],2e9);check([[1e9,1e9]],0);check([[-1e9,-1e9+1]],1);
 check([[5,1,9]],8);check([[9,1,5]],8);check([[1,9,5,7]],8);check([[0,100,0]],100);check([[1,2,3,4,50]],46);check([[50,4,3,2,1]],46);
 check([[1,5,1]],4);check([[10,1,10,1]],9);check([[7]],0);check([[-7]],0);check([[3,3,3,10,10]],7);check([[100,1,2,100]],99);check([[100,2,1,99]],98);
 const values=shadow([3,9,1]);assert.equal(helper(values),8);unchangedShadow(values,[3,9,1]);
 assert.equal(helper(Object.freeze([2,7,4])),5);
 const big=Array.from({length:1000},(_,i)=>i%2?-1:1);assert.equal(helper(big),2);
 const ramp=Array.from({length:1000},(_,i)=>i*1000);ramp[700]=ramp[699]+5000;assert.equal(helper(ramp),5000);
} else {
 for(const v of badStrings) {rejects([v,'a'],TypeError);rejects(['a',v],TypeError);rejects([v,'x'.repeat(1001)],TypeError);rejects(['x'.repeat(1001),v],TypeError);}
 rejects([],TypeError);rejects(['a'],TypeError);
 for(const [a,b] of [['x'.repeat(1001),''],['','x'.repeat(1001)],['\ud83d\ude80'.repeat(501),'\ud83d\ude80'.repeat(501)],['a','\ud83d\ude80'.repeat(500)+'a']]) rejects([a,b],RangeError);
 check(['x'.repeat(1000),'x'.repeat(1000)],true);check(['\ud83d\ude80'.repeat(500),'\ud83d\ude80'.repeat(500)],true);
 const s=Array.from({length:1000},(_,i)=>String.fromCharCode(97+i%26)).join('');
 check([s,s],true);check([s.slice(1),s],true);check([s.slice(0,999),s],true);check([s,s.slice(1)],false);check(['z'.repeat(39),s],false);check(['z'.repeat(38),s],true);check([[...s].reverse().join('').slice(0,30),s],true);check(['ba'.repeat(500),s],false);
 check(['abc','aXbXc'],true);check(['abc','cba'],false);check(['abc','acb'],false);check(['abc','ab'],false);check(['abc','bc'],false);check(['abc','abcabc'],true);check(['cab','abcabc'],true);check(['aaa','aab'],false);check(['aaa','abaca'],true);
 check(['ab','ab'],true);check(['ab','ba'],false);check(['','x'],true);check(['x',''],false);check(['A','abc'],false);check(['a b','a  b'],true);check(['ab','a b'],true);check(['a b','ab'],false);
 check(['\ud800\ud800','\ud800x\ud800'],true);check(['\u00e9t\u00e9','\u00e9x t\u00e9'],true);check(['e\u0301','e\u0301'],true);check(['\u0301','e\u0301'],true);check(['\ud83d\ude80\ud83d\ude81','\ud83d\ude80x\ud83d\ude81'],true);
 check(['\ud83d\ude81\ud83d\ude80','\ud83d\ude80\ud83d\ude81'],false);check(['\ude80\ud83d','\ud83d\ude80\ud83d'],false);
}
console.log(`PASS ${task}: ${cases.length} fixtures plus specials, exact types, boxed and proxy values, limits and independence probes`);
