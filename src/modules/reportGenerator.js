/**
 * Report Generator Module
 * Generates comprehensive reports with key metrics:
 * - Engagement (likes, comments, shares across platforms)
 * - Referrals (click-throughs, sign-ups via UTM links)
 * - User Behavior (time spent, demographics, conversion rates)
 */

const { logger } = require('../utils/logger');

class ReportGenerator {
  constructor() {
    this.brandName = 'ERIFY™';
  }

  /**
   * Generate daily performance report
   */
  async generateDailyReport(data) {
    logger.info('Generating daily report...');

    const report = {
      type: 'daily',
      date: new Date().toISOString().split('T')[0],
      period: data.period,
      summary: this.generateSummary(data),
      engagement: this.generateEngagementMetrics(data.engagement),
      referrals: this.generateReferralMetrics(data.referrals),
      userBehavior: this.generateUserBehaviorMetrics(data.userBehavior),
      alerts: this.generateAlerts(data),
      errors: data.errors || []
    };

    report.html = this.generateHtmlReport(report);
    report.text = this.generateTextReport(report);

    return report;
  }

  /**
   * Generate weekly performance report
   */
  async generateWeeklyReport(data) {
    logger.info('Generating weekly report...');

    const report = {
      type: 'weekly',
      weekEnding: new Date().toISOString().split('T')[0],
      period: data.period,
      summary: this.generateWeeklySummary(data),
      engagement: this.generateEngagementMetrics(data.engagement),
      referrals: this.generateReferralMetrics(data.referrals),
      userBehavior: this.generateUserBehaviorMetrics(data.userBehavior),
      trends: this.generateTrendAnalysis(data),
      recommendations: this.generateRecommendations(data),
      errors: data.errors || []
    };

    report.html = this.generateHtmlReport(report);
    report.text = this.generateTextReport(report);

    return report;
  }

  /**
   * Generate executive summary
   */
  generateSummary(data) {
    const totalEngagements = this.calculateTotalEngagements(data.engagement);
    const totalConversions = data.referrals?.totalConversions || 0;
    const conversionRate = data.referrals?.conversionRate || 0;

    return {
      totalEngagements,
      totalConversions,
      conversionRate,
      keyHighlight: this.getKeyHighlight(data)
    };
  }

  /**
   * Generate weekly summary with comparisons
   */
  generateWeeklySummary(data) {
    const summary = this.generateSummary(data);
    
    return {
      ...summary,
      weeklyGrowth: {
        engagements: '+12.5%', // Mock - replace with actual calculation
        conversions: '+8.3%',
        newFollowers: '+15.2%'
      }
    };
  }

  /**
   * Generate engagement metrics across all platforms
   */
  generateEngagementMetrics(engagement = {}) {
    return {
      platforms: {
        twitter: {
          engagements: engagement.twitter?.engagements || 0,
          impressions: engagement.twitter?.impressions || 0,
          engagementRate: engagement.twitter?.engagementRate || 0,
          breakdown: {
            likes: engagement.twitter?.likes || 0,
            retweets: engagement.twitter?.retweets || 0,
            replies: engagement.twitter?.replies || 0
          }
        },
        linkedin: {
          engagements: engagement.linkedin?.engagements || 0,
          impressions: engagement.linkedin?.impressions || 0,
          engagementRate: engagement.linkedin?.engagementRate || 0,
          breakdown: {
            likes: engagement.linkedin?.likes || 0,
            comments: engagement.linkedin?.comments || 0,
            shares: engagement.linkedin?.shares || 0
          }
        },
        facebook: {
          engagements: engagement.facebook?.engagements || 0,
          reach: engagement.facebook?.reach || 0,
          engagementRate: engagement.facebook?.engagementRate || 0,
          breakdown: {
            likes: engagement.facebook?.likes || 0,
            comments: engagement.facebook?.comments || 0,
            shares: engagement.facebook?.shares || 0
          }
        }
      },
      totals: {
        engagements: this.calculateTotalEngagements(engagement),
        averageEngagementRate: this.calculateAverageEngagementRate(engagement)
      }
    };
  }

  /**
   * Generate referral and conversion metrics
   */
  generateReferralMetrics(referrals = {}) {
    return {
      utmCampaigns: referrals.utmCampaigns || {},
      totals: {
        clicks: referrals.totalClicks || 0,
        conversions: referrals.totalConversions || 0,
        conversionRate: referrals.conversionRate || 0
      },
      topPerformers: this.getTopPerformingCampaigns(referrals.utmCampaigns || {})
    };
  }

