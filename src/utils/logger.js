/**
 * Logger Utility
 * Simple logging utility for the ERIFY campaign reports system
 */

class Logger {
  constructor() {
    this.levels = {
      error: 0,
      warn: 1,
      info: 2,
      debug: 3
    };
    this.currentLevel = process.env.LOG_LEVEL || 'info';
  }

  log(level, message, ...args) {
    if (this.levels[level] <= this.levels[this.currentLevel]) {
      const timestamp = new Date().toISOString();
      const prefix = `[${timestamp}] [${level.toUpperCase()}]`;
      
      if (args.length > 0) {
        console.log(prefix, message, ...args);
      } else {
        console.log(prefix, message);
      }
    }
  }

  error(message, ...args) {
    this.log('error', message, ...args);
  }

  warn(message, ...args) {
    this.log('warn', message, ...args);
  }

  info(message, ...args) {
    this.log('info', message, ...args);
  }

  debug(message, ...args) {
    this.log('debug', message, ...args);
  }
}

const logger = new Logger();

module.exports = { logger };