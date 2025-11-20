let eids=[101,102,103,104]
//create new array from existing array
let uids=[]
for(let eid of eids){
    uids.push(eid);
}
console.log(uids);


let uid=eids.map((eiid)=>{
    return eiid;
})
console.log(uid)


let pids=eids.forEach((ed)=>{
    return ed;
})
console.log(pids)