  /**
   * Generate user behavior metrics
   */
  generateUserBehaviorMetrics(userBehavior = {}) {
    return {
      websiteMetrics: {
        pageViews: userBehavior.pageViews || 0,
        uniqueVisitors: userBehavior.uniqueVisitors || 0,
        averageSessionDuration: userBehavior.averageSessionDuration || 0,
        bounceRate: userBehavior.bounceRate || 0
      },
      topPages: userBehavior.topPages || [],
      userJourney: this.analyzeUserJourney(userBehavior)
    };
  }

  /**
   * Generate performance alerts
   */
  generateAlerts(data) {
    const alerts = [];
    
    // Check for low engagement rates
    const avgEngagementRate = this.calculateAverageEngagementRate(data.engagement);
    if (avgEngagementRate < 5.0) {
      alerts.push({
        type: 'warning',
        message: 'Average engagement rate below 5% threshold',
        value: avgEngagementRate
      });
    }

    // Check for high bounce rate
    if (data.userBehavior?.bounceRate > 40) {
      alerts.push({
        type: 'warning',
        message: 'Website bounce rate above 40% threshold',
        value: data.userBehavior.bounceRate
      });
    }

    // Check for conversion rate drops
    if (data.referrals?.conversionRate < 5.0) {
      alerts.push({
        type: 'alert',
        message: 'Conversion rate below 5% target',
        value: data.referrals.conversionRate
      });
    }

    return alerts;
  }

  /**
   * Generate trend analysis for weekly reports
   */
  generateTrendAnalysis(data) {
    return {
      engagementTrend: 'increasing', // Mock - replace with actual trend calculation
      conversionTrend: 'stable',
      topGrowthPlatform: 'LinkedIn',
      insights: [
        'LinkedIn engagement up 15% this week',
        'Supreme 4 branding content performing well',
        'VIP referral program showing strong conversion'
      ]
    };
  }

  /**
   * Generate actionable recommendations
   */
  generateRecommendations(data) {
    const recommendations = [];

    const avgEngagementRate = this.calculateAverageEngagementRate(data.engagement);
    if (avgEngagementRate < 7.0) {
      recommendations.push('Consider increasing post frequency on high-performing platforms');
    }

    if (data.userBehavior?.bounceRate > 30) {
      recommendations.push('Optimize landing page content and loading speed');
    }

    recommendations.push('Continue focusing on luxury fintech messaging');
    recommendations.push('Expand Supreme 4 branding across all channels');

    return recommendations;
  }

  /**
   * Helper methods
   */
  calculateTotalEngagements(engagement = {}) {
    return (engagement.twitter?.engagements || 0) +
           (engagement.linkedin?.engagements || 0) +
           (engagement.facebook?.engagements || 0);
  }

  calculateAverageEngagementRate(engagement = {}) {
    const rates = [
      engagement.twitter?.engagementRate || 0,
      engagement.linkedin?.engagementRate || 0,
      engagement.facebook?.engagementRate || 0
    ].filter(rate => rate > 0);

    return rates.length > 0 ? rates.reduce((sum, rate) => sum + rate, 0) / rates.length : 0;
  }

  getTopPerformingCampaigns(campaigns) {
    return Object.entries(campaigns)
      .sort((a, b) => b[1].conversions - a[1].conversions)
      .slice(0, 3)
      .map(([name, data]) => ({ name, ...data }));
  }

  getKeyHighlight(data) {
    const totalEngagements = this.calculateTotalEngagements(data.engagement);
    const totalConversions = data.referrals?.totalConversions || 0;
    
    if (totalEngagements > 5000) {
      return `Strong engagement with ${totalEngagements.toLocaleString()} total interactions`;
    } else if (totalConversions > 100) {
      return `Excellent conversion performance with ${totalConversions} conversions`;
    } else {
      return 'Steady performance across all metrics';
    }
  }

  analyzeUserJourney(userBehavior) {
    return {
      averagePageviews: Math.round((userBehavior.pageViews || 0) / (userBehavior.uniqueVisitors || 1)),
      sessionQuality: userBehavior.averageSessionDuration > 3 ? 'high' : 'medium'
    };
  }

