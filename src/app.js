#!/usr/bin/env node

/**
 * ERIFY Campaign Performance Reports Automation
 * Scheduled automation for generating and distributing campaign performance reports
 */

require('dotenv').config();
const cron = require('node-cron');
const { DataCollector } = require('./modules/dataCollector');
const { ReportGenerator } = require('./modules/reportGenerator');
const { EmailNotifier } = require('./modules/emailNotifier');
const { logger } = require('./utils/logger');

class CampaignReportsApp {
  constructor() {
    this.dataCollector = new DataCollector();
    this.reportGenerator = new ReportGenerator();
    this.emailNotifier = new EmailNotifier();
  }

  /**
   * Generate and send daily report
   */
  async generateDailyReport() {
    try {
      logger.info('Starting daily report generation...');
      
      // Collect data from last 24 hours
      const data = await this.dataCollector.collectDailyData();
      
      // Generate report
      const report = await this.reportGenerator.generateDailyReport(data);
      
      // Send to team and stakeholders
      await this.emailNotifier.sendDailyReport(report);
      
      logger.info('Daily report completed successfully');
    } catch (error) {
      logger.error('Daily report failed:', error);
      await this.emailNotifier.sendErrorNotification('Daily Report Failed', error);
    }
  }

  /**
   * Generate and send weekly report
   */
  async generateWeeklyReport() {
    try {
      logger.info('Starting weekly report generation...');
      
      // Collect data from last 7 days
      const data = await this.dataCollector.collectWeeklyData();
      
      // Generate comprehensive report
      const report = await this.reportGenerator.generateWeeklyReport(data);
      
      // Send to team and stakeholders
      await this.emailNotifier.sendWeeklyReport(report);
      
      logger.info('Weekly report completed successfully');
    } catch (error) {
      logger.error('Weekly report failed:', error);
      await this.emailNotifier.sendErrorNotification('Weekly Report Failed', error);
    }
  }

  /**
   * Start the scheduled automation
   */
  start() {
    logger.info('ERIFY Campaign Reports Automation starting...');
    
    // Daily report schedule (default: 9:00 AM)
    const dailyTime = process.env.DAILY_REPORT_TIME || '09:00';
    const dailyCron = `0 ${dailyTime.split(':')[1]} ${dailyTime.split(':')[0]} * * *`;
    
    cron.schedule(dailyCron, async () => {
      await this.generateDailyReport();
    }, {
      timezone: process.env.TIMEZONE || 'America/New_York'
    });

    // Weekly report schedule (default: Monday 9:00 AM)
    const weeklyDay = process.env.WEEKLY_REPORT_DAY || 'monday';
    const weeklyTime = process.env.WEEKLY_REPORT_TIME || '09:00';
    const weeklyDayNum = {
      'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3,
      'thursday': 4, 'friday': 5, 'saturday': 6
    }[weeklyDay.toLowerCase()] || 1;
    
    const weeklyCron = `0 ${weeklyTime.split(':')[1]} ${weeklyTime.split(':')[0]} * * ${weeklyDayNum}`;
    
    cron.schedule(weeklyCron, async () => {
      await this.generateWeeklyReport();
    }, {
      timezone: process.env.TIMEZONE || 'America/New_York'
    });

    logger.info(`Daily reports scheduled at ${dailyTime}`);
    logger.info(`Weekly reports scheduled on ${weeklyDay} at ${weeklyTime}`);
    logger.info('Automation is running. Press Ctrl+C to stop.');

    // Graceful shutdown
    process.on('SIGINT', () => {
      logger.info('Shutting down gracefully...');
      process.exit(0);
    });
  }

  /**
   * Generate report on demand for testing
   */
  async generateTestReport() {
    logger.info('Generating test report...');
    await this.generateDailyReport();
  }
}

// Start the application
const app = new CampaignReportsApp();

if (require.main === module) {
  // Check if running in test mode
  if (process.argv.includes('--test')) {
    app.generateTestReport();
  } else {
    app.start();
  }
}

module.exports = CampaignReportsApp;