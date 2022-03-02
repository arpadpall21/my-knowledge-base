async function someAsyncFn(){
    let x;
    
    for(let i = 0; i < 1000000000; i++){
        x = 'Am I asynchronous?';
    }
    
    return x;
}

console.count( '->' );

someAsyncFn()
    .then((res)=> console.log(res))
    .catch((err)=> console.log(err))
    
console.count( '->' );

console.log( '--- END ----------------------------------------' );