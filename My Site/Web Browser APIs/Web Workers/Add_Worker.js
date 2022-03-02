
// receiving the message
    onmessage = function(event) {
        var transferObj = event.data;               // "event.data"'s data cannot be transfered outside the onmessage function for some reasons!
// process the received data    
        var result;                                 // since the function itself cannot be sent by a Web Worker we store the data in a variable
        process();
        function process() {
            result = Number(transferObj.field_A) + Number(transferObj.field_B);     // this function is useless here but I wrote it for demo
        };
// resending the message
    self.postMessage( result );    
    };

    

