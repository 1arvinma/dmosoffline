/* Content packs restore before the workspace reads its catalogs. */
Promise.resolve(window.DMOS_CONTENT?.ready).then(()=>{
/* DMOS_APP_ENTRY */
const entry=document.createElement('script');entry.src='app.js';document.body.appendChild(entry);
/* DMOS_APP_END */
}).catch(error=>{document.getElementById('app').textContent='DMOS could not start: '+error.message;});
