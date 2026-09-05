// import 'dotenv/config';
import { NextRequest, NextResponse } from 'next/server';
import { env } from './env';
export async function middleware(request: NextRequest) {
    console.log('middleware');
    console.log(env.PORT)
    console.log(env.PORT)
    console.log(env.PORT)
    console.log(env.PORT)
    return NextResponse.next();
}