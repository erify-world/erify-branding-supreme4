/**
 * Test Suite for ERIFY Campaign Reports Automation
 * Basic test to verify the system components work correctly
 */

const CampaignReportsApp = require('./app');
const { logger } = require('./utils/logger');

async function runTests() {
  logger.info('Starting ERIFY Campaign Reports test suite...');

  try {
    // Test 1: Initialize the application
    logger.info('Test 1: Application initialization');
    const app = new CampaignReportsApp();
    logger.info('✅ Application initialized successfully');

    // Test 2: Generate a test report
    logger.info('Test 2: Generate test report');
    await app.generateTestReport();
    logger.info('✅ Test report generated successfully');

    // Test 3: Test email configuration (if configured)
    logger.info('Test 3: Email configuration test');
    try {
      const isEmailConfigured = await app.emailNotifier.testEmailConfig();
      if (isEmailConfigured) {
        logger.info('✅ Email configuration verified');
      } else {
        logger.warn('⚠️ Email configuration not properly set up (this is expected in development)');
      }
    } catch (error) {
      logger.warn('⚠️ Email test skipped - configuration not available:', error.message);
    }

    logger.info('🎉 All tests completed successfully!');
    logger.info('');
    logger.info('📋 Next steps:');
    logger.info('1. Copy .env.example to .env and configure your credentials');
    logger.info('2. Run "npm start" to start the scheduled automation');
    logger.info('3. Or run "node src/app.js --test" to generate a test report');

  } catch (error) {
    logger.error('❌ Test failed:', error);
    process.exit(1);
  }
}

if (require.main === module) {
  runTests();
}

module.exports = { runTests };