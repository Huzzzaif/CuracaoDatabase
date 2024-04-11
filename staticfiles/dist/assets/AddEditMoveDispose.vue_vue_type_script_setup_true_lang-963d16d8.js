import{d as $,r as t,o as s,c as R,w as n,e as o,b as a,v as F,h as u,A as C,y as N,z as O,F as x,B,C as i,g as d,s as j,q,t as M}from"./index-144da44d.js";import{_ as z}from"./SaveCancelButtons.vue_vue_type_script_setup_true_lang-3db21dc4.js";import{g as P}from"./axios-cc0ad009.js";const W=$({__name:"AddEditMoveDispose",emits:["onSave"],setup(H,{expose:w}){const m=t({}),L=t();async function k(){try{const r=await P.get("/locations/"),l={};r.data.forEach(e=>{l[e.name]={name:e.name,id:e.id}}),m.value=l}catch(r){console.error(r)}}async function G(){try{const r=await P.get("/departments/");let l=[];r.data.forEach(e=>{l.push(e)}),L.value=l}catch(r){console.error(r)}}k(),G();const p=t(),v=t(),V=t(),c=t(),f=t(),I=t(),E=t(),S=t(),T=t(),g=t(),b=t(),A=t(),D=t(),U=t(),y=t();return w({locations:m,serial:p,mac:v,cid:V,mid:c,tid:f,store:I,department:E,pStation:S,register:T,ipAddress:g,itLabelID:b,itAssetID:A,notes:D,status:U,statusNotes:y}),(r,l)=>(s(),R(a(q),{fixed:!0},{default:n(()=>[o(a(j),null,{default:n(()=>[o(a(F),null,{default:n(()=>[o(a(u),{modelValue:p.value,"onUpdate:modelValue":l[0]||(l[0]=e=>p.value=e),label:"SERIAL",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter serial number"},null,8,["modelValue"]),o(a(u),{modelValue:v.value,"onUpdate:modelValue":l[1]||(l[1]=e=>v.value=e),label:"MAC ADDRESS",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter MAC address"},null,8,["modelValue"]),o(a(u),{modelValue:V.value,"onUpdate:modelValue":l[2]||(l[2]=e=>V.value=e),label:"CID#",type:"number",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter CID#"},null,8,["modelValue"]),o(a(u),{modelValue:c.value,"onUpdate:modelValue":l[3]||(l[3]=e=>c.value=e),label:"MID#",type:"number",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter MID#"},null,8,["modelValue"]),o(a(u),{modelValue:f.value,"onUpdate:modelValue":l[4]||(l[4]=e=>f.value=e),label:"TID#",type:"number",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter TID#"},null,8,["modelValue"]),o(a(C),{modelValue:I.value,"onUpdate:modelValue":l[5]||(l[5]=e=>I.value=e),label:"STORE",class:"ion-margin-vertical",fill:"outline",interface:"popover",placeholder:"Select a store"},{default:n(()=>[(s(!0),N(x,null,O(m.value,e=>(s(),R(a(i),null,{default:n(()=>[d(M(e.name),1)]),_:2},1024))),256))]),_:1},8,["modelValue"]),o(a(C),{modelValue:E.value,"onUpdate:modelValue":l[6]||(l[6]=e=>E.value=e),label:"LOCATION/DEPARTMENT",class:"ion-margin-vertical",fill:"outline",interface:"popover",placeholder:"Select a location/department"},{default:n(()=>[(s(!0),N(x,null,O(L.value,e=>(s(),R(a(i),null,{default:n(()=>[d(M(e.department),1)]),_:2},1024))),256))]),_:1},8,["modelValue"]),o(a(u),{modelValue:S.value,"onUpdate:modelValue":l[7]||(l[7]=e=>S.value=e),label:"PSTATION",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter PSTATION"},null,8,["modelValue"]),o(a(u),{modelValue:T.value,"onUpdate:modelValue":l[8]||(l[8]=e=>T.value=e),label:"REGISTER",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter REGISTER"},null,8,["modelValue"]),o(a(u),{modelValue:g.value,"onUpdate:modelValue":l[9]||(l[9]=e=>g.value=e),label:"IP ADDRESS",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter IP address"},null,8,["modelValue"]),o(a(u),{modelValue:b.value,"onUpdate:modelValue":l[10]||(l[10]=e=>b.value=e),label:"IT LABEL ID",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter IT LABEL ID"},null,8,["modelValue"]),o(a(u),{modelValue:A.value,"onUpdate:modelValue":l[11]||(l[11]=e=>A.value=e),type:"number",label:"IT ASSET ID",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter IT ASSET ID"},null,8,["modelValue"]),o(a(B),{modelValue:D.value,"onUpdate:modelValue":l[12]||(l[12]=e=>D.value=e),label:"NOTES",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter notes"},null,8,["modelValue"]),o(a(C),{modelValue:U.value,"onUpdate:modelValue":l[13]||(l[13]=e=>U.value=e),label:"STATUS",class:"ion-margin-vertical",fill:"outline",interface:"popover",placeholder:"Select a status"},{default:n(()=>[o(a(i),null,{default:n(()=>[d("Active")]),_:1}),o(a(i),null,{default:n(()=>[d("Inactive")]),_:1})]),_:1},8,["modelValue"]),o(a(B),{modelValue:y.value,"onUpdate:modelValue":l[14]||(l[14]=e=>y.value=e),label:"STATUS NOTES",class:"ion-margin-vertical",fill:"outline",placeholder:"Enter status notes"},null,8,["modelValue"])]),_:1})]),_:1}),o(z,{onOnSave:l[15]||(l[15]=e=>r.$emit("onSave"))})]),_:1}))}});export{W as _};