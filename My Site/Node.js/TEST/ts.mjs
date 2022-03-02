const abortController = new AbortController();
console.log( abortController.signal.aborted );            // -> false
abortController.signal.throwIfAborted();

abortController.abort('some abort error');
console.log( abortController.signal.aborted );            // -> true 

try {
    abortController.signal.throwIfAborted();
} catch (err) {
    console.log(err);
}

