onmessage = (ev) => {
  console.log(ev.data)          // -> 'Hello worker
}

onmessageerror = (ev) => {
  console.log('??')
  console.log(ev)
}