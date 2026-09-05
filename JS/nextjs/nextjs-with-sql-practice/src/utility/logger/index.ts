import * as winston from 'winston';
import * as path from 'path';

export const logger = (callingModule: NodeModule) => {
    return new winston.transports.Console({
        format: winston.format.combine(
            winston.format.timestamp(),
            winston.format.colorize(),
            winston.format.printf(({ timestamp, level, message }) => {
                const filename = path.relative(process.cwd(), callingModule.filename);
                return `${timestamp} [${filename}] [${level}]: ${message}`;
            })
        )
    });
};