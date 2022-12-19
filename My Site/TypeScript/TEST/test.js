const io = require('socket.io')
const config = require('../../config')
const serviceContainer = require('../service_container')

module.exports = {
    start(httpServer) {
        // socket.io v4 server options:
        // https://socket.io/docs/v4/server-api/#new-Server-httpServer-options

        // Useful links for socket.io v4 CORS specific configurations:
        // https://socket.io/docs/v4/handling-cors/
        // https://github.com/expressjs/cors#configuration-options

        return io(httpServer, config.get('web.socket', {}))
    },

    setupEvents(connection) {
        const modules = [
            require('./client'),
            require('./events/auth'),
            require('./events/pagevisit'),
            require('./events/lobby'),
            require('./events/waiting-room'),
            require('./events/echotest'),
            require('./events/ping'),
            require('./events/videochat'),
            require('./events/videochat.presentation'),
            require('./events/videochat.customerDataChange'),
            require('./events/videochat.validation'),
            require('./events/webrtclog'),
            require('./events/mobile'),
            require('./events/selfservice'),
            require('./events/selfservice-v2'),
            require('./events/flow')
        ]

        serviceContainer.emitter.callHooks('socket', modules)

        connection.sockets.on('connection', (client) => {
            modules.forEach(function (module) {
                module(client)
            })
        })
    }
}




[1, 2, 3].forEach(function (val, idx, arr) {
    console.log(val)
})