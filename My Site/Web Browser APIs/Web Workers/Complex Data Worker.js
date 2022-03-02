
var myObj = {text: "This text is sent through by the Web Worker",
              number: 4512,
              boolean: true,
              nestedObj: {nestedProp:"nested text"},
              nestedArray: ["un", "deux"]
              //additionFunc : function(a, b){return a + b;}            // cannot be sent "throws an error"
            };

var testFunction = function(a, b) {return a + b;}                       // functions cannot be sent by Web Workers

postMessage(myObj);