const popup = document.querySelector('.popup')
const profile = document.querySelector('.profile')
const content = document.querySelector('.content')
var hidden = 1 //1 means hidden

function toPop(){
    //check stuff
    
    if (hidden == 1){
        popup.removeAttribute('hidden') //this shows it
        hidden = 0
    }
    else{
        popup.setAttribute('hidden','') //this hides it
        hidden = 1
    }
}
function unPop(){
    popup.setAttribute('hidden','')
}

profile.addEventListener('click', toPop)
content.addEventListener('click', unPop)