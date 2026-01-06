//document.writeln('hello world')
//console.log('hello')
//
//function work(){
//alert('hello world')
//}

//for (let i=1;i<10;i++){
//console.log(i)
//}
//
//var i=4;
//while(let i<5){
//console.log(i)
//i++
//}
//
//do{
//console.log(i)
//i++
//}while(i<=4)

//for(let i=100;i>0;i--)
//{
//console.log(i)
//}
//
//var s="hello"
//var a=""
//for(let i=s.length-1;i>=0;--i)
//{
//   a += s[i]
//
// }console.log(a)
//
// var f=5
// let fact=1
// for (let i=1;i<=f;i++){
// fact=fact*i
// }
// console.log(fact)
//
// a=[12,54,34,78]
// sum=0
// for (let i of a){
// sum += i
// }
// console.log("sum",sum)
//
//b=a[0]
//for (let i of a){
//if (b<i){
//b=i
//}
//}
//console.log('largest',b)
//
//s="hello"
//k='l'
//count=0
//for (let i of s){
//if (i==k){
//count++;
//}
//}
//console.log('count ',count)
//
//var person={'name':'arjun','age':23}
//for( i in person){
//console.log(i,person[i])
//}
//
//
//function factorial(n){
//fact=1
//for(let i=1;i<=n;i++){
//fact =fact*i
//}
//console.log('factorial',fact)
//}
//
//factorial(6)
//
//function palindrome(s){
//a=""
//for (let i=s.length-1;i>=0;i--)
//{
//a += s[i]
//}
//if ( s==a )
//{
//console.log('palindrome')
//}
//else{
//console.log('not')
//}
//}
//
//palindrome('malayalam')
//
//const saa=(a,b)=>{return a+b}
//console.log(saa(2,2))

//function (n){
//for(let i=1;i<n;i++)
//{
//  if(i%3==0 && i%5==0)
//  {
//    console.log('fizzbuzz')
//  }
//  else if()
//}
//}

const a = (b) =>{
return b.length
}


//console.log(a('ehehe'))
//
//function vow(s) {
//    let vowels = "aeiouAEIOU";
//    let count = 0;
//
//    for (let ch of s) {
//        if (vowels.includes(ch)) {
//            count++;
//        }
//    }
//    return count;
//}
//
//console.log(vow("malayalam"));

aa=[11,9,30,16,5]
console.log(aa.map((x)=>x**2))
//cube
console.log(aa.map((x)=>x**3))
//saquare root
console.log(aa.map((x)=>x**0.5))

//given an array
ar=['cat','dog','tiger','elephant']
//to print the length of each element
console.log(ar.map((x)=>x.length))

//given an array
arrayadd=[45,33,89,12,90]
//add 10 to each element
console.log(arrayadd.map((x)=>x+10))

//given an array
arrayecen=[12,56,23,91,66]
//add 10 to even number and sub 10 from odd number
console.log(arrayecen.map((x)=> x%2==0 ? x+10 : x-10))

//given an array
students=[
    {'name':'arun','age':23,'place':'ekm'},
    {'name':'amal','age':24,'place':'tvm'},
    {'name':'anu','age':23,'place':'tcr'}

]
//print place of each student from the array
console.log(students.map((x)=>x.place))

aaa=[1,2,3,4,5,6,7,8,98,9]
console.log(aaa.filter((x)=>x%2==0))

colors=['red','green','yellow']
console.log(colors.filter((x)=>x.length<5))

students=[
    {'name':'arun','age':23,'place':'ekm'},
    {'name':'amal','age':24,'place':'tvm'},
    {'name':'anu','age':23,'place':'tcr'}

]
console.log(students.filter((x)=>x.age<50))

aaaa=[1,2,3,4,5,6,7,8,98,9]
console.log(aaaa.reduce((x,y)=>x+y))

