import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const task="sum-squares";
const helper=(await import(pathToFileURL(process.argv[2])))["sumSquares"];
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
check([[0,-0]],0);
check([[2**13]],2**26);
check([[-(2**13),2**13]],2**27);
rejects([[1e7+1]],RangeError);
rejects([[1.5]],RangeError);
rejects([[NaN]],RangeError);
rejects([[Infinity]],RangeError);
rejects([[-1e7-1]],RangeError);
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
if(task==='sum-squares') {
 for(const v of badArrays()) rejects([v],TypeError);
 for(const v of badNumbers) {rejects([[v]],TypeError);rejects([[1,v]],TypeError);rejects([[1.5,v,NaN]],TypeError);}
 inheritedHole(7,()=>{rejects([[1,,3]],TypeError);});
 for(const v of [0.5,-0.5,NaN,Infinity,-Infinity,1e7+1,-1e7-1,1e9,2**53,Number.MAX_VALUE,Number.EPSILON]) {rejects([[v]],RangeError);rejects([[1,v]],RangeError);rejects([[0,v]],RangeError);}
 const maxSafe=[10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 2683142, 1927, 187, 23];
 check([maxSafe],Number.MAX_SAFE_INTEGER);check([[...maxSafe].reverse()],Number.MAX_SAFE_INTEGER);
 rejects([[...maxSafe.slice(0,90),2683142,1927,187,24]],RangeError);rejects([Array(91).fill(1e7)],RangeError);rejects([Array(1000).fill(-1e7)],RangeError);
 check([Array(90).fill(1e7)],9e15);check([Array(90).fill(-1e7)],9e15);
 const values=shadow([3,9,1]);assert.equal(helper(values),91);unchangedShadow(values,[3,9,1]);
 assert.equal(helper(Object.freeze([2,7,4])),69);
 const big=Array.from({length:1000},(_,i)=>i%2?-1:1);assert.equal(helper(big),1000);
 check([[-7]],49);check([[-0,5]],25);check([[-0,-0]],0);check([[1,2,3,4]],30);check([[9999999]],99999980000001);
} else {
 for(const v of badStrings) {rejects([v,'a'],TypeError);rejects(['a',v],TypeError);rejects([v,'x'.repeat(1001)],TypeError);rejects(['x'.repeat(1001),v],TypeError);}
 rejects([],TypeError);rejects(['a'],TypeError);
 for(const [a,b] of [['x'.repeat(1001),''],['','x'.repeat(1001)],['\ud83d\ude80'.repeat(501),'\ud83d\ude80'.repeat(501)],['\ud83d\ude80'.repeat(500)+'a','a']]) rejects([a,b],RangeError);
 check(['x'.repeat(1000),'x'.repeat(1000)],true);check(['\ud83d\ude80'.repeat(500),'\ud83d\ude80'.repeat(500)],true);
 const s=Array.from({length:1000},(_,i)=>String.fromCharCode(97+i%26)).join('');
 check([s,s.slice(1)+s[0]],true);check([s,s.slice(999)+s.slice(0,999)],true);check([s,s.slice(1)+'!'],false);check([s,s.slice(1)],false);check([s,[...s].reverse().join('')],false);
 check(['abc','bca'],true);check(['abc','cab'],true);check(['abcd','cdab'],true);check(['abcd','acbd'],false);check(['aabb','abab'],false);check(['abab','baba'],true);
 check(['ab','ab'],true);check(['ab','abab'],false);check(['abab','ab'],false);check(['aba','abaa'],false);check(['A','a'],false);check(['1 2','21 '],true);check(['1 2',' 21'],true);check(['1 2','12 '],false);
 check(['\ud800\ud800','\ud800\ud800'],true);check(['\u00e9t\u00e9','t\u00e9\u00e9'],true);check(['e\u0301','\u0301e'],true);check(['\ud83d\ude80\ud83d\ude81','\ud83d\ude81\ud83d\ude80'],true);
 check(['\ud83d\ude80ab','b\ud83d\ude80a'],true);check(['\ud83d\ude80ab','\ude80ab\ud83d'],false);
}
console.log(`PASS ${task}: ${cases.length} fixtures plus specials, exact types, boxed and proxy values, limits and independence probes`);
