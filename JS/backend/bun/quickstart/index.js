import figlet from "figlet";

const server = Bun.serve({
    fetch(){
        const body = figlet.textSync("Whats up")
        return new Response(body)
    },
    port:3090,
});

console.log(`Listing on port ${server.port}`)