  /**
   * Generate HTML email report
   */
  generateHtmlReport(report) {
    const isWeekly = report.type === 'weekly';
    
    return `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>${this.brandName} ${isWeekly ? 'Weekly' : 'Daily'} Performance Report</title>
      <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; background: #f8f9fa; }
        .container { max-width: 800px; margin: 0 auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { background: linear-gradient(135deg, #11C9FF, #FFD700); color: white; padding: 30px; text-align: center; }
        .header h1 { margin: 0; font-size: 28px; font-weight: 900; }
        .header p { margin: 10px 0 0; opacity: 0.9; }
        .content { padding: 30px; }
        .summary { background: #f8f9ff; border-left: 4px solid #11C9FF; padding: 20px; margin-bottom: 30px; border-radius: 4px; }
        .metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .metric { background: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; }
        .metric-value { font-size: 32px; font-weight: bold; color: #11C9FF; margin-bottom: 5px; }
        .metric-label { color: #666; font-size: 14px; }
        .section { margin-bottom: 30px; }
        .section h2 { color: #333; border-bottom: 2px solid #11C9FF; padding-bottom: 10px; }
        .platform { background: #f8f9fa; padding: 15px; margin-bottom: 15px; border-radius: 6px; }
        .platform h3 { margin: 0 0 10px; color: #11C9FF; }
        .platform-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; }
        .stat { text-align: center; }
        .stat-value { font-weight: bold; font-size: 18px; }
        .stat-label { font-size: 12px; color: #666; }
        .alerts { background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 6px; padding: 15px; margin-bottom: 20px; }
        .alert { margin-bottom: 10px; }
        .alert:last-child { margin-bottom: 0; }
        .footer { background: #f8f9fa; padding: 20px; text-align: center; color: #666; font-size: 14px; }
        .trend-up { color: #28a745; }
        .trend-down { color: #dc3545; }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1>${this.brandName} ${isWeekly ? 'Weekly' : 'Daily'} Performance Report</h1>
          <p>${isWeekly ? `Week ending ${report.weekEnding}` : `Date: ${report.date}`}</p>
        </div>
        
        <div class="content">
          <div class="summary">
            <h2>📊 Executive Summary</h2>
            <p><strong>${report.summary.keyHighlight}</strong></p>
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
          </div>

          ${report.alerts.length > 0 ? `
          <div class="alerts">
            <h3>⚠️ Alerts & Notifications</h3>
            ${report.alerts.map(alert => `
              <div class="alert">
                <strong>${alert.type.toUpperCase()}:</strong> ${alert.message}
                ${alert.value ? ` (${alert.value}${alert.message.includes('rate') ? '%' : ''})` : ''}
              </div>
            `).join('')}
          </div>
          ` : ''}

          <div class="section">
            <h2>📱 Social Media Engagement</h2>
            ${Object.entries(report.engagement.platforms).map(([platform, data]) => `
              <div class="platform">
                <h3>${platform.charAt(0).toUpperCase() + platform.slice(1)}</h3>
                <div class="platform-stats">
                  <div class="stat">
                    <div class="stat-value">${data.engagements.toLocaleString()}</div>
                    <div class="stat-label">Engagements</div>
                  </div>
                  <div class="stat">
                    <div class="stat-value">${(data.impressions || data.reach || 0).toLocaleString()}</div>
                    <div class="stat-label">${data.impressions ? 'Impressions' : 'Reach'}</div>
                  </div>
                  <div class="stat">
                    <div class="stat-value">${data.engagementRate.toFixed(1)}%</div>
                    <div class="stat-label">Engagement Rate</div>
                  </div>
                </div>
              </div>
            `).join('')}
          </div>

          <div class="section">
            <h2>🔗 Referral Performance</h2>
            <div class="metrics">
              <div class="metric">
                <div class="metric-value">${report.referrals.totals.clicks.toLocaleString()}</div>
                <div class="metric-label">Total Clicks</div>
              </div>
              <div class="metric">
                <div class="metric-value">${report.referrals.totals.conversions}</div>
                <div class="metric-label">Conversions</div>
              </div>
              <div class="metric">
                <div class="metric-value">${report.referrals.totals.conversionRate.toFixed(1)}%</div>
                <div class="metric-label">Conversion Rate</div>
              </div>
            </div>
            
            ${report.referrals.topPerformers.length > 0 ? `
            <h3>🏆 Top Performing Campaigns</h3>
            ${report.referrals.topPerformers.map((campaign, index) => `
              <div class="platform">
                <h4>${index + 1}. ${campaign.name.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</h4>
                <div class="platform-stats">
                  <div class="stat">
                    <div class="stat-value">${campaign.clicks}</div>
                    <div class="stat-label">Clicks</div>
                  </div>
                  <div class="stat">
                    <div class="stat-value">${campaign.conversions}</div>
                    <div class="stat-label">Conversions</div>
                  </div>
                </div>
              </div>
            `).join('')}
            ` : ''}
          </div>

          <div class="section">
            <h2>👥 User Behavior</h2>
            <div class="metrics">
              <div class="metric">
                <div class="metric-value">${report.userBehavior.websiteMetrics.pageViews.toLocaleString()}</div>
                <div class="metric-label">Page Views</div>
              </div>
              <div class="metric">
                <div class="metric-value">${report.userBehavior.websiteMetrics.uniqueVisitors.toLocaleString()}</div>
                <div class="metric-label">Unique Visitors</div>
              </div>
              <div class="metric">
                <div class="metric-value">${report.userBehavior.websiteMetrics.averageSessionDuration.toFixed(1)}m</div>
                <div class="metric-label">Avg Session</div>
              </div>
              <div class="metric">
                <div class="metric-value">${report.userBehavior.websiteMetrics.bounceRate.toFixed(1)}%</div>
                <div class="metric-label">Bounce Rate</div>
              </div>
            </div>
          </div>

          ${isWeekly && report.recommendations ? `
          <div class="section">
            <h2>💡 Recommendations</h2>
            <ul>
              ${report.recommendations.map(rec => `<li>${rec}</li>`).join('')}
            </ul>
          </div>
          ` : ''}
        </div>

        <div class="footer">
          <p>Generated by ${this.brandName} Campaign Performance Automation</p>
          <p>For questions, contact the ERIFY Team</p>
        </div>
      </div>
    </body>
    </html>`;
  }

