import { v4 as uuidv4 } from 'uuid';

export class UUIDHandler {
    constructor() {
        console.log(`UUIDHandler called`)
    }

    public generateUUID() {
        return uuidv4();
    }
}