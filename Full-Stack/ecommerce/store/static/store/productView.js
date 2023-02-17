const add = document.querySelector('#add')
const sub = document.querySelector('#sub')
const quantity = document.querySelector('.quantity')
const addToCart = document.querySelector('#addCart')
quantity.setAttribute('disabled', '')

function adder(){
    if (quantity.value < 9){
        quantity.value = (parseInt(quantity.value) + 1).toString()
    }
}

function deadder(){
    if (quantity.value > 1){
        quantity.value = (parseInt(quantity.value) - 1).toString()
    }
}

function act(){
    quantity.removeAttribute('disabled')
}


add.addEventListener('click', adder)
sub.addEventListener('click', deadder)
addToCart.addEventListener('click', act)

/* Didn't work
addToCart.addEventListener('click', (event) => {
    quantity.removeAttribute('disabled')
})
*/