  /**
   * Generate plain text report for fallback
   */
  generateTextReport(report) {
    const isWeekly = report.type === 'weekly';
    
    return `
${this.brandName} ${isWeekly ? 'WEEKLY' : 'DAILY'} PERFORMANCE REPORT
${isWeekly ? `Week ending: ${report.weekEnding}` : `Date: ${report.date}`}
${'='.repeat(60)}

EXECUTIVE SUMMARY
${report.summary.keyHighlight}

Key Metrics:
- Total Engagements: ${report.summary.totalEngagements.toLocaleString()}
- Conversions: ${report.summary.totalConversions}
- Conversion Rate: ${report.summary.conversionRate.toFixed(1)}%

${report.alerts.length > 0 ? `
ALERTS & NOTIFICATIONS
${report.alerts.map(alert => `- ${alert.type.toUpperCase()}: ${alert.message}`).join('\n')}
` : ''}

SOCIAL MEDIA ENGAGEMENT
${Object.entries(report.engagement.platforms).map(([platform, data]) => `
${platform.toUpperCase()}:
- Engagements: ${data.engagements.toLocaleString()}
- ${data.impressions ? 'Impressions' : 'Reach'}: ${(data.impressions || data.reach || 0).toLocaleString()}
- Engagement Rate: ${data.engagementRate.toFixed(1)}%`).join('\n')}

REFERRAL PERFORMANCE
- Total Clicks: ${report.referrals.totals.clicks.toLocaleString()}
- Conversions: ${report.referrals.totals.conversions}
- Conversion Rate: ${report.referrals.totals.conversionRate.toFixed(1)}%

USER BEHAVIOR
- Page Views: ${report.userBehavior.websiteMetrics.pageViews.toLocaleString()}
- Unique Visitors: ${report.userBehavior.websiteMetrics.uniqueVisitors.toLocaleString()}
- Average Session: ${report.userBehavior.websiteMetrics.averageSessionDuration.toFixed(1)} minutes
- Bounce Rate: ${report.userBehavior.websiteMetrics.bounceRate.toFixed(1)}%

${isWeekly && report.recommendations ? `
RECOMMENDATIONS
${report.recommendations.map(rec => `- ${rec}`).join('\n')}
` : ''}

Generated by ${this.brandName} Campaign Performance Automation
    `.trim();
  }
}

module.exports = { ReportGenerator };