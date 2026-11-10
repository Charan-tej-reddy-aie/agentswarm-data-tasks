import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {types} from 'node:util';
const task="repeat-items";
const helper=(await import(pathToFileURL(process.argv[2])))["repeatItems"];
const cases=JSON.parse(readFileSync(new URL('./fixtures/cases.json',import.meta.url)));
function check(args,expected) {
 const before=structuredClone(args);
 const a=helper(...args),b=helper(...args);
 assert.deepEqual(a,expected);assert.deepEqual(b,expected);
 if(task==='argmax-index') {assert.equal(typeof a,'number');assert.ok(Object.is(a,expected));}
 else {
  for(const r of [a,b]) {assert.equal(types.isProxy(r),false);assert.equal(Array.isArray(r),true);assert.equal(Object.getPrototypeOf(r),Array.prototype);}
  assert.notEqual(a,b);for(const x of args) assert.notEqual(a,x);
  a.push('changed');assert.deepEqual(helper(...args),expected);
 }
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
check([['a'],-0],[]);
check([['\ud800'],2],['\ud800','\ud800']);
rejects([['a'],11],RangeError);
rejects([['a'],-1],RangeError);
rejects([['a'],1.5],RangeError);
rejects([['a'],'2'],TypeError);
rejects([[1],2],TypeError);
rejects([[1],11],TypeError);
rejects([Array(1),1],TypeError);
rejects([['a'],new Number(1)],TypeError);
rejects([new Proxy(['a'],{}),1],TypeError);
class A extends Array {} class S extends String {} class N extends Number {}
const proxy=x=>new Proxy(x,{}),revoked=()=>{const p=Proxy.revocable([],{});p.revoke();return p.proxy;};
const badArrays=()=>[undefined,null,true,1,'ab',{},{length:0},new Set(),new A(),A.from(['a']),Object.setPrototypeOf([],null),Object.setPrototypeOf(['a'],Object.prototype),Array(1),['a',,'b'],proxy([]),proxy(['a']),revoked()];
const badStrings=[undefined,null,true,1,1n,Symbol('x'),[],['a'],{},new String('a'),new S('a'),proxy(new String('a'))];
const badNumbers=[undefined,null,true,'1','',1n,Symbol('x'),[],[1],{},new Number(1),new N(1),proxy(new Number(1))];
const shadowed=['slice','concat','map','forEach','filter','reduce','push','at','entries','keys','values','join','indexOf','fill','flatMap','constructor'];
function shadow(values) {
 const copy=[...values];for(const name of shadowed) copy[name]=null;copy[Symbol.iterator]=null;copy.extra='ignored';return copy;
}
function unchangedShadow(copy,values) {
 for(const name of shadowed) assert.equal(copy[name],null);assert.equal(copy[Symbol.iterator],null);assert.equal(copy.extra,'ignored');
 assert.equal(copy.length,values.length);for(let i=0;i<values.length;i++) assert.ok(Object.is(copy[i],values[i]));
}
if(task==='argmax-index') {
 for(const v of badArrays()) rejects([v],TypeError);
 for(const v of badNumbers) {rejects([[v]],TypeError);rejects([[1,v]],TypeError);rejects([[1.5,v]],TypeError);rejects([[NaN,v]],TypeError);}
 for(const v of [NaN,Infinity,-Infinity,0.5,-1.5,2**53,-(2**53),Number.MAX_VALUE,Number.EPSILON]) {rejects([[v]],RangeError);rejects([[1,v]],RangeError);rejects([[v,1]],RangeError);}
 inheritedHole(9,()=>{rejects([[1,,1]],TypeError);});
 rejects([[]],RangeError);
 const values=shadow([1,7,7]);assert.equal(helper(values),1);unchangedShadow(values,[1,7,7]);
 assert.equal(helper(Object.freeze([2,-0,3,3])),2);
 const big=Array.from({length:1000},(_,i)=>i%7);assert.equal(helper(big),6);
 const desc=Array.from({length:1000},(_,i)=>1000-i);assert.equal(helper(desc),0);
 check([[4,9,9,1,9]],1);check([[-1,-1,-1]],0);check([[-2,-1]],1);check([[0,1,0,1]],1);
} else {
 for(const v of badArrays()) {rejects([v,1],TypeError);rejects([v,11],TypeError);}
 for(const v of badStrings) {rejects([[v],1],TypeError);rejects([['a',v],2],TypeError);rejects([['a',v],-1],TypeError);rejects([[v],0],TypeError);}
 for(const v of badNumbers) {rejects([['a'],v],TypeError);rejects([[],v],TypeError);}
 for(const v of [NaN,Infinity,-Infinity,0.5,1.5,-1,11,12,2**53,Number.EPSILON]) {rejects([['a'],v],RangeError);rejects([[],v],RangeError);}
 inheritedHole('p',()=>{rejects([['a',,'b'],1],TypeError);});
 const values=shadow(['b','a']);assert.deepEqual(helper(values,2),['b','b','a','a']);unchangedShadow(values,['b','a']);
 assert.deepEqual(helper(Object.freeze(['x','y']),3),['x','x','x','y','y','y']);
 for(let t=0;t<=10;t++) check([['p','q'],t],[...Array(t).fill('p'),...Array(t).fill('q')]);
 check([['solo'],1],['solo']);
 const big=Array.from({length:1000},(_,i)=>'v'+i);const out=helper(big,10);assert.equal(out.length,10000);assert.equal(out[9999],'v999');assert.equal(out[10],'v1');
 check([['a\u0000','a'],2],['a\u0000','a\u0000','a','a']);
}
console.log(`PASS ${task}: ${cases.length} fixtures plus specials, exact types, proxies, subclasses, holes, frozen, shadowed-method and independence probes`);
