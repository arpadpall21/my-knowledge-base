// let interval = setInterval(() => {
//     console.log('Hello from nodejs!')
    
// }, 5000)

process.stdin.on('data', data => {
    console.log( 'stdin --------------- ')
    console.log( data )
})

console.log( 'test' )

throw Error('test error')