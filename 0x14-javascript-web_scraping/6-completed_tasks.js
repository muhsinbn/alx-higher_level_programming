#!/usr/bin/node
// A script that computes the number of tasks completed by user ID
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksCount = tasks.reduce((acc, task) => {
      if (task.completed) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(completedTasksCount);
  }
});
