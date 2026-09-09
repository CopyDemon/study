/**
 * @description fetch data from server GET POST PUT UPDATE DELETE
 * @param url String
 * @param requestType String
 * @param requestBody Object
 * @returns Object
 */
export const fetchData = async (url: string, requestType: string, requestBody: any): Promise<any> => {
    try {
        // GET request
        if (requestType === "GET") {
            const response = await fetch(url);
            return response.json();
        }
        // POST request
        if (requestType === "POST") {
            const response = await fetch(url, {
                method: requestType,
                body: JSON.stringify(requestBody),
            });
        }
    } catch (error) {
        console.error(error);
    }
}