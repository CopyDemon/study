import { NextRequest, NextResponse } from "next/server";

/**
 * TODO: remove this api later, no need for GET request for login api
 * @description GET request for login api, now use for test api
 * @param request NextRequest
 * @returns response
 */
export async function GET(request: NextRequest) {
    return NextResponse.json({ message: "Are you try to login?" });
}
