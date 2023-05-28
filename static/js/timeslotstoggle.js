const testbutton = document.querySelectorAll('.time__elems_btn')
testbutton.forEach(item=>{
    item.addEventListener('click', ()=>{
        console.log('test')
    })
})