import { NextRequest, NextResponse } from "next/server";
export async function POST(request: NextRequest) {
    console.log(`login post request`)

    const body = await request.json();
    const username = body.username;
    const password = body.password;

    // simulate login authentication query from db and find valid user
    if(username === 'asd' && password === 'asd') {
        //simulate login process generate a web token
        let webToken = "allow"; 

        // simulate setup auto logout after 60 seconds
        setTimeout(() => {
            webToken = "";
            console.log(`post request done`)
        }, 60000)

        return NextResponse.json({ 
            message: `successful login with uname: ${username} and pwd: ${password}` ,
            webToken // web token for authentication
        });
    }

    // TODO: can check username is wrong or password is wrong or all wrong
    // simulate invalid username or password
    if(username !== 'asd' || password !== 'asd') {
        return NextResponse.json(
            { message: "Invalid username or password" },
            { status: 401 }, 
        );
    }
}
