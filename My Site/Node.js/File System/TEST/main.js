import fs from 'node:fs';


// console.log(
//   fs.symlinkSync('./file2.txt', './SYMLINK')
// )


console.log(
  fs.readFileSync('./SYMLINK').toString()
)