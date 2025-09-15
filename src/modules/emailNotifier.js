/**
 * Email Notification Module
 * Sends campaign performance reports to designated ERIFY team members and stakeholders
 * Supports both HTML and plain text formats
 */

const nodemailer = require('nodemailer');
const { logger } = require('../utils/logger');

class EmailNotifier {
  constructor() {
    this.transporter = this.createTransporter();
    this.teamEmails = this.parseEmailList(process.env.TEAM_EMAILS);
    this.stakeholderEmails = this.parseEmailList(process.env.STAKEHOLDER_EMAILS);
  }

  /**
   * Create email transporter
   */
  createTransporter() {
    return nodemailer.createTransport({
      host: process.env.SMTP_HOST || 'smtp.gmail.com',
      port: parseInt(process.env.SMTP_PORT) || 587,
      secure: false, // true for 465, false for other ports
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS
      }
    });
  }

  /**
   * Parse comma-separated email list
   */
  parseEmailList(emailString) {
    if (!emailString) return [];
    return emailString.split(',').map(email => email.trim()).filter(email => email);
  }

  /**
   * Send daily report to team and stakeholders
   */
  async sendDailyReport(report) {
    logger.info('Sending daily report...');

    const subject = `${report.type === 'daily' ? '📊 Daily' : '📈 Weekly'} Performance Report - ${report.date || report.weekEnding}`;
    
    // Send to team members (full report)
    if (this.teamEmails.length > 0) {
      await this.sendEmail({
        to: this.teamEmails,
        subject: `[TEAM] ${subject}`,
        html: report.html,
        text: report.text,
        priority: 'normal'
      });
    }

    // Send to stakeholders (summary version)
    if (this.stakeholderEmails.length > 0) {
      await this.sendEmail({
        to: this.stakeholderEmails,
        subject: `[UPDATE] ${subject}`,
        html: this.generateStakeholderSummary(report),
        text: this.generateStakeholderSummaryText(report),
        priority: 'normal'
      });
    }

    logger.info(`Daily report sent to ${this.teamEmails.length} team members and ${this.stakeholderEmails.length} stakeholders`);
  }

  /**
   * Send weekly report to team and stakeholders
   */
  async sendWeeklyReport(report) {
    logger.info('Sending weekly report...');

    const subject = `📈 Weekly Performance Report - Week ending ${report.weekEnding}`;
    
    // Send comprehensive report to team
    if (this.teamEmails.length > 0) {
      await this.sendEmail({
        to: this.teamEmails,
        subject: `[TEAM] ${subject}`,
        html: report.html,
        text: report.text,
        priority: 'high'
      });
    }

    // Send executive summary to stakeholders
    if (this.stakeholderEmails.length > 0) {
      await this.sendEmail({
        to: this.stakeholderEmails,
        subject: `[EXECUTIVE SUMMARY] ${subject}`,
        html: this.generateExecutiveSummary(report),
        text: this.generateExecutiveSummaryText(report),
        priority: 'high'
      });
    }

    logger.info(`Weekly report sent to ${this.teamEmails.length} team members and ${this.stakeholderEmails.length} stakeholders`);
  }

  /**
   * Send error notification
   */
  async sendErrorNotification(title, error) {
    logger.info('Sending error notification...');

    const subject = `🚨 ERIFY™ Report System Alert: ${title}`;
    const errorMessage = error.message || error.toString();
    
    const html = `
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
      <div style="background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <h2 style="margin: 0 0 10px;">⚠️ System Alert</h2>
        <p><strong>${title}</strong></p>
      </div>
      
      <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3>Error Details:</h3>
        <pre style="background: #fff; padding: 10px; border-radius: 3px; overflow-x: auto;">${errorMessage}</pre>
      </div>
      
      <div style="background: #d1ecf1; border: 1px solid #bee5eb; color: #0c5460; padding: 15px; border-radius: 5px;">
        <h3>Next Steps:</h3>
        <ul>
          <li>Check system logs for detailed information</li>
          <li>Verify API credentials and connections</li>
          <li>Contact the development team if the issue persists</li>
        </ul>
      </div>
      
      <hr style="margin: 20px 0;">
      <p style="color: #666; font-size: 14px;">
        Time: ${new Date().toISOString()}<br>
        System: ERIFY™ Campaign Performance Automation
      </p>
    </body>
    </html>`;

    const text = `
SYSTEM ALERT: ${title}

Error Details:
${errorMessage}

Next Steps:
- Check system logs for detailed information
- Verify API credentials and connections
- Contact the development team if the issue persists

Time: ${new Date().toISOString()}
System: ERIFY™ Campaign Performance Automation`;

    // Send to team members only
    if (this.teamEmails.length > 0) {
      await this.sendEmail({
        to: this.teamEmails,
        subject,
        html,
        text,
        priority: 'high'
      });
    }

    logger.info('Error notification sent to team');
  }

  /**
   * Generate stakeholder summary (shorter version)
   */
  generateStakeholderSummary(report) {
    return `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>ERIFY™ Performance Summary</title>
      <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; background: #f8f9fa; }
        .container { max-width: 600px; margin: 0 auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { background: linear-gradient(135deg, #11C9FF, #FFD700); color: white; padding: 30px; text-align: center; }
        .header h1 { margin: 0; font-size: 24px; font-weight: 900; }
        .content { padding: 30px; }
        .summary { background: #f8f9ff; border-left: 4px solid #11C9FF; padding: 20px; margin-bottom: 30px; border-radius: 4px; }
        .metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 30px; }
        .metric { background: #f8f9fa; padding: 15px; border-radius: 8px; text-align: center; }
        .metric-value { font-size: 24px; font-weight: bold; color: #11C9FF; margin-bottom: 5px; }
        .metric-label { color: #666; font-size: 12px; }
        .footer { background: #f8f9fa; padding: 20px; text-align: center; color: #666; font-size: 14px; }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1>ERIFY™ Performance Summary</h1>
          <p>${report.type === 'weekly' ? `Week ending ${report.weekEnding}` : `${report.date}`}</p>
        </div>
        
        <div class="content">
          <div class="summary">
            <h2>📊 Key Highlights</h2>
            <p><strong>${report.summary.keyHighlight}</strong></p>
          </div>

          <div class="metrics">
            <div class="metric">
              <div class="metric-value">${report.summary.totalEngagements.toLocaleString()}</div>
              <div class="metric-label">Total Engagements</div>
            </div>
            <div class="metric">
              <div class="metric-value">${report.summary.totalConversions}</div>
              <div class="metric-label">Conversions</div>
            </div>
            <div class="metric">
              <div class="metric-value">${report.summary.conversionRate.toFixed(1)}%</div>
              <div class="metric-label">Conversion Rate</div>
            </div>
          </div>

          ${report.alerts && report.alerts.length > 0 ? `
          <div style="background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 6px; padding: 15px; margin-bottom: 20px;">
            <h3>⚠️ Items for Attention</h3>
            ${report.alerts.map(alert => `<p>• ${alert.message}</p>`).join('')}
          </div>
          ` : ''}

          <p style="color: #666; font-size: 14px;">
            For detailed metrics and full analysis, please refer to the complete report sent to the team.
          </p>
        </div>

        <div class="footer">
          <p>ERIFY™ Campaign Performance Automation</p>
        </div>
      </div>
    </body>
    </html>`;
  }

  /**
   * Generate executive summary for weekly reports
   */
  generateExecutiveSummary(report) {
    return `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>ERIFY™ Executive Summary</title>
      <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; background: #f8f9fa; }
        .container { max-width: 700px; margin: 0 auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { background: linear-gradient(135deg, #11C9FF, #FFD700); color: white; padding: 30px; text-align: center; }
        .header h1 { margin: 0; font-size: 28px; font-weight: 900; }
        .content { padding: 30px; }
        .summary { background: #f8f9ff; border-left: 4px solid #11C9FF; padding: 20px; margin-bottom: 30px; border-radius: 4px; }
        .metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 30px; }
        .metric { background: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; }
        .metric-value { font-size: 28px; font-weight: bold; color: #11C9FF; margin-bottom: 5px; }
        .metric-label { color: #666; font-size: 14px; }
        .growth { background: #d4edda; border-left: 4px solid #28a745; padding: 15px; margin-bottom: 20px; border-radius: 4px; }
        .recommendations { background: #e7f3ff; border-left: 4px solid #0066cc; padding: 15px; margin-bottom: 20px; border-radius: 4px; }
        .footer { background: #f8f9fa; padding: 20px; text-align: center; color: #666; font-size: 14px; }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1>ERIFY™ Executive Summary</h1>
          <p>Week ending ${report.weekEnding}</p>
        </div>
        
        <div class="content">
          <div class="summary">
            <h2>📊 Performance Highlights</h2>
            <p><strong>${report.summary.keyHighlight}</strong></p>
          </div>

          <div class="metrics">
            <div class="metric">
              <div class="metric-value">${report.summary.totalEngagements.toLocaleString()}</div>
              <div class="metric-label">Total Engagements</div>
            </div>
            <div class="metric">
              <div class="metric-value">${report.summary.totalConversions}</div>
              <div class="metric-label">Conversions</div>
            </div>
            <div class="metric">
              <div class="metric-value">${report.summary.conversionRate.toFixed(1)}%</div>
              <div class="metric-label">Conversion Rate</div>
            </div>
          </div>

          ${report.summary.weeklyGrowth ? `
          <div class="growth">
            <h3>📈 Growth Metrics</h3>
            <p>
              <strong>Engagements:</strong> ${report.summary.weeklyGrowth.engagements} | 
              <strong>Conversions:</strong> ${report.summary.weeklyGrowth.conversions} | 
              <strong>New Followers:</strong> ${report.summary.weeklyGrowth.newFollowers}
            </p>
          </div>
          ` : ''}

          ${report.trends && report.trends.insights ? `
          <div style="background: #f0f8ff; border-left: 4px solid #0066cc; padding: 15px; margin-bottom: 20px; border-radius: 4px;">
            <h3>🔍 Key Insights</h3>
            <ul>
              ${report.trends.insights.map(insight => `<li>${insight}</li>`).join('')}
            </ul>
          </div>
          ` : ''}

          ${report.recommendations && report.recommendations.length > 0 ? `
          <div class="recommendations">
            <h3>💡 Strategic Recommendations</h3>
            <ul>
              ${report.recommendations.slice(0, 3).map(rec => `<li>${rec}</li>`).join('')}
            </ul>
          </div>
          ` : ''}

          ${report.alerts && report.alerts.length > 0 ? `
          <div style="background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 6px; padding: 15px; margin-bottom: 20px;">
            <h3>⚠️ Items Requiring Attention</h3>
            ${report.alerts.map(alert => `<p>• ${alert.message}</p>`).join('')}
          </div>
          ` : ''}

          <p style="color: #666; font-size: 14px; border-top: 1px solid #eee; padding-top: 15px;">
            This executive summary provides key performance indicators and strategic insights. 
            For detailed breakdowns and technical metrics, the complete report is available to the operations team.
          </p>
        </div>

        <div class="footer">
          <p>ERIFY™ Campaign Performance Automation</p>
          <p>Questions? Contact the ERIFY Team</p>
        </div>
      </div>
    </body>
    </html>`;
  }

  /**
   * Generate plain text versions for stakeholders
   */
  generateStakeholderSummaryText(report) {
    return `
ERIFY™ PERFORMANCE SUMMARY
${report.type === 'weekly' ? `Week ending: ${report.weekEnding}` : `Date: ${report.date}`}

KEY HIGHLIGHTS
${report.summary.keyHighlight}

METRICS
- Total Engagements: ${report.summary.totalEngagements.toLocaleString()}
- Conversions: ${report.summary.totalConversions}
- Conversion Rate: ${report.summary.conversionRate.toFixed(1)}%

${report.alerts && report.alerts.length > 0 ? `
ITEMS FOR ATTENTION
${report.alerts.map(alert => `- ${alert.message}`).join('\n')}
` : ''}

For detailed metrics and full analysis, please refer to the complete report sent to the team.

ERIFY™ Campaign Performance Automation`.trim();
  }

  generateExecutiveSummaryText(report) {
    return `
ERIFY™ EXECUTIVE SUMMARY
Week ending: ${report.weekEnding}

PERFORMANCE HIGHLIGHTS
${report.summary.keyHighlight}

KEY METRICS
- Total Engagements: ${report.summary.totalEngagements.toLocaleString()}
- Conversions: ${report.summary.totalConversions}
- Conversion Rate: ${report.summary.conversionRate.toFixed(1)}%

${report.summary.weeklyGrowth ? `
GROWTH METRICS
- Engagements: ${report.summary.weeklyGrowth.engagements}
- Conversions: ${report.summary.weeklyGrowth.conversions}
- New Followers: ${report.summary.weeklyGrowth.newFollowers}
` : ''}

${report.trends && report.trends.insights ? `
KEY INSIGHTS
${report.trends.insights.map(insight => `- ${insight}`).join('\n')}
` : ''}

${report.recommendations && report.recommendations.length > 0 ? `
STRATEGIC RECOMMENDATIONS
${report.recommendations.slice(0, 3).map(rec => `- ${rec}`).join('\n')}
` : ''}

${report.alerts && report.alerts.length > 0 ? `
ITEMS REQUIRING ATTENTION
${report.alerts.map(alert => `- ${alert.message}`).join('\n')}
` : ''}

This executive summary provides key performance indicators and strategic insights.
For detailed breakdowns and technical metrics, the complete report is available to the operations team.

ERIFY™ Campaign Performance Automation`.trim();
  }

  /**
   * Core email sending function
   */
  async sendEmail({ to, subject, html, text, priority = 'normal' }) {
    try {
      const mailOptions = {
        from: `"ERIFY™ Reports" <${process.env.SMTP_USER}>`,
        to: Array.isArray(to) ? to.join(', ') : to,
        subject,
        html,
        text,
        priority,
        headers: {
          'X-Priority': priority === 'high' ? '1' : '3',
          'X-MSMail-Priority': priority === 'high' ? 'High' : 'Normal'
        }
      };

      const info = await this.transporter.sendMail(mailOptions);
      logger.info(`Email sent successfully: ${info.messageId}`);
      
      return info;
    } catch (error) {
      logger.error('Failed to send email:', error);
      throw error;
    }
  }

  /**
   * Test email configuration
   */
  async testEmailConfig() {
    try {
      await this.transporter.verify();
      logger.info('Email configuration verified successfully');
      return true;
    } catch (error) {
      logger.error('Email configuration test failed:', error);
      return false;
    }
  }
}

module.exports = { EmailNotifier };