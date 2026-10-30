#!/usr/bin/env node

/**
 * Test script for Mission Control integration
 */

const http = require('http');

const MISSION_CONTROL_URL = 'http://localhost:4001';

function testMissionControlAPI() {
  console.log('🧪 Testing Mission Control API...\n');

  // Test health endpoint
  http.get(`${MISSION_CONTROL_URL}/api/health`, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      try {
        const health = JSON.parse(data);
        console.log('✅ Health check passed:');
        console.log(`   Gateway: ${health.gateway ? 'Connected' : 'Disconnected'}`);
        console.log(`   Model: ${health.model || 'N/A'}`);
        console.log(`   Active tasks: ${health.activeTasks || 0}`);
        console.log('');

        // Test creating a task
        const testTask = {
          description: 'Test task from OpenClaw Telegram integration',
          priority: 'medium'
        };

        const postReq = http.request({
          hostname: 'localhost',
          port: 4001,
          path: '/api/tasks',
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          }
        }, (postRes) => {
          let postData = '';
          postRes.on('data', chunk => postData += chunk);
          postRes.on('end', () => {
            try {
              const task = JSON.parse(postData);
              console.log('✅ Task creation test passed:');
              console.log(`   Task ID: ${task.id}`);
              console.log(`   Description: ${task.description}`);
              console.log(`   Status: ${task.status}`);
              console.log('');

              // Test listing tasks
              http.get(`${MISSION_CONTROL_URL}/api/tasks`, (listRes) => {
                let listData = '';
                listRes.on('data', chunk => listData += chunk);
                listRes.on('end', () => {
                  try {
                    const tasks = JSON.parse(listData);
                    console.log('✅ Task listing test passed:');
                    console.log(`   Total tasks: ${tasks.length}`);
                    console.log('');

                    console.log('🎉 All tests passed! Mission Control is ready.');
                    console.log('\n📱 You can now use these commands in Telegram (@rogermac_bot):');
                    console.log('   /mission create <task description>');
                    console.log('   /mission list');
                    console.log('   /mission status <task-id>');
                    console.log('   /mission cancel <task-id>');
                    console.log('   /mission health');
                  } catch (err) {
                    console.error('❌ Error parsing task list:', err.message);
                  }
                });
              });
            } catch (err) {
              console.error('❌ Error parsing task response:', err.message);
            }
          });
        });

        postReq.on('error', (err) => {
          console.error('❌ Error creating task:', err.message);
        });

        postReq.write(JSON.stringify(testTask));
        postReq.end();
      } catch (err) {
        console.error('❌ Error parsing health check:', err.message);
      }
    });
  }).on('error', (err) => {
    console.error('❌ Mission Control not reachable:', err.message);
    console.log('\n💡 Make sure Mission Control is running:');
    console.log('   cd /Users/USERNAME/mission-control');
    console.log('   npm run dev');
  });
}

testMissionControlAPI();
